import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: count (int) number of iterations
    """
    count = 0
    while(n != 1):
        count += 1
        
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
                      # the last print is 1
    return count

def graph(yertle, maxi, wn, upper):

	yertle.up()
	yertle.goto(1,0)
	yertle.down()

	max_so_far = 0
	for start in range(1, upper+1):
		result = seq3np1(start)

		yertle.goto(start, result)
		yertle.dot(5, "blue")
	
		if result > max_so_far:
			max_so_far = result
			maxi.clear()
			wn.setworldcoordinates(0, 0, start + 10, max_so_far + 10)
			label = "Maximum so far: {}, {}".format(start, result)
			maxi.up()
			maxi.goto(0, max_so_far+5)
			maxi.down()
			maxi.write(label, True, align = 'left', font = 'Arial')

	yertle.up()
	yertle.goto(upper + 10, 0)
	yertle.down()
	yertle.left(180)
	yertle.forward(upper + 10)
	yertle.right(90)
	yertle.forward(max_so_far + 10)


def main():
	seq3np1(3)
	upper_range = int(input("Please enter a positive number for your upper range. "))

	if upper_range > 0:
		for start in range(1, upper_range+1):
			iterations = seq3np1(start)
			print("n = ", start, ", number of iterations: ", iterations)

		wn = turtle.Screen()
		yertle = turtle.Turtle()
		maxi = turtle.Turtle()
		wn.setworldcoordinates(0, 0, 10, 10)

		graph(yertle, maxi, wn, upper_range)
	
		wn.exitonclick()
	else:
		quit()	
main()