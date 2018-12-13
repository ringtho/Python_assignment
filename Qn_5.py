
def square_of_no():
	squares = []
	numbers = list(range(1,21))
	
	for number in numbers:
		square = number * number
		squares.append(square)
	print("The squares: ")	
	for square in squares[:5]:
		print("\t-"+ str(square))
	
square_of_no()	

	
	
