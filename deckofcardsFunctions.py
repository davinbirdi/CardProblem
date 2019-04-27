# --------------------------------------
# Functions:
# --------------------------------------

# Create Card Deck
# Inputs: None
# Outputs: Deck of 52 suited cards

def createDeck():
    deck = []
    card_nums = list(range(1, 14))
    card_suites = ['H', 'D', 'S', 'C']

    for x in card_nums:
        for y in card_suites:
            deck.append(str(x)+str(y))
    
    return deck

# Create a Simpler Deck to work with:
# Inputs:  num - size of deck
# Outputs: Deck of size n
def createSimpleDeck(num):
    container = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    deck = []
    i = 0
    while i < num:
        deck.append(container[i])
        i = i + 1
    return deck
