ip = ""
def takingInput():
    global ip
    ip = input("Enter The Number - ")
    checkingInput()

print(ip)
def checkingInput():
    global ip
    try:
        ip = int(ip)
        st = "The {} is right Input."
        print(st.format(ip))

    except:
        print("Something Went Wrong, Please Try Again ")
        print()
        takingInput()
takingInput()
