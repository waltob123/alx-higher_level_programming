-- lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT `id`, `name` FROM `cities` 
WHERE EXISTS 
(SELECT `id` FROM `states` WHERE `cities`.`state_id` = `id`);

