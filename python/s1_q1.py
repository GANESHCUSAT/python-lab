number = int(input("enter a 4 digit number: "))

num = number #storing original number to a temporary number 
t=0
while num>0:
  r = num%10
  t=t+1  #finding number of digits
  num = (num-r)/10

if t==4:
  i=4
  reverse=0
  sum=0
  even,odd=1,1

  while i>0:
    r = number%10 #extracting the last digt

    if i%2==0:  #finding even and odd places
      even = even*r  #product of even place digits
    else:
      odd = odd*r #product of odd place digits 

    i=i-1
    number = (number-r)/10  
    
    sum = sum + r #sum of the digits
    reverse = (reverse*10) + r #reverse of the number

  #finding the difference btw the product odd and even place digits
  diff = odd-even
  print("sum of the digits=",sum)
  print("reverse of the number=",reverse)
  print("difference between the product of the odd and even place digits=",diff) 

else:
  print("enter a 4 digit number!!")  
