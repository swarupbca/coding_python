def fibo(n):

    a=0
    b=1

    print(a)
    print(b)


    for i in range(n-2):

        
        sum=a+b
        print(sum)
        a=b
        b=sum
        

fibo(10)

