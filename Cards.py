import random as rand 
            
class Deck:

    def __init__ (self):
        self.currentDeck = []
        self.generate()

# generates new deck of 52 cards
# cards are tuples -> (rank, suit)
    def generate(self):
        suits = ["D", "H", "S", "C"]
        ranks = [*range(1, 14, 1)]
        for suit in suits:
            for rank in ranks:
                self.currentDeck.append((rank, suit))
        rand.shuffle(self.currentDeck)
        # print(self.currentDeck)

# removes card tuple from deck
    def removeFromDeck(self, toRemove):
        for card in self.currentDeck:
            if card == toRemove:
                self.currentDeck.remove(card)
                break

# takes user input to cut deck
    def playerCut(self):
        print("\nPLAYER CUTS THE DECK!")
        while True:
            try:
                cutPosition = int(input('Enter an integer between 1 and {len}: '.format(len=len(self.currentDeck)-1)))
            except ValueError:
                print('That\'s not a number!')
            else:
                if 1 <= cutPosition <= len(self.currentDeck)-1:
                    break
                else:
                    print('Out of range. Try again')
        cutPosition -= 1
        cutCard = self.currentDeck[cutPosition]
        print("Cut card is: ")
        self.showCard(cutCard)
        self.removeFromDeck(cutCard)
        return(cutCard)

# randomly cuts deck for bot
    def botCut(self):
        print("\nBOT CUTS THE DECK!")
        cutCard = self.currentDeck[rand.randint(0, len(self.currentDeck)-1)]
        print("Cut card is: ")
        self.showCard(cutCard)
        self.removeFromDeck(cutCard)
        return(cutCard)

# prints a properly formatted display of a given card 
    def showCard(self, card):
        rank = card[0]
        suit = card[1]
        tRank = ""
        tSuit = ""
        if rank == 1:
            tRank = "Ace"
        elif rank == 13:
            tRank = "King"
        elif rank == 12:
            tRank = "Queen"
        elif rank == 11:
            tRank = "Jack"
        else:
            tRank = str(rank)
        if suit == "D":
            tSuit = "Diamonds"
        elif suit == "H":
            tSuit = "Hearts"
        elif suit == "S":
            tSuit = "Spades"
        elif suit == "C":
            tSuit = "Clubs"
        print(card, ", {rank} of {suit}".format(rank=tRank, suit=tSuit))

# Deals a new 6 card hand
    def dealHand(self):
        i = 0
        hand = []
        while i < 6:
            randCard = rand.randint(0, len(self.currentDeck)-1)
            hand.append(self.currentDeck[randCard])
            self.removeFromDeck(self.currentDeck[randCard])
            i+=1
        return hand

# returns generated deck
    def getCurrentDeck(self):
        return self.currentDeck

# prints generated deck
    def printCurrentDeck(self):
        print(self.currentDeck)

if __name__ == "__main__":
    test = Deck()
    test.playerCut()