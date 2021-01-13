import connect_mysql as cm

sql = "DROP TABLE IF EXISTS customer_info"

cm.mycursor.execute(sql)
