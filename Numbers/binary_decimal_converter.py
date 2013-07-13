#Develop a converter to convert a decimal number to binary
#or a binary number to its decimal equivalent.

from math import log

def biToDec(binary):
    length = len(binary) -1
    decimal = 0
    
    for x in binary:
        decimal += int(x)*2**length
        length -= 1
    
    return decimal

def decToBi(decimal):
    decimal = int(decimal)
    exp = int(log(decimal, 2))
    
    binary = []
    for i in range(exp, -1, -1):
        if decimal - 2**i >=0:
            binary.append('1')
            decimal -= 2**i
        else:
            binary.append('0')
    
    return ''.join(binary)


if __name__ == '__main__':
    num = raw_input('Enter number to convert: ')

    try:
       val = int(num)
    except ValueError:
       print("That's not an int!")
    else:
        choice = raw_input('Convert to binary or decimal? (Enter B/D): ')
        
        if choice.lower() == 'b':
                print decToBi(num)
        elif choice.lower() == 'd':
            notBi = False
            for x in list('23456789'):
                if x in num:
                    print 'Not a binary number'
                    notBi = True
                    break
            if not notBi:
                print biToDec(num)
        else:
            print "You did not answer if B or D...."
        
