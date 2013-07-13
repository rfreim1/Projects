#Calculate the total cost of tile it would take to cover a floor plan of width 
#and height, using a cost entered by the user.

def tile(cost, width, height):
	return cost*width*height


def test():
	assert tile(10,10,10) == 1000
	assert tile(15,10,10) == 1500
	assert tile(0,10,10) == 0


if __name__ == '__main__':
	test()
	cost = input("Enter cost of a sqft. tile: ")
	width = input("Enter width of floor plan: ")
	height = input("Enter height of floor plan: ")
	print "The cost of the tiling is $%.2f" %(tile(cost, width, height))
