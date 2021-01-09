import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM student_info"
mycursor.execute(sql)

print()
print()
myresult = mycursor.fetchall()
print("(Id, Name, Class, Mark)")
print()
for x in myresult:
  print(x)
