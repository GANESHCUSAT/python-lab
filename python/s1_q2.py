import math
#function to recieve the values from the user
def sides_input():
  side1= int(input("enter the value of side1: ")) 
  side2= int(input("enter the value of side2: "))
  side3= int(input("enter the value of side3: "))
  return side1,side2,side3

#function to calculate the area of the triangle
def area(s1,s2,s3):
  s=(s1+s2+s3)/2  #semi perimeter
  A=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))  #area
  return A

#function to find the contribution of each triangle to the total area
def percentage(a1,a2):
  total=a1+a2
  triangle1 = round((a1/total)*100,2) #triangle1 percentage
  triangle2 = round((a2/total)*100,2) #triangle2 percentage

  #output
  print("contribution of triangle1 to total area in percentage =",triangle1)
  print("contribution of triangle2 to total area in percentage =",triangle2)
  

print("traingle1")
a1,b1,c1 = sides_input()  
area1 = area(a1,b1,c1)
print("area of triangle1 =",area1)

print("triangle2")
a2,b2,c2 = sides_input()
area2 = area(a2,b2,c2)
print("artea of traingle2 =",area2)

percentage(area1,area2) #calling function to find the percentage of contribution 
