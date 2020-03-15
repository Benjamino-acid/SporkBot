import sys
import mysql.connector
import sql

subcommand = sys.argv[1];
user_id = sys.argv[len(sys.argv) - 1];

if(subcommand.lower() == "help"):
	print "Todo & MyTodo help"
	print "Manage your team's, and your personal todolist"
	print "\tUsage : todo help => get this help menu"
	print "\tUsage : todo [ text to add to list ] => add item to the list"
	print "\tUsage : todo list => list all todo items"
	print "\tUsage : todo done # => makes item # ( number ) as completed"
        print "\t\tNote : to manage your personal todo list, type mytodo instead of todo"
	
elif(subcommand.lower() == "list"):
	# get list of not completed items, by user, ordered by created date
	cnx = sql.getsqlconnector()
        cursor = cnx.cursor()

        query = ("select id, itemtext from todoitems where user_id = %(user_id)s and completed = 0 order by createddate ")

        data = {
                'user_id' : user_id,
        }

        cursor.execute(query, data)
        i = 1;
	for (id, itemtext) in cursor:
		print "{})  {}".format(i,itemtext)
		i = i + 1
	if(i == 1):
		print "No items in your list"
        cursor.close()
        cnx.close()
elif(subcommand.lower() == "completed" or subcommand.lower() == "done"):
	itemtomark = ' '.join(map(str, sys.argv[2:len(sys.argv)-1]))
	itemtomark = itemtomark.strip()
	cnx = sql.getsqlconnector()
        cursor = cnx.cursor()

        query = ("select id, itemtext from todoitems where user_id = %(user_id)s and completed = 0 order by createddate ")

        data = {
                'user_id' : user_id,
        }

        cursor.execute(query, data)
        i = 1;
        updateid = ''
	updateitemtext = ''
	for (id, itemtext) in cursor:
                if(itemtomark == str(i)):
			updateid = str(id)
			updateitemtext = itemtext
               	i = i + 1

        cursor.close()
        cnx.close()	

	cnx = sql.getsqlconnector()
        cursor = cnx.cursor()
	update_item = ("update todoitems set completed = 1 where id = %(id)s ")
        update_data = {
        	'id' : updateid,
        }
        
	cursor.execute(update_item, update_data)
        
	print 'Item marked completed : ' + updateitemtext

	cnx.commit()
	cursor.close()
        cnx.close()

else:
	#add all text to the database

	cnx = sql.getsqlconnector()
	cursor = cnx.cursor()

	add_item = ("Insert into todoitems (user_id, itemtext) values (%(user_id)s,%(itemtext)s ) ")

	text = ' '.join(map(str, sys.argv[1:len(sys.argv)-1])) 

	if(len(text.strip()) == 0):
		print "No text supplied to add"

	else:
		data_item = {
			'user_id' : user_id,
			'itemtext' : text,
		}

		cursor.execute(add_item, data_item)

		cnx.commit()
		cursor.close()
		cnx.close()
	
		print "Item added successfully : " + text;

