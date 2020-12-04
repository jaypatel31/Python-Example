import os
# For Creating And Appending 
f = open("Demo.txt","a")
f.write("\nHey Some Text......")
f.close()
# For Reading
f = open("Demo.txt","r")
for line in f:
    line = line.strip()
    print(line)
f.close()
# Deleteing File 
os.remove("Demo.txt")