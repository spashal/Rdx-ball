# Rdx-ball
## About
This is a single player game where the user had to control the paddle and thereby control the ball. The ball is supposed to break bricks that earns you points. You would like to accumulate most points.

## Dynamics of Rdx Ball

### Features of the game are
- The user can only control the paddle
- The ball follows a certain speed change on hitting the paddle
- The ball hits a brick to score points related to the brick
- The brick on collision with the ball shall change into a weaker brick and subsequently get completely destroyed
- Color of a brick represents its strength and special attributes
    * Red - Weakest Brick (1 point)
    * Dark Green - Medium Strength (2 points)
    * Pink - Strongest Breakable brick (3 points)
    * Sky Blue - Unbreakable Bricks (4 points)
    * Yellow - Chain Reacting bricks (5 points)
    * Bright Red - Bomber Bricks (6 points)
- There are certain power ups that fall when you break a brick
    * Expand - <kbd>E</kbd> - Expands paddle
    * Shrink - <kbd>S</kbd> - Shrinks paddle
    * Thru Ball - <kbd>T</kbd> - Ball passes through bricks even after destroying them
    * Fast Ball - <kbd>F</kbd> - Increases the speed of the ball
    * Grab - <kbd>G</kbd> - User can grab the ball and release it again at their own will
    * Multiply - <kbd>M</kbd> - Single ball changes to multiple balls suddenly

### How to play
- <kbd>A</kbd> - move the paddle left
- <kbd>D</kbd> - move the paddle right
- <kbd>space</kbd> - release the ball from paddle whenever you can
- <kbd>Q</kbd> - Quit the game

## How to run the game
* pip3 install colorama
* pip3 install numpy
* python game.py