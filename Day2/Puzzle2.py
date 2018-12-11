import collections

# get the file 1st
f = open("Puzzle2input.txt","r")
fl = f.readlines()
total = 0
amount_containing_two_of_any_letter = 0;
amount_containing_three_of_any_letter = 0;
for line in fl:
    d = collections.defaultdict(int)
    foundTwoLetters = False
    foundThreeLetters = False
    for c in line:
        # check each character to see if its in the string more than once
        d[c] += 1
    for c in d:
        # if it contains 2 and hasn't been incremented then add to the int
        if d[c] == 2 and not foundTwoLetters:
            amount_containing_two_of_any_letter += 1
            foundTwoLetters = True
        # if it contains 3 and hasn't been incremented then add to the int
        if d[c] == 3 and not foundThreeLetters:
            amount_containing_three_of_any_letter += 1
            foundThreeLetters = True

# multiple both numbers together to get a basic checksum
basic_checksum = amount_containing_two_of_any_letter * amount_containing_three_of_any_letter
print("Basic Checksum="+str(basic_checksum))