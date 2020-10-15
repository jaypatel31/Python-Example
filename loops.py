numbers = [50,10,30,70,100,20,2]

n = len(numbers)

print("Numbers : ");
def loop(array):
    for num1 in array:
        print(num1, end=", ")
loop(numbers)

i=0
while i<n :
    j=i+1
    while j<n :
        if numbers[i] >numbers[j]:
            ref = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = ref
        j = j+1
    i=i+1

print("\n After Sorting : ")
loop(numbers)
