a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
outl=[]

num = int(input("pick a number:"))
for item in a:
	if item < num:
		outl.append(item)

print (outl)
