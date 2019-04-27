print("Card Problem\n")
# ------------------------------------------
# Algorithm:
# Goal: To model the different unique combinations of combining two simple decks
# ------------------------------------------

# Initiallizing
from deckofcardsFunctions import *

deck1 = createSimpleDeck(5)
deck2 = createSimpleDeck(5)

deck3 = []
i = 0

# Dealing Deck1
print("D:\tDeck1:")
for i in reversed(range(5)):
    print(str(deck1[0]), end="   ")
    deck3.append(deck1[0])
    deck1.pop(0)
    print("   ", end="")
    for x in range(i):
        print("" + str(deck1[x]), end="")
    print("")

print("\nDeck3:")
for i in range(len(deck3)):
    print(deck3[i], end="")

