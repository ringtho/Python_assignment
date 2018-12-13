print("Bank Transactions")
print("Enter 'q' to stop the transactions")
print("\nThe format is transaction type followed by amount in numbers.")
print("D for deposit and W for withdraw e.g D 100\n")

account_balance = 0

while True:
	
	word = input("Please provide transaction: ")
	transaction = word.split(" ")
	
	try:
		trans_type = transaction[0]
		amount = int(transaction[1])
	
	except ValueError:
		print("\tPlease use the provided format in the instructions!!!!.\n")
	
	else:
		if trans_type=="D" or trans_type=="d":
			account_balance += amount
		elif trans_type=="W" or trans_type=="w":
			account_balance -= amount
		else:
			print("The format is 'D 100' for deposit and 'W 100' for withdraw!!. ")
		
		word = input("Continue (Y/N) : ")
		if not (word[0] =="Y" or word[0] =="y") :
			break
		
print("\nYour account balance is " +str(account_balance)+ " /= ")
