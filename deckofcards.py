print("Card Problem\n")
# ------------------------------------------
# Algorithm:
# Goal: To model the different unique combinations of combining two simple decks
# ------------------------------------------

# Initiallizing
from deckofcardsFunctions import *
from random import randint


size1= 3
size2 = 3
bigdeck = []

# Dealing Deck1
print("D:\tDeck1:")

# Stack the decks
# Deal the deck
for x in range(fact(size1+size2,1)):
    deck1 = createSimpleDeck(size1)
    deck2 = createSimpleDeck(size2)
    deck3 = []

    for i in range(len(deck2)):
        deck1.append(deck2[i])

    for i in reversed(range(len(deck1))):
        # len(deck1)-1 to prevent accessing out of range
        dealt = randint(0, len(deck1)-1)
        #print(str(deck1[dealt]), end="   ")
        deck3.append(deck1[dealt])
        deck1.pop(dealt)
        
        #print("   ", end="")
        #for x in range(i):
        #    print("" + str(deck1[x]), end="")
        #print("")
        
    print("\nDeck3:")
    for i in range(len(deck3)):
        print(deck3[i], end="")

    bigdeck.append(deck3)



print('\n\nEach Variation')

for x in range(len(bigdeck)):
    for i in range(len(deck3)):
        print(bigdeck[x][i], end="")
    print('')
