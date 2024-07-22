import random
path = 'words.txt'
words = []
with open(path, 'r') as file:
    for line in file:
        word = line.rstrip()
        words.append(word)

guess = random.choice(words)
player = input("What's your guess? ")
output = "_____"
while guess != player:
    if not player.isalpha():
        print("Word can't have special characters")
        player = input("What's your guess? ")
        continue
    elif len(player) > 5:
        print("Guess the 5-letter word\n")
        player = input("What's your guess? ")
        continue
    
    for i in range(5):
        if guess[i] == player[i]:
            output = output[:i] + guess[i] + output[i+1:]
        
    print(output + "\n")

    player = input("What's your guess? ")
print("Congratulations the word is "+ guess)