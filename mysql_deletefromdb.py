import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor()

sql = "DELETE FROM student_info WHERE student_name = %s"

value = ("Ketul",)
mycursor.execute(sql, value)

mydb.commit()

print(mycursor.rowcount,"Record(s) Deleted")
