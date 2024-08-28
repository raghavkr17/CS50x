SELECT ROUND(AVG(rating), 2) AS average_rating
FROM ratings, movies
WHERE year = 2012;
