
num = int(input("pick a number:"))

x = range(1,num)
a=[]

for item in x:
	if num%item == 0:
		a.append(item)
		
print(a)

