ll={'Codingal':3,'is':2,'for':2,'Coding':1}
print(str(ll))
x=int(input("Enter the number to check the frequency(3,2,1):"))
y=0
for k in ll:
    if ll[k]==x:
        y=y+1

print("Frequency of",x,":",y)
