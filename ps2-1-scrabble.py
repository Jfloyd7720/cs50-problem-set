thisdict = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

user = input("Player 1, enter a word: ").upper()
userTwo = input("Player 2, enter a word: ").upper()

# def calculate_score(word):
#     return sum(thisdict.get(char, 0) for char in word if char.isalpha())

# final = calculate_score(user)
# finalTwo = calculate_score(userTwo)


final = 0
finalTwo = 0

for char in user:
    if char.isalpha():
        value = thisdict[char]
        final += value

for char in userTwo:
    if char.isalpha():
        value = thisdict[char]
        finalTwo += value

if final > finalTwo:
    print("Player 1 wins!!")
elif finalTwo > final:
    print("Player 2 wins!!")
else:
    print("Its a TIE!")








