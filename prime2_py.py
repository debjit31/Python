#to print all prime numbers between lower limit and upper limit
low=(int)(input("Enter the lower limit = "))
up=(int)(input("Enter the upper limit = "))
for i in range(low,up+1):
    flag=0
    for j in range(1,i+1):
        if i%j==0:
            flag+=1
    if flag==2:
        print(i,end=' ')
    
