Name = input("Enter First Name= ")
Surname = input("Enter Surname= ")
c= float(input("Enter Math grade= "))
d= float(input("Enter English grade= "))
e= float(input("Enter Biology grade= "))

s= (c + d + e)/3
print(s)
print(Name +  Surname)

if s>=17 :
    print("Very Good")
    
if 15<s<17 :  
    print("Good")
    
if 12<=s<17 :
    print("Acceptable")
    
if s<12 :
    print("Failed")
if s == 15:
    print("Good")