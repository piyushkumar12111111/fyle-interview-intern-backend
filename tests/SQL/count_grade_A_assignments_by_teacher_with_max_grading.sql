-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherGradingCount AS (
    SELECT 
        teacher_id, 
        COUNT(*) AS graded_count,
        COUNT(CASE WHEN grade = 'A' THEN 1 END) AS grade_A_count
    FROM 
        assignments 
    WHERE 
        grade IS NOT NULL 
    GROUP BY 
        teacher_id
    ORDER BY 
        graded_count DESC, 
        grade_A_count DESC
    LIMIT 1
)
SELECT 
    grade_A_count
FROM 
    TeacherGradingCount;