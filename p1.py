# This is my first python program
print("Hello, World!")

print(5+3)

print("5+3")
#representing print of different data types
print("Store:", "Pune", "| Orders today: ",18) #represents print of different data types

a = 5
b = 3
sum = a + b
print("Sum:", sum)

name = "bhima"

print(type(name))
print(type(a))

#float, bool

c = 5.0
d = True
print(type(c))
print(type(d))

#formating output
print("Sum of {} and {} is {}".format(a, b, sum))
print(f"Sum of {a} and {b} is {sum}")

#print(name + 5)

# containers
#list, tuple, set, dictionary
emp_list = [] #empty list
print(type(emp_list))
emp_list = ["bhima", "pune", 18, 5.0, True]
print(emp_list)

