name = input('Enter Your Name :')

def greet(user):
    user = user.capitalize()
    greet = "Namaste " + user
    return greet

if name.isalpha()==True:
    finalgreet = greet(name)
    print(finalgreet)
else :
    print("Please Enter The String!!!");
