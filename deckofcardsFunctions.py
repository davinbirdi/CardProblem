# --------------------------------------
# Functions:
# --------------------------------------

# Function: Create Card Deck
# Inputs:   None
# Outputs:  Deck of 52 suited cards

def createDeck():
    deck = []
    card_nums = list(range(1, 14))
    card_suites = ['H', 'D', 'S', 'C']

    for x in card_nums:
        for y in card_suites:
            deck.append(str(x)+str(y))
    
    return deck

# Function: Create a Simpler Deck to work with:
# Inputs:   num - size of deck
# Outputs:  Deck of size n
def createSimpleDeck(num):
    container = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    deck = []
    i = 0
    while i < num:
        deck.append(container[i])
        i = i + 1
    return deck


# Function: Factorial
# Input:    int n
# Output:   int n!
def factTR(n,a):
    if (n == 1):
        return a
    return factTR(n-1, n * a)

def fact(n,a):
    if (n == 1):
        return a
    return factTR(n-1, n * a)




'''  Don't want to throw this away just yet
#Dealing deck1 randomly into deck3
for i in reversed(range(5)):
    # len(deck1)-1 to prevent accessing out of range
    dealt = randint(0, len(deck1)-1)
    print(str(deck1[dealt]), end="   ")
    deck3.append(deck1[dealt])
    deck1.pop(dealt)
    
    print("   ", end="")
    for x in range(i):
        print("" + str(deck1[x]), end="")
    print("")
'''
'''
for i in range(len(deck1)):
    dealt = randint(0, len(deck1)-1)
    deck3.append(deck1[dealt])
    deck1.pop(dealt)
 '''   