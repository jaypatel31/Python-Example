import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE student_info (student_id INT AUTO_INCREMENT PRIMARY KEY, student_name VARCHAR(25), student_class INT, student_marks FLOAT )")

mycursor.execute("ALTER TABLE student_info CHANGE student_name student_name VARCHAR(25) NOT NULL, CHANGE student_class student_class INT NOT NULL, CHANGE student_marks student_marks FLOAT NOT NULL")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)
