# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/59410

-- 코드를 입력하세요
SELECT animal_type, COALESCE(name, 'No name') AS name, SEX_UPON_INTAKe
FROM animal_ins
ORDER BY animal_id;
