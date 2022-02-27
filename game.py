import random as rand
import sys, os
from player import Player as player
from bot import Bot as bot
from randbot import RandBot as randbot
from Cards import Deck as deck
from cribbage_scorer import cribbage_scorer

class Cribbage:

    def __init__(self):
        print("WELCOME TO CRIBBAGE!\n")
        
        self.currentDeck = []
        self.player = player(self.currentDeck)
        self.bot = bot(self.currentDeck)
        self.currentDeal = 1
        self.playerScore = 0
        self.botScore = 0
        self.winner = 2

    # start new game
    def game(self):
        print("121 Points to win")
        while not self.checkScore():
            self.newRound()
        return self.winner

    # start new round
    def newRound(self):
        # initialize
        self.printScore()
        self.currentDeck = deck()
        currentCrib = []
        players = ["Player", "Bot"]
        cutCard = ()
        
        # generate new deck and give to player/bot
        self.player.newDeck(self.currentDeck)
        self.bot.newDeck(self.currentDeck)

        # generate new hands for players
        playerHand = self.currentDeck.dealHand()
        botHand = self.currentDeck.dealHand()
        
        # player discards and builds crib
        playerTemp = self.player.discard(playerHand)
        playerHand = playerTemp[0]
        currentCrib.append(playerTemp[1][0])
        currentCrib.append(playerTemp[1][1])

        # bot discards and builds crib
        botTemp = self.bot.discard(botHand)
        botHand = botTemp[0]
        currentCrib.append(botTemp[1][0])
        currentCrib.append(botTemp[1][1])

        # generate permanent copies
        playerHandPerm = playerHand.copy()
        botHandPerm = botHand.copy()

        print("Current Crib:", currentCrib)

        # cut the deck, 0 for player, 1 for bot
        if self.currentDeal == 0:
            cutCard = self.currentDeck.playerCut()
            scores, msg, = cribbage_scorer.cut_calc_score(cutCard, players, "Bot")
            print(msg)
            self.updateScore("Bot", scores["Bot"])
            self.changeCurrentDeal()
        elif self.currentDeal == 1:
            cutCard = self.currentDeck.botCut()
            scores, msg, = cribbage_scorer.cut_calc_score(cutCard, players, "Player")
            print(msg)
            self.updateScore("Player", scores["Player"])
            self.changeCurrentDeal()

        # check for victory condition
        if self.checkScore():
            return
        
        # starting main loop for round
        while len(playerHand) > 0 or len(botHand) > 0:
            currentCount = 0
            playedCards = []
            self.firstPlayer = ""
            print("COUNT IS SET TO 0\n")
            while currentCount <= 31:
                playerPlayable = []
                botPlayable = []

                # checking playable cards for player
                for card in playerHand:
                    # adjust value for face cards
                    if card[0] == 11 or card[0] == 12 or card[0] == 13:
                        tempValue = 10
                    else:
                        tempValue = card[0]
                    if currentCount + tempValue <= 31:
                        playerPlayable.append(card)

                # checking playable cards for bot
                for card in botHand:
                    if card[0] == 11 or card[0] == 12 or card[0] == 13:
                        tempValue = 10
                    else:
                        tempValue = card[0]
                    if currentCount + tempValue <= 31:
                        botPlayable.append(card)

                # break if no more playable cards
                if len(playerPlayable) == 0 and len(botPlayable) == 0:
                    break

                # play card in order based on turn, then update currentCount
                if self.currentDeal == 0:
                    playTemp1 = self.playHuman(playerHand, currentCount, playedCards)
                    currentCount = playTemp1[0]
                    playedCards = playTemp1[1]
                    playTemp2 = self.playBot(botHand, currentCount, playedCards)
                    currentCount = playTemp2[0]
                    playedCards = playTemp2[1]
                elif self.currentDeal == 1:
                    playTemp1 = self.playBot(botHand, currentCount, playedCards)
                    currentCount = playTemp1[0]
                    playedCards = playTemp1[1]
                    playTemp2 = self.playHuman(playerHand, currentCount, playedCards)
                    currentCount = playTemp2[0]
                    playedCards = playTemp2[1]
                print("THE CURRENT COUNT IS", currentCount)

            self.scorePlay(playedCards)
            if self.checkScore():
                return

        self.scoreShow(playerHandPerm, botHandPerm, currentCrib, cutCard)
        if self.checkScore():
            return

    # play a single card from player's hand
    def playHuman(self, playerHand, currentCount, playedCards):
        # set first player for scoring
        if len(playedCards) == 0:
            self.firstPlayer = "Player"

        print("PLAYER's TURN!")
        playerPlayable = []
        # checking playable cards again
        for card in playerHand:
            if card[0] == 11 or card[0] == 12 or card[0] == 13:
                        tempValue = 10
            else:
                        tempValue = card[0]
            if currentCount + tempValue <= 31:
                        playerPlayable.append(card)
        # end function if no playable cards
        if len(playerPlayable) == 0:
            self.changeCurrentDeal()
            print("Player has No Playable Cards!")
            return [currentCount, playedCards]

        # select card to be played
        print("Player's Hand:", playerHand)
        playedCard = self.player.playCard(playerPlayable, playedCards)
        playerHand.remove(playedCard)
        print("\nPlayer Played:", end='')
        self.currentDeck.showCard(playedCard)

        # adjust value for face cards
        if playedCard[0] == 11 or playedCard[0] == 12 or playedCard[0] == 13:
            tempCount = 10
        else:
            tempCount = playedCard[0]

        # append played card
        playedCards.append(playedCard)

        # update currentCount
        if currentCount + tempCount > 31:
            return [currentCount, playedCards]
        currentCount += tempCount
        print("Current Count:", currentCount, "\n")
        
        self.changeCurrentDeal()
        return [currentCount, playedCards]

    # play a single card from bot's hand
    def playBot(self, botHand, currentCount, playedCards):
        # set first player for scoring
        if len(playedCards) == 0:
            self.firstPlayer = "Bot"

        print("BOTS TURN!")
        botPlayable = []
        # checking playable cards again
        for card in botHand:
            if card[0] == 11 or card[0] == 12 or card[0] == 13:
                        tempValue = 10
            else:
                        tempValue = card[0]
            if currentCount + tempValue <= 31:
                        botPlayable.append(card)
        # end function if no playable cards
        if len(botPlayable) == 0:
            self.changeCurrentDeal()
            print("Bot Has No Playable Cards!")
            return [currentCount, playedCards]

        # select card to be played
        # print("Bot Hand:", botHand)
        playedCard = self.bot.playCard(botPlayable, playedCards)
        botHand.remove(playedCard)
        print("\nBot Played:", end='')
        self.currentDeck.showCard(playedCard)

        # adjust value for face cards
        if playedCard[0] == 11 or playedCard[0] == 12 or playedCard[0] == 13:
            tempCount = 10
        else:
            tempCount = playedCard[0]

        # append played card
        playedCards.append(playedCard)

        # update currentCount
        if currentCount + tempCount > 31:
            return [currentCount, playedCards]
        currentCount += tempCount
        print("Current Count:", currentCount, "\n")

        self.changeCurrentDeal()
        return [currentCount, playedCards]

    # handles scoring for each set of the play phase of the round
    def scorePlay(self, playedCards):
        print("\nNOW SCORING SET")
        # check for first player
        if self.firstPlayer == "Player":
            players = ["Player", "Bot"]
        elif self.firstPlayer == "Bot":
            players = ["Bot", "Player"]

        scores, currentCount, play_log = cribbage_scorer.play_calc_score_set(playedCards, players)
        print("Current Count is:", currentCount)
        print(play_log)
        # updates scores and check victory condition
        self.updateScore(players[0], scores[players[0]])
        if self.checkScore():
            return
        self.updateScore(players[1], scores[players[1]])
        if self.checkScore():
            return

    # handles scoring for the show phase of the round
    def scoreShow(self, playerHand, botHand, currentCrib, cutCard):
        print("\nNOW SCORING ROUND")
        crib = True

        if self.currentDeal == 0:
            score, msg = cribbage_scorer.show_calc_score(cutCard, playerHand, crib)
            print("SCORING PLAYER'S HAND")
            print(msg)
            self.updateScore("Player", score)
            if self.checkScore():
                return

            score, msg = cribbage_scorer.show_calc_score(cutCard, botHand, crib)
            print("SCORING BOT'S HAND")
            print(msg)
            self.updateScore("Bot", score)
            if self.checkScore():
                return

        elif self.currentDeal == 1:
            score, msg = cribbage_scorer.show_calc_score(cutCard, botHand, crib)
            print("SCORING BOT'S HAND")
            print(msg)
            self.updateScore("Bot", score)
            if self.checkScore():
                return
            
            score, msg = cribbage_scorer.show_calc_score(cutCard, playerHand, crib)
            print("SCORING PLAYER'S HAND")
            print(msg)
            self.updateScore("Player", score)
            if self.checkScore():
                return

        if self.currentDeal == 0:
            score, msg = cribbage_scorer.show_calc_score(cutCard, currentCrib, crib)
            print("SCORING THE CRIB")
            print(msg)
            self.updateScore("Player", score)
        elif self.currentDeal == 1:
            score, msg = cribbage_scorer.show_calc_score(cutCard, currentCrib, crib)
            print("SCORING THE CRIB")
            print(msg)
            self.updateScore("Bot", score)
        if self.checkScore():
            return
        

    # prints current score
    def printScore(self):
        print("--Current Score--")
        print("Player:", self.playerScore, " Bot:", self.botScore, "\n")

    # checks current score for victory condition
    def checkScore(self):
        if self.playerScore >= 121:
            self.printScore()
            print("GAME OVER! Player Wins!")
            self.winner = 1
            return True
        if self.botScore >= 121:
            self.printScore()
            print("GAME OVER! Bot Wins!")
            self.winner = 0
            return True
        return False

    # updates player/bot scores
    def updateScore(self, user, points):
        if points == 11 or points == 12 or points == 13:
            points = 10
        if user == "Player":
            self.playerScore += points
            self.printScore()
        elif user == "Bot":
            self.botScore += points
            self.printScore()
        else:
            pass

    # updates which player's turn it is
    def changeCurrentDeal(self):
        if self.currentDeal == 0:
            self.currentDeal = 1
        elif self.currentDeal == 1:
            self.currentDeal = 0


# Disable print output
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore print output
def enablePrint():
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    # result = test.game()
    # print(result)
    playerWins = 0
    n = 0
    avgScoreDif = 0
    numberGames = 10
    # blockPrint()
    while n < numberGames:
        test = Cribbage()
        result = test.game()
        if result == 1:
            playerWins += 1
        avgScoreDif += test.playerScore - test.botScore
        n += 1
    avgScoreDif /= numberGames
    # enablePrint()
    print("Human Wins:", playerWins)
    print("Bot Wins:", numberGames-playerWins)
    print("Average Score Difference:", avgScoreDif, "(in Bot favor)")