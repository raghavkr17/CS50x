SELECT DISTINCT p.name
FROM people p
JOIN movie_cast mc1 ON p.id = mc1.person_id
JOIN movies m1 ON mc1.movie_id = m1.id
JOIN movie_cast mc2 ON m1.id = mc2.movie_id
JOIN people p2 ON mc2.person_id = p2.id
WHERE p2.name = 'Kevin Bacon' AND p2.birth_year = 1958 AND p.name <> 'Kevin Bacon';
