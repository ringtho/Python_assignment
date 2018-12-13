binaries = []
numbers = input().split(",")


for num in numbers:
	try:
		x = int(num, 2)
	except ValueError:
		print("\n\tPlease provide binary numbers!!!\n")
	else:
		y = x%5
		if y == 0:
			binaries.append(num)
		
print(','.join(binaries))



