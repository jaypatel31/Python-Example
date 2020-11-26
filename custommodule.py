import datetime
z = datetime.datetime.now()
x = z.strftime("%H")
x = int(x)
def greet(name):
    if x > 0 and x <= 11:
        print("Good Morning",name)
    elif x >= 12 and x <= 16:
        print("Good Afternoon",name)
    elif x >=17 and x <= 21:
        print("Good Evening",name)
    else:
        print("Good Night",name)

    print("Hope Doing Well.")
