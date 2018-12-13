marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]

small = []
big = []

for mark in marks:
	if mark > 50:
		big.append(mark)
	else:
		small.append(mark)
		
	if mark < 20:
		print("Repeat!")
	elif 20 <= mark <= 39:
		print("Very Poor!!")
	elif 40 <= mark <= 59:
		print("Poor!")
	elif 60 <= mark <= 69:
		print("Good")
	elif 70 <= mark <= 89:
		print("Very Good")
	else:
		print("Excellent")
		
print("\nThe lists are: ")
print(small)
print(big)
