





print("welcome to treasure island")
print("your mission is to find the treasure.")
print("you come up to a path with two directions.")
leftorright = input("would you like to take a left or right?")
if leftorright == "right":
        print("game over. you fell in a hole")
        exit()

else:
    print("you went down the right path")

swimorwait = input("you come a pond, do you want to wait for a boat or swim?")
if swimorwait == ("swim"):
    print("game over. you drowned.")

else:
    print("you safely made it across the lake to a house")

colorofdoor = input("what door would you like to go through? (green, red, and yellow)")

if colorofdoor == "red":
    print("good job, you found the treasure")
elif colorofdoor == "green":
    print("game over. you fell into a pit of snakes.")
else:
    print("game over. you got golden showered on by r.kelly")

