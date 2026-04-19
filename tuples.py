days=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
#display wed
print(days[2])

#display mon to thurs
print(days[0:4])
#convert friday to fri(convert to list)
days=list(days)
#modify
days[4]='fri'
#convert back to tuple
days=tuple(days)
print(days)