-- Making a script that shows every value
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY    score DESC;