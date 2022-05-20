<p align="center">
  <img width="200" src="img\LOGO_v1.png" alt="Game of Matches logo">
</p>
<h1 align="center">Game of Matches</h1>

Program that allows the user to play (via a TKinter graphical interface) the game of matches.
Four modes are available: Player vs. Player, Player vs. Computer (random), Player vs. Computer (algorithmic) and Computer vs. Computer (random).

- [Principle of the game](https://github.com/4strium/Game-of-Matches#principle-of-the-game)
- [Games Modes](https://github.com/4strium/Game-of-Matches#games-modes-)
    - [Player vs. Player](https://github.com/4strium/Game-of-Matches#player-vs-player-)
    - [Player vs. Computer (random)](https://github.com/4strium/Game-of-Matches#player-vs-computer-random-)
    - [Player vs. Computer (algorithmic)](https://github.com/4strium/Game-of-Matches#player-vs-computer-algorithmic-)
    - [Computer vs. Computer (random)](https://github.com/4strium/Game-of-Matches#computer-vs-computer-random-)
- [Technologies used](https://github.com/4strium/Game-of-Matches#technologies-used-)
- [Downloads](https://github.com/4strium/Game-of-Matches#downloads-)

## Principle of the game :
The principle of the game is quite simple, it's a two-player game, initially there are 21 matches which are laid out on a table.
In turn, you will have to remove one, two or three matches.
BUT BE CAREFUL, whoever removes the last match from the table loses!
It's up to you to develop the best strategy to win!

In case of problems, you can directly access the rules of the game in the home page of the game:
<p align="center">
  <img width="200" src="img\docs\game_rules.PNG" alt="Image button of game rules">
</p>

## Games Modes :
The game offers several different game modes whether you are alone or two:
- ### Player vs. Player :
You can take turns playing with a friend! The first player will be "Player 1" and the second "Player 2".
- ### Player vs. Computer (random) :
This is the game mode that starts if you select the player vs computer mode with the easy difficulty. The robot takes matches randomly (with [random](https://docs.python.org/3/library/random.html) module) until there are only 3 or less left, to prevent it from playing "crazy"
- ### Player vs. Computer (algorithmic) :
This is the game mode that starts if you select the player vs computer mode with the hard difficulty. The robot here picks matches algorithmically, and logically. Here is the logic code:
```python
if nb_allumettes % 4 == 3:                  # Here unlike the simple difficulty, I algorithmically determine the number of matches that the robot must take to be sure to win!
            nb_robot = 2
        elif nb_allumettes % 4 == 2:
            nb_robot = 1
        elif nb_allumettes % 4 == 0:
            nb_robot = 3
        else:
            nb_robot = 1
        if nb_allumettes == 1 :
            messagebox.showinfo("Won ! :)","The robot is forced to take the last match, well done!")
            msg_remerciment()
        canvas.after(3000, suppr_allum_robot_difficile, nb_robot, canvas, root_correspondant)             # This function allows you to execute the "suppr_allum_robot_simple()" function seen just above after 3000ms and with my number which has just been determined, as an argument.
```
- ### Computer vs. Computer (random) :


## Technologies used :
I use two very useful and functional modules:
- [Random](https://docs.python.org/3/library/random.html)
to completely randomly generate the number of matches taken by the computers.
- [TKinter](https://docs.python.org/fr/3/library/tk.html)
to create the full GUI! All actions with buttons, animations,...
- [PYinstaller](https://pyinstaller.org/en/stable/)
to compact all the external files in the same executable file, this module also allows to run any python program (even with dependencies) on any machine!
- [NSIS](https://nsis.sourceforge.io/Main_Page) 
to build a simple and efficient installer.

## Downloads :
You can access the different versions of the game and download them on the page dedicated to [releases.](https://github.com/4strium/Game-of-Matches/releases)
|                |Description                         |Changes                         |Release date                        |
|----------------|-------------------------------|-----------------------------|-----------------------------|
|[v1.0.0](https://github.com/4strium/Game-of-Matches/releases/tag/v1.0.0)|`Initial version`            |...            |Released at 15-05-2022|


## Licence :
Licensed under the [GNU General Public License v3.0](https://github.com/4strium/Game-of-Matches/blob/main/LICENSE)
