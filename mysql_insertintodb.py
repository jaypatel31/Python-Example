import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO student_info (student_name,student_class,student_marks) VALUES ('Jay',12,89.5)"

mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
