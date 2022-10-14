#!/usr/bin/env python
# coding: utf-8

# # Rollercoaster Ticket Criteria Cheker

# In[ ]:


print("Welcome to the Rollercoaster!")
height = int(input("What is your Height in cm? "))

if height>=120:
    print("You can ride the rollercoaster!!")
    age = int(input("What is your age? "))
    if age<12:
        print("Please pay $5. ")
    elif age>=12 and age<=18:
        print("Please pay $7. ")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.")

