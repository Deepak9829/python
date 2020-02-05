# Day 5 Assignments 


"""
# Clean the Messy salaries into integers for Data Processing
salaries = ['$876,001', '$543,903', '$2453,896'] 
"""

"""
    We are going to make a "Shopping List" app. 
    Run the script to start using it.
    Put new things into the list one at a time
    Enter the word DONE - in all CAPS - to QUIT the program
    And once i quit, I want the app to show me everything thats on my list.

Hint 1
    Step 1: Make a list to hold onto our items.
    Step 2: Print out instructions on how to use the app

    Step 3: Ask for new items
    Step 4: Add new items to our list
    Step 5: Be able to quit the app with DONE

    Step 6: print out the list
"""
salaries = ['$876,001', '$543,903', '$2453,896'] 
l1=salaries[0]
a=str(l1)
b=a[1:]
c=b.replace(",","")
A=print(int(c))

l2=salaries[1]
a1=str(l2)
b1=a1[1:]
c1=b1.replace(",","")
B=print(int(c1))

l3=salaries[2]
a2=str(l3)
b2=a2[1:]
c2=b2.replace(",","")
C=print(int(c2))
