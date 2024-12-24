file = open("Codingal.txt","r")
print("file in reading mode")
print(file.read())
file.close()

file2 = open("Codingal.txt","w")
file2.write("file in write mode")
file2.write("hi i am Derion and i am 13 yaer old")
file2.close()

file3 = open("Codingal.txt","a")
file3.write("file in append mode")
file3.write("hi i am Derion and i am 14 yaer old")
file3.close()