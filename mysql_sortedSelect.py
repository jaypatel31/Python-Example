import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pydb"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM student_info ORDER BY student_marks DESC"

mycursor.execute(sql)
print()
print("Ranking of Student ")
print()

print("(ID , Name, CLass, Marks)")
print()
print()
ans = mycursor.fetchall()

for x in ans:
    print(x)
