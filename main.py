name = "Jack"
age = 15
income = str(256.78)

# print(isinstance(name,str))
# print(isinstance(age,str))
# print(isinstance(income,str))

# c1=True
# c2=False

# print("Conditions")
# print(c1 and c2)
# print(c1 or c2)
# print(not c1)
# print(not c2)

#Ternary operator
# def IsAdult(age):
#     return True if age>18 else False

# print(IsAdult(age))

#Multi line string
# print("""This is 
      
#       a multi 

#       line String

# thank you
# """)

#print("\"Muhammad giani\" is my name  ")

#indexing a string
#print(name[-4])

#using range
# print(name[-4:-1])

# #any, all statements
# check = any([True,False])
# print(check)

# check2 = all([True,False])
# print(check2)

# #complex function

# num1=2+3j
# num2=complex(2,3)

# print(num1)

# print(num2.real,num2.imag)

# #Enums

# from enum import Enum

# class State(Enum):
#     INACTIVE=0
#     ACTIVE=1

# print(len(State))

#Lists

#cars = ["Honda", 25, True, 97.8]
# print("Roger" in cars)
# cars.extend(["toyota", 53])
# cars.remove("Honda")
# cars[2:2]=["Jack",30,"corolla"]
# print(cars)

# ages=[25,7,90,33,21]
# ages.sort()
# print(ages)

# names=["Jack", "David", "bob", "lucy", "karen"]
# print(sorted(names,key=str.lower))
# print(names)

#Tuples
year = ("2025", "2024", "2023")

newYear= year + ("2026","2027")
print(year)
print(newYear)
print(sorted(year))

# python data types
complex
dict
list
tuple
set
range
bool