#Calculate the monthly payments of a fixed term mortgage over given Nth terms 
#at a given interest rate. 


if __name__ == "__main__":
	p =  input("Enter initial principle: ")
	interest = input("Enter interest rate: ")
	terms = input("Enter number of terms: ")

	print "Monthy payment is: "
	print p*((interest*(1+interest)**terms)/ ((1 + interest)**terms - 1))
