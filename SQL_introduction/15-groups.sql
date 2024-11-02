-- Making a script in SQL thst gropus dsts with same values
SELECT score, COUNT(*) AS recorded
FROM second_table
GROUP BY score
ORDER BY recorded DESC;