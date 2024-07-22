import random
path = 'words.txt'
words = []
with open(path, 'r') as file:
    for line in file:
        word = line.rstrip()
        words.append(word)

guess = random.choice(words)
player = input("What's your guess?")
while guess != player:
    if not player.isalpha():
        print("Word can't have special characters")
        player = input("What's your guess?")
        continue
    output = ""
    for i in range(5):
        if guess[i] == player[i]:
            output += guess[i]
        else:
            output += "_"
    print(output + "\n")
    player = input("What's your guess?")
print("Congratulations the word is "+ guess)