import React from 'react';

const CoursesPage: React.FC = () => {
    return (
        <div className="p-6">
            <h1 className="text-3xl font-bold text-center mb-8">All Courses</h1>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                {/* Replace with dynamic course data */}
                <div className="bg-white shadow-md rounded-lg p-4 hover:shadow-lg transition-shadow">
                    <h2 className="text-xl font-semibold text-blue-600 mb-2">Course 1</h2>
                    <p className="text-gray-600 mb-4">Learn the basics of Course 1.</p>
                    <a
                        href="/courses/1"
                        className="inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
                    >
                        View Details
                    </a>
                </div>
                <div className="bg-white shadow-md rounded-lg p-4 hover:shadow-lg transition-shadow">
                    <h2 className="text-xl font-semibold text-blue-600 mb-2">Course 2</h2>
                    <p className="text-gray-600 mb-4">Explore the advanced topics in Course 2.</p>
                    <a
                        href="/courses/2"
                        className="inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
                    >
                        View Details
                    </a>
                </div>
                <div className="bg-white shadow-md rounded-lg p-4 hover:shadow-lg transition-shadow">
                    <h2 className="text-xl font-semibold text-blue-600 mb-2">Course 3</h2>
                    <p className="text-gray-600 mb-4">Master the skills in Course 3.</p>
                    <a
                        href="/courses/3"
                        className="inline-block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
                    >
                        View Details
                    </a>
                </div>
            </div>
        </div>
    );
};

export default CoursesPage;