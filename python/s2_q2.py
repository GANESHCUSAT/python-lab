list1=input("enter the number with space: ")
print(type(list1))
list2=list1.split(" ")
list3=[int(i) for i in list2]
print("converted list to integers: ")
print(list3,"\n")

k=int(input("enter the number of positions to be rotated from right: "))

list4=[i for i in list3[-k:]]
list5= [ i for i in list3[0:len(list3)-k]]
list6=list4+list5
print("list after rotating",k,"positions: \n")
print(list6,"\n")

list7=tuple(list3)
print("result after converting to tuple: ")
print(list7,"\n")

list8=set(list7)
list9=list(list8)
print("list after removing duplicate elements: ")
print(list9,"\n")

list10=[(i**2 -i)for i in list9]
print("list after evaluating the functon f(x)=x^2-x: ")
print(list10,"\n")

list11=set(list10+list9)
print("list after merging of two lists: ")
print(list11,"\n")