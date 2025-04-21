// filepath: frontend/courses-nextjs-ui/app/courses/[id]/page.tsx
import React from 'react';

interface CoursePageProps {
    params: { id: string };
}

const CoursePage: React.FC<CoursePageProps> = ({ params }) => {
    const { id } = params;

    return (
        <div>
            <h1>Course Details</h1>
            <p>Course ID: {id}</p>
            {/* Fetch and display course details here */}
        </div>
    );
};

export default CoursePage;