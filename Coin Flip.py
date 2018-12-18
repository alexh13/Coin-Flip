# Assignment calls for a coin toss program
# "Pretend that you have been hired by the National Football League (NFL) to write a program to replace the coin toss.
# The output should be simple: either the word "Heads" or the word "Tails". Allow the user to specify
# (via keyboard data entry) the number of coin tosses to perform when you run the program, and
# have the program display the result of each coin toss (that is, "Heads" or "Tails")"
# Assignment calls for a coin toss program
# Version 2, everything put into a function
import random  # import random.randint


def coinFlip():
    print("Hello this is my a coin toss simulation")
    while True:  # while the following statement is true
        heads = tails = 0  # heads - tails value is zero
        while True:  # while the following statement is true
            count = int(input("Enter the number of tosses to perform:"))  # count value becomes input of number of toss
            break

        while tails + heads < count:  # while heads+tails is less than count is true 
            coin = random.randint(1, 2)  # process random flip
            if coin == 2:  # if 2 was result then
                heads = heads + 1
            else:
                tails = tails + 1

        print("Coin tossed", count, "time(s)")  # show output number of requested coin toss(s)
        print("Heads", heads, "time(s)")  # show output number of head(s)
        print("Tails", tails, "time(s)")  # show output number of tail(s)
        break


coinFlip()
