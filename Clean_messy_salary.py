''' Day-2 Assignment
 Clean the Messy salary into integers for Data Processing
 salary = '$876,001' 
 Hint:
     Remove the $
     Remove the ,
     Convert into integer
'''
salary='$876,001'
A=salary[1:]
B=A.replace(",","")
int(B)



