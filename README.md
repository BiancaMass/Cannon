# Cannon
## About
This directory contains the final project for the class Intelligent Search and Games, 2021. <br/>
Maastricht University, Department of Data Science and Knowledge Engineering.<br/>
Master in Data Science for Decision Making.<br/>

Author: Bianca M. Massacci

## Compiling 
The repository contains the game "Cannon"
To play the game, run the file main.py

To change the player that the AI plays, go to main.py lines 52-61.

## Dependencies<br/>
- pygame                    2.0.1<br/>
- python                    3.8.11<br/>
- sqlite                    3.36.0<br/>
- tk                        8.6.11<br/>

## TODOs
This implementation is still work in progress. Currently missing:
### Game rules
- Cannon detection (currently incomplete)
- Cannon move
- Cannon shooting
- Winning condition missing: when opponent has no legal moves

### AI
- Place tower autonomously
- Alpha-beta pruning for speed
- Transposition table and hash mapping

### Playability
- Numeric labels on the sides
- Better aesthethics
- Print out of AI chosen moves

### Improvements
- Evaluation function
- Testing


## Sources:

[1] Ruscica, T. (2020, September 3). Python-Checkers-AI. [GitHub Repository]. https://github.com/techwithtim/Python-Checkers-AI <br/>
[2] Ruscica, T. [Tech with Tim]. (2020, September 28). Python checkers AI tutorial part 2 - implementation & visualization (minimax). [Video]. YouTube https://www.youtube.com/watch?v=mYbrH1Cl3nw <br/>
[3] Ruscica, T. [Tech with Tim]. (2020, September 5). Python/Pygame checkers tutorial (part 1) - drawing the board. [Video]. YouTube. https://www.youtube.com/watch?v=vnd3RfeG3NM <br/>
[4] Ruscica, T. [Tech with Tim]. (2020, September 9). Python/Pygame checkers tutorial (part 2) - pieces and movement. [Video]. YouTube. https://www.youtube.com/watch?v=LSYj8GZMjWY <br/>
[5] Ruscica, T. [Tech with Tim]. (2020, September 12).  Python/Pygame checkers tutorial (part 3) - jumping and king movement. [Video]. YouTube. https://www.youtube.com/watch?v=_kOXGzkbnps <br/>
[6] Cannon rules: https://www.iggamecenter.com/info/en/cannon.html <br/>
