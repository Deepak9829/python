#pattern print
for i in range(11,1,-1):
    for j in range(0,i): 
        print("*",end="")
    print(" ")
    
    
#vowel and consonant    
ch = input("enter a character:")
if(ch=='A' or ch=='a' or ch=='E' or ch=='I' or ch=='i' or ch=='e' or ch=='O' or ch=='o' or ch=='U' or ch=='u' ):
    print(ch, "is a vowel")
else:
    print(ch,"is a consonant")
    
#reverse number
    
n=int(input("enter a number"))
rev=0
while(n>0):
    rem=n%10;
    rev=rev*10+rem;
    n=n//10;
print("reverse",rev)
    
    
#lower and upper range
lower=int(input("enter the lower range"))
upper=int(input("enter the upper range"))
for i in range(lower,upper+1):
   if(i%7==0 and i%5==0):
     print(i)
     
     
#pattern    
for i in range(1,11):
     print("*")
     
for i in range(1,11):
    for j in range(0,i): 
        print("*",end="")
    print(" ")
    
#pattern
for i in range(11,1,-1):
    for j in range(0,i): 
        print("*",end="")
    print(" ")
for k in range(1,11):
    for l in range(0,k):
        print("*",end="")
    print(" ")    
    
#pattern    
for row in range(0,7):
    for col in range(0,5):
        if ((col==0 or col==4) and (row!=0) or (row==0 or row==3) and (col>0 and col<4)):
            
            print("*",end="")
    
        else:
             print(end=" ")
            
    print()            

#pattern
for k in range(1,11):
    for l in range(0,k):
        print("*",end="")
    print(" ")    
for i in range(11,1,-1):
    for j in range(0,i): 
        print("*",end="")
    print(" ")
