# from Cards import Cards
from Cards import Deck
from random import randrange
class RandBot:
    
    def __init__ (self, currentDeck):
        self.currentDeck = currentDeck

    def newDeck(self, currentDeck):
        self.currentDeck = currentDeck

	#Bot recieves a hand consisting of 6 cards.
    # discards 2 of the cards randomly
	#output will be ((list of new deck), (list of discarded deck))
    def discard(self, six_card_deck):
        discard_list = []
        print("RANDBOT's CURRENT HAND (discard two):")
        for card in six_card_deck:
            self.currentDeck.showCard(card)

        randTemp = randrange(len(six_card_deck))
        discard_list.append(six_card_deck[randTemp])
        six_card_deck.remove(six_card_deck[randTemp])
        randTemp = randrange(len(six_card_deck))
        discard_list.append(six_card_deck[randTemp])
        six_card_deck.remove(six_card_deck[randTemp])
        
        print("RANDBOT's NEW HAND (discarded):")
        for card in six_card_deck:
            self.currentDeck.showCard(card)

        return (six_card_deck, discard_list)

	#hand represents a list of Cards
    # plays one card randomly
    def playCard(self, hand, playedCards):
        print("RANDBOT'S PLAYABLE HAND:")
        for card in hand:
            self.currentDeck.showCard(card)
        
        cardTmp = hand[randrange(len(hand))]
        return cardTmp

if __name__ == "__main__":
	testDeck = Deck()
	test = RandBot(testDeck)
	hand = testDeck.dealHand()
	temp = test.discard(hand)[0]
	# print(test.playCard(temp))


