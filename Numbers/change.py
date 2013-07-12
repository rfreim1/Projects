#The user enters a cost and then the amount of money given. The program will figure 
#out the change and the number of quarters, dimes, nickels, pennies needed.


def get_change(cost, money):
        change = [0,0,0,0,0]
        difference = money - cost
        
        if difference < 0:
                print "Not enough money given"
                
        if difference >= 1:
                        change[0] += int(difference)
                        difference -= int(difference)
        difference = 100*difference
        if difference >= 25:
                change[1] += int(difference/25)
                difference = int(difference % 25)
        if difference >= 10:
                change[2] += int(difference/10)
                difference = int(difference % 10)
        if difference >= 5:
                change[3] += int(difference/5)
                difference = int(difference % 5)
        if difference >= 1:
                change[4] += difference

        return change



if __name__ == '__main__':
        cost = input("Enter cost: ")
        money = input("Enter money given: ")

        change = get_change(cost, money)
        print "dollars: " + str(change[0]) + " q: " + str(change[1])
        print (" d: " + str(change[2]) + " n: " + str(change[3])
               + " p: " + str(change[4]))
