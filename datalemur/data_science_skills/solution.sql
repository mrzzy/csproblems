
SELECT c.candidate_id FROM candidates c
INNER JOIN candidates c2 ON c2.candidate_id = c.candidate_id AND c2.skill = 'Tableau'
INNER JOIN candidates c3 ON c3.candidate_id = c.candidate_id AND c3.skill = 'PostgreSQL'
WHERE c.skill = 'Python'
