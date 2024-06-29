#Task 1
pi = 22 / 7
print("Value of pi:", pi)
print("Data type of pi:", type(pi))

#Task 2
#Uncommenting the following lines will cause a SyntaxError because for is a reserved keyword in Python which can't be used to as a variable.
#for = 4
#print(for)

#Task 3
P=int(input("Enter the principle amount:"))
T=int(input("Enter the time period:"))
R=int(input("Enter the rate of interest:"))
simple_interest = (P * T * R) / 100
print("Simple Interest: ", simple_interest)
