# Convert a float to an integer with an inbuilt function in Python
# temp = 56.8926 to 57

temp=56.8926
print(round(temp))
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.89 

temp1=56.8926
print(round(temp1,2))
# Convert the float below to give the results as follows
# temp = 56.8926 to 56.893 

temp2 = 56.8926
print(round(temp2,3))
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 

temp3=56.8926


# Convert to string
s = str(temp3)

# Get digits after decimal
fraction = s.split('.')[1]

# Reformat
result = float(fraction[0] + '.' + fraction[1:])

print(result)  # 8.926
