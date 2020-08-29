import mysql.connector


# conn = mysql.connector.connect(
#     host='localhost', user='h-takada', password='7010mogu')

# cursor = conn.cursor()

# cursor.execute('CREATE DATABASE test_mysql_database')

# cursor.close()
# conn.close()

conn = mysql.connector.connect(
    host='localhost', database='test_mysql_database', password='7010mogu')
cursor = conn.cursor()
# cursor.execute('CREATE TABLE persons('
#                'id int NOT NULL AUTO_INCREMENT,'
#                'name varchar(14) NOT NULL,'
#                'PRIMARY KEY(id))')

cursor.execute('INSERT INTO persons(name) values("Mike")')
conn.commit()

cursor.execute('SELECT * FROM persons')
for row in cursor:
    print(row)

# cursor.execute('UPDATE persons set name ="MIchel" WHERE name = "Mike"')
# cursor.execute('DELETE FROM persons WHERE name = "Mike"')

cursor.close()
conn.close()
