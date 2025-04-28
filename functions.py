#basic functions
def hi(name):
    return f"hello,{name}!"
print(hi("students"))

#default parameters
def a(x,y=1):
    return x*y

print(a(5))
print(a(5,3))

#function with var args
def summ(*args):
    return sum(args)
print(summ(1,2,3))
print(summ(10,10,30,40))

#functions with keyword args
def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
info(name='usha',age=50,city='hybd')

#lambda function
sq=lambda a:a*a
print(sq(4))
add=lambda x,y:x+y
print(add(5,9))

#programs to return multiple values
#1.min,max,avg by passing 1,2,3,4,5 to a function
def fun(*args):
    return f"min_valu:{min(args)},max_valu:{max(args)},avg:{sum(args)/len(args)}"
print(fun(1,2,3,4,5))

 #recursive functions
# 1.direct recursive
# eg:factorial
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5)) 

# 2.indirect recursive
# eg: even or odd
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
print(is_even(4))
print(is_odd(7))


#eg2
'''create a program to determine if a string is a palindrome by recursiely comparing characters 
from start to end by base case functionand call if the pointer meets its palindrome constraints'''
def is_pal (string):
    if len(string)<=1:
        return True
    return check_pal(string,0,len(string)-1)
def check_pal(string,start,end):
    if start>=end:
        return True
    if string[start]!=string[end]:
        return False
    return is_pal(string[start+1:end])    
print(is_pal("racar"))
print(is_pal("hello"))
print(is_pal("level"))

