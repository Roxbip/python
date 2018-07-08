str = input("enter string:")

for letter in str:
	if letter == str[-1]:
		str=str[0:-1]
		print(str)
	else:
		print("NOT")
		exit()
print("YES")