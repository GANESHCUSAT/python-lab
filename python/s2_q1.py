#question1

list1=[]
mnths=int(input("enter the number of months: "))
m1,m2=2,2
total,i=0,0
list1=[m1,m2]

if(mnths==1 or mnths==2):
  print("number of rabits at ",mnths,"months is",m1)
else:
  while(i<mnths-2):
    total=m1+m2
    m1=m2
    m2=total
    list1.append(total)
    i+=1
  print("number of rabits at ",mnths,"months is",total)
