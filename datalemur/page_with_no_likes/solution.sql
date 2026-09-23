--
-- CSProblems
-- Datalemur
-- DL4. Page with No Likes
--

SELECT p.page_id
FROM pages p
WHERE p.page_id NOT IN (SELECT DISTINCT page_id FROM page_likes)
