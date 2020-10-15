length = input("Enter The Length of Array : ")
array = []

# Taking Inout of array
for i in range(int(length)) :
    value = input("Enter The "+ str(i+1) + " Value :")
    if value.isnumeric() == True:
        array.append(int(value))
        flag = "num"
    else :
        value = value.capitalize()
        array.append(value)
        flag = "string"

# For numeric array
if flag == "num" :
    largest = -1
    for num in array :
        if num > largest :
            largest = num
    print("Largest Number is : ", largest);

# for String array
else :
    largest = -1
    for word in array:
        word_len = len(word)
        if word_len > largest :
            largestWord = word
    print("Word : ",largestWord)
