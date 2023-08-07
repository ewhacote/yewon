문제 https://school.programmers.co.kr/learn/courses/30/lessons/132202

-- 2022년 5월에 예약한 환자 수를 진료과코드 별로 조회
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE YEAR(APNT_YMD)=2022 AND MONTH(APNT_YMD) = 5
-- WHERE APNT_YMD LIKE '2022-05%'
GROUP BY MCDP_CD
ORDER BY 2, 1;
