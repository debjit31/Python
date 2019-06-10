#picle module
#used to save collections like lists,dictionary to a file


import pickle
a=[1,3,5,7,9]
file1=open("meaw.txt","wb") #binary mode
pickle.dump(a,file1)
file1.close()


file1=open("meaw.txt","rb")
b=pickle.load(file1)
print(b)


if a==b:
    print("identical")
else:
    print("not identical")




