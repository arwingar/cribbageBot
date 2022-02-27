# cribbageBot
A bot capable of playing and beating humans in the game of cribbage.

The codebase requires the falling package to be able to run:</br> numpy, more-itertools, and cribbage-scorer.
</br>If you do not already have these packages installed on your machine, they can be installed with the following commands:</br>
</br>*pip install numpy
</br>pip install more-itertools
</br>pip install cribbage-scorer*
</br></br> In order to run the game, simply execute the game.py file after you have installed the above packages.
</br>FILE DESCRIPTIONS:
</br>1. game.py holds the logic and instructions for the primary game loop, including initialization, starting a new game, starting a new round, dealing out cards, and scoring the game at each phase.
</br>2. Cards.py contains all functions for managing the deck, as well as the cards within the deck. It includes functions that cut the deck for humans and bots, remove cards, display cards, deal a new hand, and more.
</br>3. randbot.py is a bot player that makes purely random decisions.
</br>4. bot.py is a bot player that makes decisions based on a greedy full search that considers the guaranteed score of a decision. More detail on this algorithm can be found in our report.
</br>5. player.py is a human player class that takes inputs in the terminal from the user in order to make decisions.
</br>6. scorermod.py is a modified version of the cribbage-scorer library that we needed in order to use the scoring functions in more diverse ways, allowing us to score partial rounds easily. The only change between the two is that this file does not account for the starter card.
</br>7. mcts.py is our *incomplete* attempt at implementing the Monte Carlo Tree Search algorithm. This file does not function, and is currently not in use by the rest of the code base. More detail on this algorithm can be found in our report.
