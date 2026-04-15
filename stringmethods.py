text="Software DEVELOPER"
# capitalize
text1=text.capitalize()
print(text1)

# casefold
text2=text.casefold()
print(text2)

# count
text3=text.count('e')
print(text3)

# replace
text4=text.replace('DEVELOPER','Programmer')
print(text4)

#endswith and startswith
text5=text.endswith('r')
print(text5)

# lower
text6=text.lower()
print(text6)

#upper
text7=text.upper()
print(text7)

# strip
text="                Software DEVELOPER              "
print(len(text))
print(text)
text=text.strip()
print(len(text))
print(text)

# split
text8=text.split()
print(text8)
text8=text.split('ware')
print(text8)

# quiz 
text="    jUnIoR develOper   "
print(len(text))
print(text)
text=text.strip()
text=text.capitalize()
print(text)