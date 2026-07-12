#1.Add two numbers
def add(a,b):
    return a+b
#2.Largest of two numbers
def largest(a,b):
   if a>b:
       return
   else:
       return b
#Check whether a number is even
def even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "odd"
#factorial of num
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
#Reverse a string
def reverse_string(text):
    return text[::-1]
print ("Addition:",add(10,20))
print("largest:",largest(15,8))
print("even_or_odd:",even_or_odd(50))
print("factorial:",factorial(5))
print("reverse_string:",reverse_string("python"))