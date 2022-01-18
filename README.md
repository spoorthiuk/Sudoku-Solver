# Sudoku Solver

Sudoku is a logic based puzzle. The puzzle consists of a 9x9 grid broken down into sub grids of size 3x3. The obective is to fill the grid with numbers from 1-9 such that there are no repeating digit in a row, column or in a sub grid.

Even though solving the puzzle on your own is really fun. Sometimes getting at the solution could be really hard.

The first version of the code is a backtracking solution to  a given valid sudoku puzzle. The algorithm takes more time to solve as the number of blank spaces in the grid increases.

Following is the puzzle hardcoded in the program for testing

![41586_2012_Article_BFnature20129751_Figa_HTML](https://user-images.githubusercontent.com/43513525/149981460-6de5470b-22e1-4165-b309-e7b0810888ee.jpg)

And the following is the solution given by the algorithm

![image](https://user-images.githubusercontent.com/43513525/149981796-6905f509-a912-47c0-a44f-15e9480cfc67.png)

The puzzle is given as an input as a 2D matrix where the blank spaces are represented with 0s. 

Open CV could be used to read the puzzle on paper or an image and to solve it.
