-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherGradingCount AS (
    SELECT teacher_id, COUNT(*) AS graded_count FROM assignments 
    WHERE grade IS NOT NULL 
    GROUP BY teacher_id
),
TopTeacher AS (
    SELECT teacher_id FROM TeacherGradingCount
    ORDER BY graded_count DESC
    LIMIT 1
)
SELECT 
    COUNT(*) AS grade_A_count
FROM 
    assignments
WHERE 
    teacher_id = (SELECT teacher_id FROM TopTeacher)
    AND grade = 'A';