print("Enter any two numbers")
n1,n2=int(input()),int(input())
print(f"Numbers are : {n1},{n2}")
n3 = n1
n1 = n2
n2 = n3
print(f"After Swapping: {n1},{n2}")
if n1>0:
    print("First number is positive")
elif n1==0:
    print("First number is zero")
else:
    print("First number is negative")
    
