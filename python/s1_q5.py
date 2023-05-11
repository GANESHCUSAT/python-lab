#function to print all possible substrings
def substrings(s1):
  lens=len(s1)
  list1 = []
  print("\nAll possible substrings are:")
  for i in range(lens+1):
    for j in range(i,lens+1): 
      s=s1[i:j] #slicing
      print(s)

#sunction to print all possible substrings with specified length
def substring_of_length_k(s2,k):
  lens=len(s2)
  list1=[]
  for i in range(lens+1):
    for j in range(i,lens+1): 
      s=s2[i:j] #slicing
      list1.append(s) #adding required elements to list1
  print("\nThe possible substrings with length",k,"is: ")  
  for r in list1:
    if len(r)==k:
      print(r)

#function to print all possible substrings with specified length and no of distinct characters 
def subs_with_diff_char_and_len(s3,size,n):
  lens=len(s3)
  print("The substrings with length",size,"and",n,"distinct characters are:")
  for i in range(lens+1):
    for j in range(i,lens+1): 
      s=s3[i:j] #slicing
      if len(s)==size: #checking the specified size
        list1 = set(s)
        if (len(list1)<=size) and len(list1)==n:
          print(s)

#function to print all possible substrings with max length and n no of distinct characters
def substrings_with_dist_char_and_max_length(s4,n):
  lens=len(s4)
  print("\nThe substrings with max length with",n,"distinct characters are:")
  list1=[]
  for i in range(lens+1):
    for j in range(i,lens+1): 
      s=s4[i:j] #slicing
      dist = set(s) #making a dist set 
      if len(dist) == n:
        list1.append(s) #required elements to list1
  for i in list1:      
    l = max(list1,key = len)
    print(l)
    
  

#function to print all the paliandrome sub-strings
def palindrome_subs(s5):
  i,j=0,0
  l=len(s5)
  for i in range(0,l+1):
    for j in range(i+1,l+1):
      s1=s5[i:j]
      s2=s1[::-1] #to reverse the substring
      if(s2==s1):
        print(s2)

  
# to print all possible sub-strings
print("to print all possible sub-strings")
string1=input("enter the word: ")
#calling function to print all possible substrings
substrings(string1)


#to print all possible substrings with specified length
print("to print all possible substrings with specified length\n")
string2=input("enter the word: ")
k=int(input("enter the length of the substring: "))
#calling function to print all possible substrings with specified length
substring_of_length_k(string2,k)  

#to print all possible substrings with length and no of distinct characters
print("to print all possible substrings with length and n no: of distinct characters")
string3=input("enter the word: ")
k=int(input("enter the Enter the length of the substring: "))
n=int(input("Enter the number of distinct characters in the substring: "))
#calling function to print all possible substrings with length and no of distinct characters
subs_with_diff_char_and_len(string3,k,n)  

#to print all sub-strings with max-length with specified no of distinct characters
print("to print all sub-strings with max-length with specified no of distinct characters")
string4=input("enter the word: ")
n=int(input("enter the number of distinct characters: "))
#callin function to print all sub-strings with max-length with specified no of distinct characters
substrings_with_dist_char_and_max_length(string4,n)

#to print all the paliandrome sub-strings
print("to find the palindrome substrings\n")
string5=input("enter the word: ")
#calling function to print all the paliandrome sub-strings
palindrome_subs(string5)
