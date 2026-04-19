my_list=['mike','mary','paul',5,6,7,True,False]
#remove- removes items with the specified value.
my_list.remove(5)
print(my_list)

#pop- removes the element at the specified position
my_list.pop(2)
print(my_list)

#insert- adds an element to the specified position
my_list.insert(3,'frank')
print(my_list)

#append- adds an element at the end of the list
my_list.append('alice')
print(my_list)

# qiuz
lst=[10,20,30,['mary','kim',[1000,2000,3000]],40,50,60]
#1.using methods add 70 in the list
lst.append(70)
print(lst)
#2.add jane between mary and kim
lst[3].insert(1,'jane')
print(lst)

#3. add 1500 between 1000 and 2000
lst[3][3].insert(1,'1500')
print(lst)
#4.delete 2000
lst[3][3].pop(2)
print(lst)
#count-used to count the number of elements in a list with the specified value
lst2=['mike','mary','paul',5,6,7,True,False]
print(lst2.count('mike'))
#sort-sorts the list
lst3=['mike','mary','paul']
lst3.sort()
print(lst3)

#extend-add the elements of a list to the end of the current list
lst3=['mike','mary','paul']
my_list=['mike','mary','paul',5,6,7,True,False]
lst3.extend(my_list)
print(lst3)

#clear
print(lst3.clear())

#in operator check for membership
print('paul' in lst3)
