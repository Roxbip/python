import random
a=random.randint(1,9)
count = 0
print("Guess a number between 1 to 9\n")
while True:

	x=int(input())
	if x > a:
		print("to high, guess again\n")
		count+=1
	elif x < a:
		print("to low, guess again\n")
		count+=1
	else:
		print("correct!!, and it took you", count , "guess")
		count = 0
		a=random.randint(1,9)
		s= input("To play again type 1 to exit type Exit\n")
		if s == "1":
			print("Guess a number between 1 to 9\n")
			continue
		elif s == "Exit":
			break