# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/59041

-- 코드를 입력하세요
SELECT name, count(*) as count
from animal_ins
group by name
having count >= 2 and name is not null
order by name
