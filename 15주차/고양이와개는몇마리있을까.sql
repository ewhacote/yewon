# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/59040

-- 코드를 입력하세요
SELECT animal_type, count(*) as count
from animal_ins
group by animal_type
having animal_type in ('cat', 'dog')
order by 1
