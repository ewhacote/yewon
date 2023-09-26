# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/59412

-- 코드를 입력하세요
SELECT 
    HOUR(DATETIME),
    COUNT(ANIMAL_ID)
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN '09' AND '19'
GROUP BY 1
ORDER BY 1
