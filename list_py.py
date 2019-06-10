#list

#it is a collection of elements.it is mutable in nature which means it can be
# changed or modified

list1=[1,2,3,'a','c',3.2]
print(list1)

for i in range(len(list1)):
    print(list1[i],end=' ')

print()
for c in list1:
    print(c,end=' ')

#----------------modify a list
list1[2]=99
print(list1)

#----------------inserting an element in  a list
list1.insert(4,70)
print(list1)

#--------deleting an element from a list
del list1[2] #deletes element from 2nd index from the list
print(list1)

#-------appending element to a list
list1.append(23)# appends an element at the end of the list
print(list1)

list2=[1,2,3,8,55,9]
print("Sum of the elements is = ",sum(list2))
print("Maximum element is = ",max(list2))
print("Minimum element is = ",min(list2))

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)







