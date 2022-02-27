import numpy as np
import copy
from collections import defaultdict
from Cards import Deck
from random import randrange
import scorermod
class MCTSNode():

	def __init__(self, state, parent = None, parentAction = None):
		#represents round state
		self.state = state
		#None when its the root node, and for other nodes its = to node it came from
		self.parent = parent
		#none for root node, other nodes its equal to the action which the parent did, aka
		#which card was placed
		self.parentAction = parentAction
		#possible actions from current node, aka what cards left in hand to play
		self.children = []
		#number of times this node is visited
		self.numVisits = 0
		self.results = defaultdict(int)
		#PURPOSE OF BELOW??
		self.results[1] = 0
		self.results[-1] = 0
		#PURPOSE OF ABOVE??
		#list of all possible actions
		self.notExploredActions1 = None
		self.notExploredActions1 = self.notExploredActions()
		return

	def notExploredActions(self):
		self.notExploredActions1 = self.state.getPossibleActions()
		return self.notExploredActions1

	def differenceOfWinsLoss(self):
		#self.results[1] represents wins
		#self.results[-1] represents losses
		return self.results[1] - self.results[-1]

	def numNodeVisits(self):
		return self.numVisits

	def expand(self):
		action = self.notExploredActions1.pop()
		# next_state = self.state.move(action)
		nextState = self.state.takeAction(action)
		childNode = MCTSNode(nextState, parent = self, parentAction = action)
		self.children.append(childNode)
		return childNode

	def isTerminalNode(self):
		return self.state.isTerminal()

	def simulation(self):
		currentSimulationState = self.state

		while not currentSimulationState.isTerminal():
			possibleMoves = currentSimulationState.getPossibleActions()
			action = self.simulationPolicy(possibleMoves)
			currentSimulationState = currentSimulationState.takeAction(action)

		return currentSimulationState.gameResult()

	def backpropagate(self, result):
		self.numVisits += 1
		self.results[result] += 1
		if self.parent:
			self.parent.backpropagate(result)


	def ifFullyExpanded(self):
		return len(self.notExploredActions1) == 0

	def bestChild(self, cParam = 0):
		choicesWeights = [(c.differenceOfWinsLoss() / c.numNodeVisits()) + cParam * np.sqrt((2 * np.log(self.numNodeVisits() / c.numNodeVisits()))) for c in self.children]
		return self.children[np.argmax(choicesWeights)]

	def simulationPolicy(self, possibleActions):
		return possibleActions[np.random.randint(len(possibleActions))]

	def treePolicy(self):
		currentNode = self
		while not currentNode.isTerminalNode():
			if not currentNode.ifFullyExpanded():
				return currentNode.expand()
			else:
				currentNode = currentNode.bestChild()
		return currentNode

	def bestAction(self):
		simulationNum = 100

		for i in range(simulationNum):
			v = self.treePolicy()
			reward = v.simulation()
			v.backpropagate(reward)
		return self.bestChild(cParam = 0)


class State():
	def __init__(self):
		pass

	def getPossibleActions(self, botHand):
		# returns iterable of all actions from currentState
		# doesn't do anything with actions, just shows which ones are possible 
	    actionsPossible = []
	    for card in range(len(botHand)):
	        if not self.isTerminal():
	            actionsPossible.append(card)
	    return actionsPossible 

	# variables it needs: botHand, playerHand, pileSum, currentCardsPlayed
	def isTerminal(self):
		# returns boolean 
		# terminal state is one of the following:
  		# one of the players is forced to say 'Go'
	    # pile reaches exactly 31
	    # both players run out of cards 
	    # temp = []
	    # for card in (botHand):
	    #     if (pileSum) + card > 31:
	    #         temp.append(True)
	    #     else:
	    #         temp.append(False)
	    # if (botHand) == None and (playerHand) == None:
	    #     return True 
	    # elif (pileSum) + (currentCardsPlayed) == 31:
	    #     return True 
	    # elif temp.count(False) == 0:
	    #     return True
	    # else: 
	    #     return False
		return False

	# TODO: generates reward for a given terminal state
	def getReward(self):
		return False
			

	def takeAction(self):
		# input action is selected based on isTerminal() and getReward(card)
		# we want the action that results in isTerminal() returning true and getReward(card) being maximized 
		# then it returns the next state after the action is taken
		newState = copy.deepcopy(self)
		possibleRewards = []
		possibleActions = self.getPossibleActions(self)
		for card in range(len(possibleActions)):
		    if not self.isTerminal():
		        possibleRewards.append(self.getReward())
		    else:
		        possibleRewards.append(0)
		# next state based on which action was taken
		newState = self.takeAction() 
		return newState

	def gameResult(self):
		pass


