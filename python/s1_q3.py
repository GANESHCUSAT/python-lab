def gross_salary(bp,da,hra,ma): #caluculating  gross salary
    gs = bp+da+hra+ma
    return gs

def deduction(pt,pf,it):   #calculating deduction
    d = pt+pf+it
    return d
  
def net_salary(gs,d):  #calculating net salary
    ns = gs-d
    return ns


#function for finding ma,pt,da,hra,pf,it
def components(bp): 
 #when basic pay is less than 10000 
    if bp<10000: 
        ma  = 500
        pt  = 20
        da  = bp*(5/100)
        hra = bp*(2.5/100)
        pf  = bp*(8/100)
        it  = 0
        return ma,pt,da,hra,pf,it

 #when basic pay is less than  30000 and greater than 10000      
    elif bp>10000 and bp<30000:
        ma  = 2500
        pt  = 60
        da  = bp*(7.5/100)
        hra = bp*(5/100)
        pf  = bp*(8/100)
        it  = 0
        return ma,pt,da,hra,pf,it

 #when basic pay is less than  50000 and greater than 30000      
    elif bp>30000 and bp<50000:
        ma  = 5000
        pt  = 60
        da  = bp*(11/100)
        hra = bp*(7.5/100)
        pf  = bp*(11/100)
        it  = bp*(11/100)
        return ma,pt,da,hra,pf,it
        
 #when basic pay is greater than 50000       
    else:
        ma  = 7000
        pt  = 80
        da  = bp*(25/100)
        hra = bp*(11/100)
        pf  = bp*(12/100)
        it  = bp*(20/100)
        return ma,pt,da,hra,pf,it

#read employee's name 
en = input("enter employee's name: ")  

#read the code of the employee
code = int(input("enter the code: ")) 

#read the basic pay of the employee
basic_pay = int(input("enter the basic pay: ")) 

bp = basic_pay

#calling function for computing the components
ma,pt,da,hra,pf,it = components(bp) 

#calling function gross salary
gs = gross_salary(bp,da,hra,ma)

#calling function deduction
d  = deduction(pt,pf,it)

#calling the function net_salary
ns = net_salary(gs,d)

#PAYMENT SLIP
print("\n\n      PAYMENT SLIP\n")
print("employee's name :",en)
print("code            :",code)
print("basic pay       :",bp)
print("DA              :",da)
print("HRA             :",hra)
print("MA              :",ma)
print("PT              :",pt) 
print("PF              :",pf)
print("IT              :", it)
print("gross salary    :",gs)
print("deduction       :",d)
print("net salary      :",ns)