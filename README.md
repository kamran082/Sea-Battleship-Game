# Sea Battleship

Sea Battleship is a python terminal game, which runs in the code institute mock terminal on Heroku.
It,s single player game, player needs to find two ships on board. And sunk them, before finish bullets.

# How to play

Sea Battleship is based on the classis pen-and-paper game. You can read more about it on Wikipedia.
In this version, a board randomly generated. The player need to guess ships on boards. Guesses are
marked on (-) . Hits are indicated by (X).
The player challenge is to sunk all ships before finish all bullets.

# Screenshots & Features

1. A random board generated.
2. Ships are randomly placed on board.
3. player cannot see where the ships are.

![CI logo](../Sea-Battleship-Game/images/1.png)



1. Player guess between 0-3.
2. If you miss, or Hit boards will show you the message.
3. Board will show howmany bullets and ships left.

![CI logo](../Sea-Battleship-Game/images/2.png)


1. You can not enter number outside the grid.
2. You can not enter a word or letter.
3. you can not enter same guess twice.

![CI logo](../Sea-Battleship-Game/images/3.png)

# Data Model
I used 2D array Model.

# Testing

I have manually tested this project by doing the folling:
1. passed the code throught a PEP8 linter and confirmed ther are no problems.
2. Given invalid inputs, strings when numbers are expected, same input twice.

# Bugs.
#Solved Bugs:

 when i wrote the project i was getting white line spacing, which i fixed it by change the setting in gitpod.

# Remaining Bugs.
#No bugs remaining.

# Deployment
This project was deployed using code institute mock terminal for Heroku.

#Steps for Deployment:

1. Fore or clone this repository
2. Create a new Heroku app
3. Set the buildbacks to python and node js in the order
4. Link the Heroku app to the repository
5. Click on Deploy.

# Credits
1. Code institute for the deployment terminal
2. Wikipedia for the details of the Battleship game.
