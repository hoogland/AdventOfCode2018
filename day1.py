filename = "resources/day1.txt"

changes = [int(x) for x in open("resources/day1.txt").readlines()]

#Solution first star
print("Final frequency: " + str(sum(changes)))

#solution second star
frequency = 0
frequencies = set([0])
inFrequencies = False

while inFrequencies == False:
    for line in changes:
        frequency += line
        if frequency in frequencies:
            print("First double value: " + str(frequency))
            inFrequencies = True
            break
        frequencies.add(frequency)


#Lessons learned: 
# set is way faster then List
# cleaner to read in the changes into variable and convert to int
