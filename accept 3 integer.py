# this is a python program to accept 3 integers in the same line
var1,var2,var3=[int(a)for a in input("enter three numbers : ").split()]
print("sum = ",var1+var2+var3)
var1,var2,var3=[int(a)for a in input("enter three numbers : ").split(',')] #give input in commas i.e 10,20,30
print("sum = ",var1+var2+var3)
#accept group of string from keyboard separated by commas
str=[a for a in input('Enter string : ').split(',')]
print("string is ",str)