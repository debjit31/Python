file1=open("file1.txt","a")
file1.write("hello\nhi\nbye\n")
file1.close()

#import pickle

#file2=open("file2.txt","w")

file1=open("file1.txt","r")
#b=file1.read()
#print(b)

file2=open("file2.txt","w")
file2.write(file1.read())
file1.close()
file2.close()
