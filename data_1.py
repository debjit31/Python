 #Creating a simple database using sqlite3 library module in Python

import sqlite3

conn = sqlite3.connect("database_1.db")#connecting to database
c = conn.cursor()#establishing a cursor

def create_table():#CREATE THE TABE WITH THE COLUMNS
    c.execute('CREATE TABLE IF NOT EXISTS mytable(Name TEXT, Roll TEXT, Marks TEXT)')
    conn.commit()


def insert_values():#ENTER VALUES THROUGH VARIABLE
    name = input("Enter your name = ")
    roll = (int)(input("Enter your roll no:- "))
    marks = (int)(input("Enter percentage of marks obtained = "))
    c.execute('INSERT INTO mytable(Name, Roll, Marks) VALUES(?, ?, ?)',
              (name, roll, marks))
    conn.commit()


def display_values():#DISPLAY CONTENT OF THE DATABASE
    c.execute("SELECT * FROM mytable  ")
   # print("NAME\t\t\tROLL\t\t\tMARKS\n")
    for row in c.fetchall():#FETCHALL SELECTS ALL THE INFORMATION STORED IN THE DATA BASE
##        print(row[0],"\t\t\t",row[1],'\t\t\t',row[2],'\n\n')
        print('Name :- ',row[0])
        print('Roll :- ',row[1])
        print('Marks = ',row[2],'\n')

def del_and_update():
##        c.execute('SELECT * FROM mytable WHERE Marks <90')
##        [print(row) for row in c.fetchall()]

##        c.execute('SELECT * FROM mytable WHERE Marks <90')
##        print(len(c.fetchall()))
##        print(50*'#')
##        c.execute('DELETE FROM mytable WHERE Marks < 90')
##        conn.commit()
##        display_values()
        c.execute('SELECT * FROM mytable')
        #[print(row) for row in c.fetchall()]
        c.execute('UPDATE  mytable SET Name = "Sanjib" WHERE Name = "QQQ"')
        conn.commit()

        c.execute('SELECT * FROM mytable')
        [print(row) for row in c.fetchall()]

        
          
        
create_table()#FUNCTION CALL TO CREATE THE TABLLE
a = input("Do you want to insert to the database ? ")
if a =="yes":
    for i in range(2):#LOOP TO TAKE INPUT AS PER REQUIRED  NUMBER OF TIMES
       insert_values()
#display_values()
del_and_update()
c.close()#CLOSE THE CURSOR
conn.close()#CLOSE CONNECTION WITH DATABASE









