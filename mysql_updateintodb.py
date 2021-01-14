import connect_mysql as cm

update_std_name = "Amit"
update_std_mark = 99
sql = "UPDATE student_info SET student_marks = %s WHERE student_name = %s"

val = (update_std_mark,update_std_name,)

cm.mycursor.execute(sql,val)

cm.mydb.commit()

sql2 = "SELECT student_name, student_marks FROM student_info WHERE student_name = %s"
val2 = (update_std_name,)
cm.mycursor.execute(sql2,val2)

myresult = cm.mycursor.fetchall()
print()
print("Updated Record")
print()
print()
for x in myresult:
    print(x)
