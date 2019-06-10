#tuple is also a collectiom of elements.unlike list, it cannot be immutable
#or it cannot be modified

tuple1=(1,2,5,'c','r')
print(tuple1)

for i in range(len(tuple1)):
    print(tuple1[i],end=' ')

for t in tuple1:
    print(t,end=' ')

#tuple1[2]=7#not supported

list1=(list)(tuple1)
print(tuple1)

list1[1]=8
tuple1=(tuple)(list1)
print(tuple1)



#to create a list with user input
list2=[]
n=(int)(input("Enter the number of elements = "))
for i in range(n):
    num=(int)(input("Enter a number = "))
    list2.append(num)


print(list2)
