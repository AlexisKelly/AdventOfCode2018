
f = open("Puzzle1input","r")
fl = f.readlines()
total = 0
for x in fl:
    # add or take away from value int
    print("total before adding x="+str(total))
    total = total + int(x)
    print("x="+str(x))
    print("total"+str(total))

