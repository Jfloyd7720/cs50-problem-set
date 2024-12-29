import math

change = int(input("Change owed: "))
cents = [25, 10, 5, 1]
changeCount = 0

for i in cents:
    while change >= i:
        change -= i
        changeCount += 1
print(changeCount)

