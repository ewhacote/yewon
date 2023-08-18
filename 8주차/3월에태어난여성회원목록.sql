SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth, '%Y-%m-%d')
FROM member_profile
WHERE Month(date_of_birth) = '03' AND gender = 'W' AND tlno IS NOT NULL
ORDER BY member_id;
