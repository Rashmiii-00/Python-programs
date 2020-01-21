option=''
while True:
    print("Enter 1 for pallindrome \n2 for factorial \n3 for Exit")
    op = int(input("Enter Your choice:"))
    #while op<3:
    if op==1:
        s2=input("Enter any String or integer ")
        print()
        n = len(s2)
        #s1=s1.split()
        s1 = list(s2)
        for i in range(int(n/2)+1):        
            if s1[i]!=s1[n-1-i]:
                break;
        if i is(int(n/2)):
        #if i <int(n/2):
            print("Entered String is  a pallindrome")
            print()
        else:
            print("Entered String is not a pallindrome")
            print()
    elif op == 2:
        print()
        n1=int(input("Enter any number:"))
        fac=1
        i=1
        while i<=n1:
           fac = fac*i
           i = i+1
        print()
        print("Factorial of ", n1 ," is " ,fac)
    if op==3 :
        break;
                                    
