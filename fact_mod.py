import sys
sys.path.append("F:/")#path of user defined module
import mod_test
num = (int)(input("Enter a number = "))
f = mod_test.fact(num)
print("The factorial is ",f)
