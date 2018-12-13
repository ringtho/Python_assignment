
numbers = list(range(2000,3201))

answers = []

for number in numbers:
	divide = number % 7
	multiple = number % 5 
	if divide == 0 and multiple != 0:
		answers.append(number)

print(answers)
