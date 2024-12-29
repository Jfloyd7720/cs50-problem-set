creditCard = input("Enter credit card number: ")

length = len(creditCard)
newList = []
endSum = 0
endSum2 = 0

for char in creditCard:
    newList.append(char)

for i in newList[-2:-17:-2]:
    calc = int(i)*2
    if calc > 9:
        for n in str(calc):
            endSum += (int(n))
    else:
        endSum += int(calc)

for j in newList[1:16:2]:
    endSum2 += int(j)

print(endSum + endSum2)



