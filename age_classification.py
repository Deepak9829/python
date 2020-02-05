'''Take the age as input from the user and print whether he is a infant, Child , 
Adult,  Senior Citizen
0 - 1 is Infant
> 1 and < than 18 is Child 
> 18 and < 60 is Adult
> 60 is Senior Citizen 
'''
Age=int(input("enter your age: "))
if(Age<=1 and Age>0):
    print("infant")
elif(Age<=18 and Age>1):
    print("child")
elif(Age<60 and Age>18):
    print("Adult")
elif(Age>=60):
    print("senior citizen")
else:
    print("alian")
