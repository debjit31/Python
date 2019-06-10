#dictionary contains elements in the form of key value pairs
#it is usable like list

dept={"HR":7,"ADMIN":6,"MKTG":4}

print(dept)

keys=dept.keys()
list1=(list)(keys)
print(keys)
print(list1[1])

values=dept.values()
list1=(list)(values)
print(list1)


items=dept.items()
print(items)

print(dept["HR"])

dept["HR"]=20 #modifying a dictionary
print(dept)

del dept["HR"]
print(dept)

dept.update({"HR":9,"ACCOUNTS":10})
print(dept)

print(dept.pop("HR"))
print(dept)
