-- the script Lists shows from hbtn_0d_tvshows_rate by rating.
-- and sorted in descending order


SELECT `title`, SUM(`rate`) AS `rating`
  FROM `tv_shows` AS show
       INNER JOIN `tv_show_ratings` AS rate
       ON show.`id` = rate.`show_id`
 GROUP BY `title`
 ORDER BY `rating` DESC
