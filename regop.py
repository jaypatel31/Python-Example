import re

mailid = input("Enter Your Mail Id - ")

verify = re.findall("^.+@[a-z\.]+.[a-z]{2,4}$",mailid)

if len(verify)==0:
    print("Not Valid Email Id.")
else:
    print("Valid Email :)")

