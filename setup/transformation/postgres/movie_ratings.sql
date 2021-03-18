CREATE TABLE movies_rating AS
WITH average_ratings AS (
    SELECT
        "movieId"     AS id,
        AVG(rating)   AS avg_rating,
        COUNT(rating) AS number_of_ratings
    FROM ratings
    GROUP BY 1
)
SELECT
    movies.id                                       AS id,
    REGEXP_REPLACE(movies.title, '\s\(\d{4}\)', '') AS title,
    SUBSTRING(movies.title, '\s\((\d{4})\)')        AS published,
    CASE WHEN average_ratings.avg_rating IS NULL
        THEN false
        ELSE true
    END                                             AS is_rated,
    round(average_ratings.avg_rating::NUMERIC, 2)   AS avg_rating,
    average_ratings.number_of_ratings               AS number_of_ratings
FROM movies
LEFT JOIN average_ratings ON movies.id = average_ratings.id;
