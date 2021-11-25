# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)
print("Welcome to Addition Trainer!")
print("I will ask you 10 addition problems.")
import random
score = 0
for i in range(10):
	a = random.randint(0, 99)
	b = random.randint(0, 99)
	print("What is the sum of",a, "and",b, "?")
	user_ans = int(input("Enter you answer: "))
	ans = a + b
	if user_ans == ans:
		print("That's right!")
		score = score + 1
	else:
		print("Wrong!")
print("You got",score,"/ 10!")