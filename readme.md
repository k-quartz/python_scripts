### This Repository has python scripts in separate branch. Check out particular branch.

# Branch Name:**maze_game_textual**

## Desription : This is a textual maze game.
Input is of the form 
X by Y. It is not compulsory to be in square maze.

On executing the script you will get below screen.

Enter No of Cols<br>
Enter No of Rows<br>

*** Enter Value of the maze : (Value can be any of the below)
1. 0-9 behaves like a portal. If value is 1 it can cross 1 X walls. If value is 2 it can cross 2 X walls. Input will be like
        1X1 or 2XX2 or 3XXX3.<br>
2. O (Capital O, not zero)<br>
3. X behaves like a wall<br> ***


sample input maze<br>
O X X X 2<br>
O 1 X 1 O<br>
X X X X O<br>
2 X X O O<br>


Output from above maze should be:<br>
. X X X 2<br>
. . X . .<br>
X X X X .<br>
2 X X O .<br>

