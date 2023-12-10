#!/usr/bin/env python
# coding: utf-8

# ### DEFINING A CLASS

# In[1]:


class Point3D():
    def __init__(s, x,y,z):
        s.x = x
        s.y = y
        s.z = z
        
        
        


# In[2]:


my_point = Point3D(1,2,3)


# In[3]:


print(my_point.y)


# ### RECTANGLE

# In[4]:


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of Rectangle
my_rectangle = Rectangle(length=4, width=3)

# Compute area and perimeter
area_result = my_rectangle.area()
perimeter_result = my_rectangle.perimeter()

# Print the results
print("Area:", area_result)
print("Perimeter:", perimeter_result)


# ### CIRCLE

# In[5]:


import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def isInside(self, x, y):
        distance = math.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)
        return distance <= self.radius

# Create an instance of Circle
my_circle = Circle(center_x=0, center_y=0, radius=5)

# Compute area and perimeter
area_result = my_circle.area()
perimeter_result = my_circle.perimeter()

# Test if a point is inside the circle
point_x = 3
point_y = 4
is_inside = my_circle.isInside(point_x, point_y)

# Print the results
print("Area:", area_result)
print("Perimeter:", perimeter_result)
print(f"Is point ({point_x}, {point_y}) inside the circle? {is_inside}")


# ### BANK ACCOUNT

# In[6]:


class Bank:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal amount exceeds balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

# Example usage
my_account = Bank(balance=1000)

my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(800)
my_account.deposit(1000)


# In[ ]:




