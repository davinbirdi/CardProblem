print("Card Problem\n")
# ------------------------------------------
# Algorithm:
# Goal: To model the different unique combinations of combining two simple decks
# ------------------------------------------

# Initiallizing
from deckofcardsFunctions import *
from random import randint

deck1 = createSimpleDeck(5)
deck2 = createSimpleDeck(5)

deck3 = []
i = 0

# Dealing Deck1
print("D:\tDeck1:")
for i in reversed(range(5)):
    dealt = randint(0,len(deck1)-1)
    print(str(deck1[dealt]), end="   ")
    
    deck3.append(deck1[dealt])
    
    deck1.pop(dealt)
    
    print("   ", end="")
    for x in range(i):
        print("" + str(deck1[x]), end="")
    print("")

print("\nDeck3:")
for i in range(len(deck3)):
    print(deck3[i], end="")

