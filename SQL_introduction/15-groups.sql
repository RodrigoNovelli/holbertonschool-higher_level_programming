-- Making a script in SQL thst gropus dsts with same values
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;