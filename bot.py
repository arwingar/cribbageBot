from Cards import Deck
import scorermod
# Code For Greedy Algo Bot
class Bot:
    
    def __init__ (self, currentDeck):
        self.currentDeck = currentDeck

    # initializes new deck
    def newDeck(self, currentDeck):
        self.currentDeck = currentDeck

	#Bot recieves a hand consisting of 6 cards. 
	#output will be ((list of new deck), (list of discarded deck))
    def discard(self, six_card_deck):
        print("PLAYER's CURRENT HAND (discard two):")
        for card in six_card_deck:
            self.currentDeck.showCard(card)

        currentHighScore = 0
        currentBestHand = []
        discard_list = []
        # generate list of all possible discard combinations
        possibleDiscards = [(a, b) for i, a in enumerate(six_card_deck) for b in six_card_deck[i + 1:]]

        # loop through all possible discard combinations
        for discards in possibleDiscards:
            deckTemp = six_card_deck.copy()
            deckTemp.remove(discards[0])
            deckTemp.remove(discards[1])
            score, msg = scorermod.show_calc_score(deckTemp, False)
            
            # if new best score if found, set to current max score
            if score > currentHighScore:
                currentHighScore = score
                currentBestHand = deckTemp.copy()
                discard_list = discards
        
        # if discard list is shorter than two cards (meaning no max score was found) select first two cards in deck (randomly generated)
        if len(discard_list) < 2:
            while len(discard_list) < 2:
                discard_list.append(six_card_deck[0])
                six_card_deck.remove(six_card_deck[0])
                discard_list.append(six_card_deck[0])
                six_card_deck.remove(six_card_deck[0])

        return (currentBestHand, discard_list)

	#hand represents a list of Cards
    # bot must play one card in current hand
    def playCard(self, hand, playedCards):
        currentHighScore = 0
        bestCard = hand[0]
        
        # loop through each possible card to play
        for card in hand:
            deckTemp = playedCards.copy()
            deckTemp.append(card)
            scoreTemp = 0
            
            # check who the first player is
            # get score for hypothetical card played
            if len(playedCards) % 2 == 0:
                players = ["Player", "Bot"]
                scores, currentCount, play_log = scorermod.play_calc_score_set(playedCards, players)
                scoreTemp = scores[players[0]]
            else:
                players = ["Bot", "Player"]
                scores, currentCount, play_log = scorermod.play_calc_score_set(playedCards, players)
                scoreTemp = scores[players[1]]
            # if new best score is found, set to current max score
            if scoreTemp > currentHighScore:
                currentHighScore = scoreTemp
                bestCard = card
        
        return bestCard

if __name__ == "__main__":
	testDeck = Deck()
	test = Bot(testDeck)
	hand = testDeck.dealHand()
	temp = test.discard(hand)
	# test.playCard(temp)


