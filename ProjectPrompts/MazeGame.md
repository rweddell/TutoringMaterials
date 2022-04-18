# WORK IN PROGRESS

# Maze Game

Write a program that will create a square maze of rooms that a user will navigate through in order to exit
The program will be text-based that will present the user with up to 4 choices when entering a room:
    - Back
    - Left
    - Right
    - Forward
'Back' should always be available because the user might reach a dead-end
The maze should be a squar grid made up of rooms
Each room can be connected to up to four adjacent rooms, but must be connected to at least one
The beginning of the maze should be at grid square (0,0), and the end should be at grid square (maze_height, maze_width)

Start by creating a 'Room' class with attributes to show what other rooms it is connected to.
Next create a 'Maze' class that has a grid of rooms, a 'start', and an 'end'.
Then create logic that allows a user to move through the maze.

Keep in mind that back, left, right, and forward are conceptual and might take the form of 'up', 'down', 'left', and 'right' or some other directionality.

