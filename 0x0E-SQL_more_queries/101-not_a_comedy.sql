-- script lists with no comedy genre in database hbtn_0d_tvshows and
-- sorted in ascending order


SELECT DISTINCT `title`
  FROM `tv_shows` AS show
       LEFT JOIN `tv_show_genres` AS show_genre
       ON show_genre.`show_id` = show.`id`

       LEFT JOIN `tv_genres` AS genre
       ON genre.`id` = show_genre.`genre_id`
       WHERE show.`title` NOT IN
             (SELECT `title`
		FROM `tv_shows` AS show
		     INNER JOIN `tv_show_genres` AS show_genre
				 ON show_genre.`show_id` = show.`id`

		     INNER JOIN `tv_genres` AS genre
		     ON genre.`id` = show_genre.`genre_id`
		     WHERE genre.`name` = "Comedy"
ORDER BY `title`;
