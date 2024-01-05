TASK 1:

This Python script is made to generate stack-realizable permutations, a type of permutation that can be achieved by repeatedly performing two operations: pushing elements onto a stack and popping elements from it.

HOW TO USE THE SCRIPT:
1. To run the script, open your command prompt or terminal and execute the following command:
2. You will be prompted to enter a string of numbers separated by commas. These numbers should follow specific rules:
- Ensure that there are no repeated numbers in your input.
- The numbers should be in ascending order, starting from 1. For example: 1, 2, 3, and so on.

CODE BREAKDOWN:

> INPUT:
- The script starts by asking you to provide a list of numbers. The format of this input is important, as it dictates the types of permutations that can be generated.
- The script performs one check on your input:
 - Repeated Elements: It looks for and alerts you to any numbers that appear more than once.

> PERMUTATION GENERATION:
- Once your input is confirmed to be valid, the script employs a method to generate stack-realizable permutations. These are permutations that can be achieved through the push and pop operations on a stack-like structure.

> OUTPUT:
- The script then displays the stack-realizable permutations it has created.
- It provides you with the total count of these achievable permutations.

################################################################################################################

TASK 2:

Maze Solver - README

This Python script is designed to find the shortest path in a maze from a given source to a destination. It uses a Breadth-First Search (BFS) approach to solve the maze.
How to Use the Script:
     Execute the script by running it with Python using the following command in your terminal:

    python Task2.py
    The script will guide you through the process by asking for specific inputs.

Code Explanation:

    Input:
    First, you will provide the size of the square maze, specifying the number of rows and columns.

    Then, you'll input the source and destination coordinates in the format of (row, column).

    You'll be asked to input the maze grid. For the grid:
        Use 0 to represent open paths.
        Use 1 to indicate obstacles.
        

    Output:

    If the destination is unreachable from the source, the script will print "The destination is unreachable from the source."

    If a path is found, the script will display:
        The shortest path length from the source to the destination.
        The possible paths as a sequence of coordinates.

    The script checks if source and destination coordinates are within the maze bounds. If not, it will generate an error.

Code Flow:

The script starts by taking the maze input from the user and reversing it to create the maze.
It then validates the source and destination coordinates to ensure they are within bounds.
Using BFS, it explores the maze to find the shortest path, tracking the visited cells and their distances.
If the destination is reachable, the script prints the shortest path length and the path itself.
