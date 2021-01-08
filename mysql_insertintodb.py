import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor()
ip = input("Enter The Number of Students: ")
ip = int(ip)
multi = list()
for x in range(ip):
    name = input("Enter The Name of Student: ")
    grd = input("Enter The Class of Student: ")
    mrk = input("Enter The Marks of Student: ")
    tmplist = (name,grd,mrk)
    multi.append(tmplist)

sql = "INSERT INTO student_info (student_name,student_class,student_marks) VALUES (%s, %s, %s)"


mycursor.executemany(sql, multi)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
