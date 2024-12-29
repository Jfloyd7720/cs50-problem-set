import math

userInput = input("Enter height: ")
numSpace = int(userInput) - 1
numHash = 1
gap = 2
outputList = []

while numSpace >= 0:
    outputList.append(numSpace * " ")
    numSpace -= 1
    outputList.append(numHash * "#")
    outputList.append(gap * " ")
    outputList.append(numHash * "#")
    numHash += 1
    outputList.append('\n')
s = ''.join(str(x) for x in outputList)
print(s)


