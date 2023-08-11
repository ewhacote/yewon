# 문제 https://school.programmers.co.kr/learn/courses/30/lessons/131533

-- 코드를 입력하세요
SELECT p.product_code, SUM(p.price * o.sales_amount) sales
FROM product p
JOIN offline_sale o
ON (p.product_id = o.product_id)
GROUP BY p.product_id
ORDER BY sales DESC, p.product_code;
