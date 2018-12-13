
print("Provide a sentence!")
print("(Enter 'q' to end)\n")

sentences = []

while True:
	sentence = input(": ")
	if sentence == 'q':
		break;
	else:
		sentences.append(sentence)
print("\nThe capitalized sentences are: ")	
for sentence in sentences:
	print("-"+sentence.upper())
