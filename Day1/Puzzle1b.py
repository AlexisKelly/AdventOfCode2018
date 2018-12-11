frequencies = set()
frequencyDuplicateFound = False
total = 0
while not frequencyDuplicateFound:
    f = open("Puzzle1input","r")
    fl = f.readlines()

    for x in fl:
        total = total + int(x)
        if total in frequencies:
            frequencyDuplicateFound = True
            print("1st repeated is="+str(total))
            break
        else:
            frequencies.add(total)
