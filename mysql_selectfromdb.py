import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor()

def askuser():
    global ip
    ip = input("Enter The Name of the Student: ")

askuser()

sql = "SELECT * FROM student_info WHERE student_name = %s"
val = (ip,)
mycursor.execute(sql,val)

print()
print()
myresult = mycursor.fetchall()
if len(myresult) == 0:
    print("No Such Record Found!!")
else:
    print("(Id, Name, Class, Mark)")
    print()
    for x in myresult:
      print(x)
