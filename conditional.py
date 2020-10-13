#EVEN odd CHECKER
print('*************EVEN - ODD CHECKER*****************')

#Input Fetch
number = input('Enter The Number :')


#Conditions
try :
    number = int(number)
    if number%2 == 0 :
        print(str(number) +' is Even.')
    elif number%2 != 0 :
        print(str(number) + ' is Odd.')
except :
    print(number + ' is Not a Number.')
