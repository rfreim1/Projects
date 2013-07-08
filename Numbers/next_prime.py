#Have the program find prime numbers 
#until the user chooses to stop asking for the next one.

import math

def next_prime(current):
        while True:
                prime = True
                x = current+1
                if x % 2 == 0:
                        current = current + 1
                        continue

                for i in range(3, int(math.sqrt(x)+1), 2):
                        if x % i == 0:
                                current = current+1
                                prime = False
                                break
                if prime:
                	return x


if __name__ == '__main__':
        run = 1
        x = 2
        print x
        while run == 1:
                ans = raw_input("Do you want to see the next prime number? (Y/N)")
                if ans.lower() == 'y':
                        x = next_prime(x)
                        print x
                elif ans.lower() == 'n':
                        run = 0
                        print "Fine. We are done here."
                else:
                        print "You didnt answer with Y or N..."
