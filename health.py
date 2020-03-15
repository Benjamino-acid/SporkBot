import sys
import mysql.connector
import sql

cnx = sql.getsqlconnector()
cursor = cnx.cursor()

query = ("SELECT concat('Today Logs : ',CAST(count(*) AS CHAR)) data1 FROM requestlogs where createddate > DATE(now())  union SELECT concat('Total Logs : ',CAST(count(*) AS CHAR)) FROM requestlogs union SELECT concat('New Todo Items : ',CAST(count(*) AS CHAR)) FROM todoitems where createddate > DATE(now())  union SELECT concat('Total Todo Items : ',CAST(count(*) AS CHAR)) FROM todoitems union select concat('Unique Users : ', CAST(count(*) as CHAR)) from ( select distinct user_id from requestlogs ) a")

cursor.execute(query)
i = 1;
for (dr) in cursor:
	print( dr[0] )
	i = i + 1
if(i == 1):
	print "No items in spork health"
cursor.close()
cnx.close()


