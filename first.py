def prime(num):
    div=2
    f=1
    fact=1
    while div < num:
        if num % div == 0:
            print("composite !")
            return 
        div = div + 1
    print("prime !")
    print ("Factorial : ")
    while (f <= num):
        fact= fact * f
        f = f + 1   
    print (fact) 

    
for i in range (1, 101): 
   print(i)
   prime(i)
   
   
