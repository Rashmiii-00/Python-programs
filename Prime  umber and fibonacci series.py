option = ''
while True:
        op = int(input("1:prime number series\n2:Fibonacci series\n3:Quit\n"))
        
        if op == 1:
            n = int(input("Enter the range\n"))
            print("prime number series:\n")
            print("2 ")
            for x in range(3,n+1):
                for i in range(2,x):
                    if x%i == 0:
                        break;
                else:
                    print(f"{x} ")
        elif op == 2:
            n = int(input("Enter the range\n"))
            print("Fibonacci series:\n")
            print("1\n2")
            f=1
            s=2
            sum = 0
            for i in range(2,n):
                sum = f+s
                print(sum)
                f=s
                s=sum
        if op==3:
            break;
        
        
        
        
        
        
        
    