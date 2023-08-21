#!/usr/bin/python3
'''cities_by_state module

A script that lists all cities from  the database hbtn_0e_4_usa.
The script takes in 3 arguments (username, password,database_name).
'''

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.excute("SELECT `c`.`id`, `c`.`name`, `s`.`name` FROM`
            cities`  as c INNER JOIN `states` as `s` ON `c`.`id`
            = `s`.`id` ORDER BY `cities`.`id` ASC")
    [print(city) for city in cursor.fetchall()]
