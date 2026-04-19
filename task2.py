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
temp2=round(temp2,3)
print(temp2)
# Convert the float below to give the results as follows
# temp=56.8926 to 8.926 

temp=56.8926
temp=str(temp)
temp=temp[3:]
temp=temp[0]+'.'+temp[1:]
temp=float(temp)
print(temp)