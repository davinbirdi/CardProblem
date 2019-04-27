print("Card Problem\n")


# Functions:
# Create Card Deck
def createDeck():
    deck = []
    card_nums = list(range(1, 14))
    card_suites = ['H', 'D', 'S', 'C']

    for x in card_nums:
        for y in card_suites:
            deck.append(str(x)+str(y))
    
    return deck


def createSimpleDeck(num):
    container = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    deck = []
    i = 0
    while i < num:
        deck.append(container[i])
        i = i + 1
    return deck


# Algorithm:

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

