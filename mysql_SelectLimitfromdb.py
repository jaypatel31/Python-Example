import connect_mysql as cm

def askuser():
    global ip
    ip = input("Enter The Number of Records To Be Displayed: ")
    try:
        ip = int(ip)
    except:
        print("Please Input Number Only")
        askuser()
askuser()

sql = "SELECT * FROM student_info LIMIT %s"
val = (ip,)

cm.mycursor.execute(sql,val)

myresult = cm.mycursor.fetchall()
print()
print()
print("(Id, Name, Class, Mark)")
print()
for x in myresult:
    print(x)
