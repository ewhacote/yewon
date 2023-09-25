# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/59414

-- 코드를 입력하세요
SELECT animal_id, name, DATE_FORMAT(datetime, '%Y-%m-%d') 
FROM animal_ins
ORDER BY 1;
