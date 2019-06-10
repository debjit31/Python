#SQL Structured Query Language
#DDl-Data Definition Language
#Create, Alter, Drop

#DML
    #DATA MANIPULATION LANGUAGE
    #INSERT, UPDATE,DELETE

import sqlite3

conn = sqlite3.connect("test.db")#to connect to the database
conn.execute('''Create table if not exists Employee(EID INTEGER PRIMARY KEY, ENAME TEXT NOT NULL,ESAL INTEGER NOT NULL)''')


###---------------------------To add data to the table---------------------
##eid = (int)(input("Enter employee id :- "))
##ename = input("Enter employee name = ")
##esal = (int)(input("Enter employee salary = "))
##row = [(eid,ename,esal)]
##conn.executemany("insert into employee(EID,ENAME,ESAL) values(?,?,?)",row)
##conn.commit()
##print("No of rows added ", conn.total_changes)
##

#----------to view the table data--------------
#rows = conn.execute("select * from employee order by EID desc")
#rows = conn.execute("select * from employee where ename like 'a% '")
#rows = conn.execute("select * from employee where esal>150")
rows = conn.execute("select * from employee")
for row in rows:
    print("ID",row[0])
    print("Name",row[1])
    print("Salary",row[2],'\n\n')
#---------------to delete data from a table------------------
    conn.execute("delete from employee where eid  = 1")
    conn.commit()
    print("No. of rows deleted ", conn.total_changes)

#------------to update data in a table-------------
conn.execute("update employee set ename = 'ppp' where eid = 2")
conn.commit()
print("No. of rows updated ",conn.total_changes)

rows = conn.execute("select * from employee")
for row in rows:
    print("ID",row[0])
    print("Name",row[1])
    print("Salary",row[2],'\n\n')
