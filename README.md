you are a Python developer, Develop a web application for E-learning that allows administrators to create and manage courses, including adding lessons, quizzes, and assignments. track all user progress and course completion.
Administrators need a dashboard analysis of course activities.

learners can view and search for available courses. they can visualize their progress after enrollment.
Built it using Flask, SQLite. make sure the REST API is asynchronous using Asyncio.

- Course Creation:
    Add course title, description, and category.
    Upload course materials (PDFs, videos, external links).

- Lesson Management:
    Create lessons with rich text and media support.
    Organize lessons in a structured order.

- Quiz Creation:
    Add multiple-choice, true/false, and short-answer questions.
    Set quiz duration, passing score, and review options.

- Assignment Management:
    Upload assignments with detailed instructions.
    Set deadlines and grading criteria.

- User Progress Tracking Module

   - Objective: Track user engagement and performance in real-time.
    Key Features:
        Progress Visualization:
            Dashboard displaying completed and pending lessons.
            Course completion percentage for users.
        Quiz and Assignment Tracking:
            Track scores, attempts, and submission status.
            Provide feedback on completed quizzes and assignments.
        Certificate Generation:
            Issue certificates upon course completion.
    Technologies:
        Database: SQLite for storing user progress data.
        Analytics: Python with Plotly