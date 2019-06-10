#--------------------------------------filter function----------------#
list1=[2,3,5,7,9,6]
f=lambda x:x%2==1
list2=(list)(filter(f,list1))
print(list2)


#-----------map function----------------
list1=[2,3,4,5,6]
list2=(list)(map(lambda x:x*x,list1))
print(list2)


#----------------------list comprehension---------
list1=[2,3,4,5,6,7,9]
list2=[x*x for x in list1]
print(list2)

list2=[x for x in list1 if x%2==1]
print(list2)
