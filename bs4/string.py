

print("*************Total Vowel In the String*************")

string = input("Enter The String : ")

smallconvert = string.lower()
vowel = 0
indexs = []

for letter in smallconvert :
    if letter == 'a' or letter == "e" or letter == "i" or letter == "o" or letter == "u" :
        vowel = vowel+1
        indexs.append(smallconvert.find(letter))
        smallconvert = smallconvert.replace(letter,'X',1)


print("Total Vowel In The String" , str(vowel))
print("At Index :" , indexs)
