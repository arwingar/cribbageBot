# from Cards import Cards
from Cards import Deck
class Player:

	def __init__ (self, currentDeck):
			self.currentDeck = currentDeck

	def newDeck(self, currentDeck):
			self.currentDeck = currentDeck

	#Human player recieves a hand consisting of 6 cards. 
	#Human player will discard 2 of the 6
	#output will be ((list of new deck), (list of discarded deck))
	# most of the code just checks for incorrect inputs from player
	def discard(self, six_card_deck):
		discard_list = []
		print("YOUR CURRENT HAND (discard two):")
		for card in six_card_deck:
			self.currentDeck.showCard(card)

		rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')
		if ", " not in rank_suit_str:
			while ", " not in rank_suit_str:
				print('ERROR: Not correct format. Must have the ", " included as well')
				rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')


		rank_suit_lst = rank_suit_str.split(", ")

		if not rank_suit_lst[0].isnumeric():
			while not rank_suit_lst[0].isnumeric():
				print('ERROR: Rank is not numeric')
				rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')
				if ", " not in rank_suit_str:
					while ", " not in rank_suit_str:
						print('ERROR: Not correct format. Must have the ", " included as well')
						rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')
				rank_suit_lst = rank_suit_str.split(", ")



		rank = int(rank_suit_lst[0])
		suit = rank_suit_lst[1]
		suit = suit.upper()

		card_tmp = (rank, suit)
		print(card_tmp)
		if card_tmp not in six_card_deck:
			while card_tmp not in six_card_deck:
				print("ERROR: You entered a card not in the hand.")
				rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')
				if ", " not in rank_suit_str:
					while ", " not in rank_suit_str:
						print('ERROR: Not correct format. Must have the ", " included as well')
						rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')


				rank_suit_lst = rank_suit_str.split(", ")
				if not rank_suit_lst[0].isnumeric():
					while not rank_suit_lst[0].isnumeric():
						print('ERROR: Rank is not numeric')
						rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')
						if ", " not in rank_suit_str:
							while ", " not in rank_suit_str:
								print('ERROR: Not correct format. Must have the ", " included as well')
								rank_suit_str = input('Enter the first card to discard in this format - "13, S", "3, D", etc.: ')

				rank_suit_lst = rank_suit_str.split(", ")

				rank = int(rank_suit_lst[0])
				suit = rank_suit_lst[1]
				suit = suit.upper()

				card_tmp = (rank, suit)

		six_card_deck.remove(card_tmp)
		discard_list.append(card_tmp)


		print("YOUR CURRENT HAND (discard one):")
		for card in six_card_deck:
			self.currentDeck.showCard(card)

		rank_suit_str = input('Enter the second card to discard in this format - "13, S", "3, D", etc.: ')
		if ", " not in rank_suit_str:
			while ", " not in rank_suit_str:
				print('ERROR: Not correct format. Must have the ", " included as well')
				rank_suit_str = input('Enter the second card to discard in this format - "13, S", "3, D", etc.: ')

		rank_suit_lst = rank_suit_str.split(", ")


		if not rank_suit_lst[0].isnumeric():
			while not rank_suit_lst[0].isnumeric():
				print('ERROR: Rank is not numeric')
				rank_suit_str = input('Enter the second card to discard in this format - "13, S", "3, D", etc.: ')
				if ", " not in rank_suit_str:
					while ", " not in rank_suit_str:
						print('ERROR: Not correct format. Must have the ", " included as well')
						rank_suit_str = input('Enter the second card to discard in this format - "13, S", "3, D", etc.: ')
				rank_suit_lst = rank_suit_str.split(", ")



		rank = int(rank_suit_lst[0])
		suit = rank_suit_lst[1]
		suit = suit.upper()

		card_tmp = (rank, suit)
		if card_tmp not in six_card_deck:
			while card_tmp not in six_card_deck:
				print("ERROR: You entered a card not in the hand.")
				rank_suit_str = input('Enter the second card to discard in this format: - "13, S", "3, D", etc.: ')
				if ", " not in rank_suit_str:
					while ", " not in rank_suit_str:
						print('ERROR: Not correct format. Must have the ", " included as well')
						rank_suit_str = input('Enter the second card to discard in this format - "13, S", "3, D", etc.: ')

				rank_suit_lst = rank_suit_str.split(", ")
				if not rank_suit_lst[0].isnumeric():
					while not rank_suit_lst[0].isnumeric():
						print('ERROR: Rank is not numeric')
						rank_suit_str = input('Enter the second card to discard in this format - "13, S", "3, D", etc.: ')
						if ", " not in rank_suit_str:
							while ", " not in rank_suit_str:
								print('ERROR: Not correct format. Must have the ", " included as well')
								rank_suit_str = input('Enter the second card to discard in this format - "13, S", "3, D", etc.: ')
						rank_suit_lst = rank_suit_str.split(", ")

				rank_suit_lst = rank_suit_str.split(", ")
				rank = int(rank_suit_lst[0])
				suit = rank_suit_lst[1]
				suit = suit.upper()

				card_tmp = (rank, suit)
		six_card_deck.remove(card_tmp)
		discard_list.append(card_tmp)

		return (six_card_deck, discard_list)

	#hand represents a list of Cards
	# most of the code just checks for incorrect inputs from player
	def playCard(self, hand, playedCards):
		print("YOUR PLAYABLE HAND:")
		for card in hand:
			self.currentDeck.showCard(card)
		cardToPlay = input('Enter a card to play in this format "1, H", "4, C", etc.: ')
		if ", " not in cardToPlay:
			while ", " not in cardToPlay:
				print('ERROR: Not correct format. Must have the ", " included as well')
				cardToPlay = input('Enter enter a card to play in this format - "1, H", "4, C", etc.: ')

		rank_suit_lst = cardToPlay.split(", ")

		if not rank_suit_lst[0].isnumeric():
			while not rank_suit_lst[0].isnumeric():
				print('ERROR: Rank is not numeric')
				cardToPlay = input('Enter a card to play in this format - "13, S", "3, D", etc.: ')
				if ", " not in cardToPlay:
					while ", " not in cardToPlay:
						print('ERROR: Not correct format. Must have the ", " included as well')
						cardToPlay = input('Enter a card to play in this format - "13, S", "3, D", etc.: ')
				rank_suit_lst = cardToPlay.split(", ")

		rank = int(rank_suit_lst[0])
		suit = rank_suit_lst[1]
		suit = suit.upper()

		cardTmp = (rank, suit)
		if cardTmp not in hand:
			while cardTmp not in hand:
				print("ERROR: You entered a card not in the hand.")
				cardToPlay = input('Enter a card to play in this format "1, H", "4, C", etc.: ')

				if ", " not in cardToPlay:
					while ", " not in cardToPlay:
						print('ERROR: Not correct format. Must have the ", " included as well')
						cardToPlay = input('Enter enter a card to play in this format - "1, H", "4, C", etc.: ')


				rank_suit_lst = cardToPlay.split(", ")

				if not rank_suit_lst[0].isnumeric():
					while not rank_suit_lst[0].isnumeric():
						print('ERROR: Rank is not numeric')
						cardToPlay = input('Enter a card to play in this format - "13, S", "3, D", etc.: ')
						if ", " not in cardToPlay:
							while ", " not in cardToPlay:
								print('ERROR: Not correct format. Must have the ", " included as well')
								cardToPlay = input('Enter a card to play in this format - "13, S", "3, D", etc.: ')
						rank_suit_lst = cardToPlay.split(", ")

				rank = int(rank_suit_lst[0])
				suit = rank_suit_lst[1]
				suit = suit.upper()

				cardTmp = (rank, suit)

		return cardTmp

if __name__ == "__main__":
	testDeck = Deck()
	test = Player(testDeck)
	hand = testDeck.dealHand()
	temp = test.discard(hand)[0]
	# test.playCard(temp)


