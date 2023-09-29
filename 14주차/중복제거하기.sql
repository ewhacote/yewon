# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/59408

-- 코드를 입력하세요
SELECT COUNT(distinct(NAME)) AS 'COUNT'
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
