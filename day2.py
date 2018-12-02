filename = "resources/day2.txt"

boxes = [str(x).rstrip() for x in open(filename).readlines()]

def check_freq(str):
    freq = {}
    for c in str:
       freq[c] = str.count(c)
    return freq

#star 1 solution
twoOccurance = 0
threeOccurance = 0
for box in boxes:
    frequencies = check_freq(box)
    if 2 in frequencies.values():
        twoOccurance += 1
    threeOccurance += list(frequencies.values()).count(3)

print('The checksum = ' + str(twoOccurance) + " * " + str(threeOccurance) + " = " + str(twoOccurance * threeOccurance))

#star 2 solution
commonLetters = ''
for index, box1 in enumerate(boxes):
    for box2 in boxes[index:]:
        if sum(a != b for a, b in zip(box1, box2)) == 1:
            for a, b in zip(box1, box2):
                if a == b:
                    commonLetters += a
            print("The common letters are: " + commonLetters)

#Lessons learned
#   Zip events can be used to combine two variables and then to iterate through them together