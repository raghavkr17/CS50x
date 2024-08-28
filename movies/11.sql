SELECT title
FROM movies
JOIN movie_cast mc ON movies.id = mc.movie_id
JOIN people p ON mc.person_id = p.id
WHERE p.name = 'Chadwick Boseman'
ORDER BY imdb_rating DESC
LIMIT 5;
