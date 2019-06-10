# lists in Python

list1=[1,2,3,'a','c',4.5]
##print(list1)
##
#for i in range(len(list1)):
#   print(list1[i],end=' ')

##for c in list1:
##        print(c,end=' ')


list1[3]='z' 
##print(list1)


##list1.insert(3,'a')
##print(list1)
##
##del list1[4]
##print(list1)

list2=[1,34,-100,0.45,4.67,23,11,22]
#print(list2)
##print("Sum of the elements in the list = ",sum(list2))
##print("Maximum element in list = ",max(list2))
##print("Minimum element in list = ",min(list2))

##list2.sort()
##print("List in ascending order :- ",list2)

##list2.sort(reverse=True)
##print(list2)

##list2.append(90)
##print(list2)








                    ##---------------------------TUPLE-----------------------------------##
tuple=(1,2,3,'a',4.67,'z')
print(tuple)

##for i in range(len(tuple)):
##    print(tuple[i],end=' ')
##print()
##
##for c in tuple:
##    print(c,end=' ')
##print()

##tuple[2]=67
##print(tuple)
##
##list=(list)(tuple)
##print(list)
##
##list[2]=67
##print(list)
##
##list.append(34)
##print(list)
##
##tuple=(list)
##print(tuple)


list1=[]
n=(int)(input("Enter the number of elements = "))
for i in range(n):
    num=(int)(input("Enter a number = "))
    list1.append(num)
print(list1)
