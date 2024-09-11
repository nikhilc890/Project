import mysql.connector
conn=mysql.connector.connect(
    host ='localhost', username='sqluser',password='password',database='hotel'
)
my_cursor=conn.cursor()
yes="insert into room_type(room_id,room_price,room_type) values (%s,%s,%s)"
yes1=(8,200,"nope")
my_cursor.execute(yes,yes1)
conn.commit()
conn.close()
print("Successfully installed")