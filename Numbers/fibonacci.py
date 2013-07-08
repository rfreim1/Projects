#Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

print "This provides the fibonacci sequence up to the Nth number given as input."
number = input("Enter number: ")

def fibonacci(num):
        print "Sequence: "
        seq = [0,1]
        if num == 1:
                print "0"
        elif num <= 0:
                print "ERROR: cannot compute...beep boop bop"
        else:   
                while len(seq) < num:
                        seq.append(seq[-1]+seq[-2])
                for x in seq:
                        print x

fibonacci(number)
