#function - checking whether a given number is happy or not
def check_happy(n):
    i=0
    while i<100:
        sum=0
        if n==1:
            print("given number is happy")
            break
        else:
            while n>0:
                r=n%10
                sum = sum + r**2
                n=n//10                
            if sum==1:
                print("given number is happy")
                i=100 
                break
            else:
                n=sum
                sum=0
                i=i+1
        i=i+1
    if sum!=1:                   
        print("given number is not happy")
      
#function - to find the happy numbers between a given range      
def happy_terms(n,m):
    happy=0
    for i in range(n,m+1):
        sum=0
        j=0
        q=i
        while j<100:
            while i>0:
                r=i%10
                sum = sum + r**2
                i=i//10                
            if sum==1:
                print(q)
                happy=happy+1
                j=99
            else:
                i=sum
                sum=0
            j=j+1 
    if happy==0:
      print("there is no happy numbers in the given range")   

#function - to find happy numbers upto n terms                      
def happy_upto_n_terms(p):
    e=0
    q=1
    while q>0 and e<p:
        sum=0
        j=0
        i=q
        while j<100:
            while i>0:           
                r=i%10
                sum = sum + r**2
                i=i//10                
            if sum==1:
                print(q)
                e=e+1
                break
            else:
                i=sum
                sum=0
            j=j+1                   
        q=q+1

#read the number to find happy or not                                       
print("to find given number is happy or not\n")
num=int(input("enter the number: "))
check_happy(num) #calling function to check happy or not

#read two numbers to find happy numbers in between them 
print("\nto find the happy terms between range of two numbers\n")
lower_limit=int(input("enter lower limit: "))
upper_limit=int(input("enter upper limit : "))
#calling the function to find the number between the range
happy_terms(lower_limit,upper_limit)
      
#read the number of terms of happy numbers to be printed      
print("\nto find n terms of happy numbers\n")       
limit=int(input("enter the limit: "))
#calling the function to find n happy numbers
happy_upto_n_terms(limit)