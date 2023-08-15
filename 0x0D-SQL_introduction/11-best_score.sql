--  the script lists all records with score >= 10 in table second_table of database hbtn_0c_0 in MySQL server.

SELECT score,
    name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
