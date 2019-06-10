file1=open("sample.txt","w")
file1.write("hello\nhi\nbye\n")
file1.close()




file1=open("sample.txt","r")
#print(file1.read())

#print(file1.readline())




file1.seek(7)#will move the file pointer to the index 6 and then do the task
print(file1.read())
#print(file1.readline())
print(file1.tell()) #returns the position


























