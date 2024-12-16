import asyncio
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.future import select
from datetime import datetime

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this!
jwt = JWTManager(app)

# Database setup
DATABASE_URL = "sqlite+aiosqlite:///elearning.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    image = Column(String)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Lesson(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    title = Column(String, nullable=False)
    content_type = Column(String, nullable=False)  # 'video' or 'text'
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserCourse(Base):
    __tablename__ = 'user_courses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    assigned_at = Column(DateTime, default=datetime.utcnow)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(init_db())

# Helper functions
async def get_pagination_params():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return page, per_page

# Course Management Endpoints
@app.route('/courses', methods=['POST'])
@jwt_required()
async def create_course():
    """
    Create a new course
    ---
    tags:
      - Courses
    parameters:
      - in: body
        name: course
        schema:
          type: object
          required:
            - name
            - description
            - image
            - category
          properties:
            name:
              type: string
            description:
              type: string
            image:
              type: string
            category:
              type: string
    responses:
      201:
        description: Course created successfully
      400:
        description: Invalid input
    """
    data = request.json
    if not all(k in data for k in ('name', 'description', 'image', 'category')):
        return jsonify({"error": "Missing required fields"}), 400
    
    async with async_session() as session:
        new_course = Course(**data)
        session.add(new_course)
        await session.commit()
    
    return jsonify({"message": "Course created successfully"}), 201

@app.route('/courses/<int:course_id>', methods=['PUT'])
@jwt_required()
async def update_course(course_id):
    """
    Update an existing course
    ---
    tags:
      - Courses
    parameters:
      - in: path
        name: course_id
        required: true
        type: integer
      - in: body
        name: course
        schema:
          type: object
          properties:
            name:
              type: string
            description:
              type: string
            image:
              type: string
            category:
              type: string
    responses:
      200:
        description: Course updated successfully
      404:
        description: Course not found
    """
    data = request.json
    async with async_session() as session:
        course = await session.get(Course, course_id)
        if not course:
            return jsonify({"error": "Course not found"}), 404
        
        for key, value in data.items():
            setattr(course, key, value)
        
        await session.commit()
    
    return jsonify({"message": "Course updated successfully"})

@app.route('/courses/<int:course_id>', methods=['DELETE'])
@jwt_required()
async def delete_course(course_id):
    """
    Delete a course
    ---
    tags:
      - Courses
    parameters:
      - in: path
        name: course_id
        required: true
        type: integer
    responses:
      200:
        description: Course deleted successfully
      404:
        description: Course not found
    """
    async with async_session() as session:
        course = await session.get(Course, course_id)
        if not course:
            return jsonify({"error": "Course not found"}), 404
        
        await session.delete(course)
        await session.commit()
    
    return jsonify({"message": "Course deleted successfully"})

@app.route('/courses', methods=['GET'])
async def get_courses():
    """
    Retrieve all courses with pagination
    ---
    tags:
      - Courses
    parameters:
      - in: query
        name: page
        type: integer
      - in: query
        name: per_page
        type: integer
    responses:
      200:
        description: List of courses
    """
    page, per_page = await get_pagination_params()
    
    async with async_session() as session:
        query = select(Course).limit(per_page).offset((page - 1) * per_page)
        result = await session.execute(query)
        courses = result.scalars().all()
    
    return jsonify([{
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "image": course.image,
        "category": course.category
    } for course in courses])

# Lesson Management Endpoints
@app.route('/lessons', methods=['POST'])
@jwt_required()
async def create_lesson():
    """
    Create a new lesson (video or text)
    ---
    tags:
      - Lessons
    parameters:
      - in: body
        name: lesson
        schema:
          type: object
          required:
            - course_id
            - title
            - content_type
            - content
          properties:
            course_id:
              type: integer
            title:
              type: string
            content_type:
              type: string
              enum: [video, text]
            content:
              type: string
    responses:
      201:
        description: Lesson created successfully
      400:
        description: Invalid input
    """
    data = request.json
    if not all(k in data for k in ('course_id', 'title', 'content_type', 'content')):
        return jsonify({"error": "Missing required fields"}), 400
    
    if data['content_type'] not in ['video', 'text']:
        return jsonify({"error": "Invalid content type"}), 400
    
    async with async_session() as session:
        new_lesson = Lesson(**data)
        session.add(new_lesson)
        await session.commit()
    
    return jsonify({"message": "Lesson created successfully"}), 201

@app.route('/lessons/<int:lesson_id>', methods=['PUT'])
@jwt_required()
async def update_lesson(lesson_id):
    """
    Update an existing lesson
    ---
    tags:
      - Lessons
    parameters:
      - in: path
        name: lesson_id
        required: true
        type: integer
      - in: body
        name: lesson
        schema:
          type: object
          properties:
            title:
              type: string
            content_type:
              type: string
              enum: [video, text]
            content:
              type: string
    responses:
      200:
        description: Lesson updated successfully
      404:
        description: Lesson not found
    """
    data = request.json
    async with async_session() as session:
        lesson = await session.get(Lesson, lesson_id)
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404
        
        for key, value in data.items():
            setattr(lesson, key, value)
        
        await session.commit()
    
    return jsonify({"message": "Lesson updated successfully"})

@app.route('/lessons/<int:lesson_id>', methods=['DELETE'])
@jwt_required()
async def delete_lesson(lesson_id):
    """
    Delete a lesson
    ---
    tags:
      - Lessons
    parameters:
      - in: path
        name: lesson_id
        required: true
        type: integer
    responses:
      200:
        description: Lesson deleted successfully
      404:
        description: Lesson not found
    """
    async with async_session() as session:
        lesson = await session.get(Lesson, lesson_id)
        if not lesson:
            return jsonify({"error": "Lesson not found"}), 404
        
        await session.delete(lesson)
        await session.commit()
    
    return jsonify({"message": "Lesson deleted successfully"})

@app.route('/lessons', methods=['GET'])
async def get_lessons():
    """
    Retrieve all lessons with pagination
    ---
    tags:
      - Lessons
    parameters:
      - in: query
        name: page
        type: integer
      - in: query
        name: per_page
        type: integer
    responses:
      200:
        description: List of lessons
    """
    page, per_page = await get_pagination_params()
    
    async with async_session() as session:
        query = select(Lesson).limit(per_page).offset((page - 1) * per_page)
        result = await session.execute(query)
        lessons = result.scalars().all()
    
    return jsonify([{
        "id": lesson.id,
        "course_id": lesson.course_id,
        "title": lesson.title,
        "content_type": lesson.content_type,
        "content": lesson.content
    } for lesson in lessons])

# User-Course Interaction Endpoints
@app.route('/assign-course', methods=['POST'])
@jwt_required()
async def assign_course():
    """
    Assign a course to a user
    ---
    tags:
      - User-Course
    parameters:
      - in: body
        name: assignment
        schema:
          type: object
          required:
            - user_id
            - course_id
          properties:
            user_id:
              type: integer
            course_id:
              type: integer
    responses:
      201:
        description: Course assigned successfully
      400:
        description: Invalid input
    """
    data = request.json
    if not all(k in data for k in ('user_id', 'course_id')):
        return jsonify({"error": "Missing required fields"}), 400
    
    async with async_session() as session:
        new_assignment = UserCourse(**data)
        session.add(new_assignment)
        await session.commit()
    
    return jsonify({"message": "Course assigned successfully"}), 201

@app.route('/user-courses/<int:user_id>', methods=['GET'])
@jwt_required()
async def get_user_courses(user_id):
    """
    Get all courses assigned to a user
    ---
    tags:
      - User-Course
    parameters:
      - in: path
        name: user_id
        required: true
        type: integer
    responses:
      200:
        description: List of courses assigned to the user
    """
    async with async_session() as session:
        query = select(UserCourse).where(UserCourse.user_id == user_id)
        result = await session.execute(query)
        user_courses = result.scalars().all()
    
    course_ids = [uc.course_id for uc in user_courses]
    
    async with async_session() as session:
        query = select(Course).where(Course.id.in_(course_ids))
        result = await session.execute(query)
        courses = result.scalars().all()
    
    return jsonify([{
        "id": course.id,
        "name": course.name,
        "description": course.description,
        "image": course.image,
        "category": course.category
    } for course in courses])

if __name__ == '__main__':
    app.run(debug=True)