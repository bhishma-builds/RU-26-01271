 # Maze Escape Game 

A console-based maze game in Python 3. The player moves through a 5x5 maze using W/A/S/D keys and must reach the exit. Walls block movement, and the program can also find the shortest path from start to exit using BFS (Breadth-First Search).

**Concepts used:** 2D Lists, Algorithms (BFS), Movement logic

## Maze

```
P . . # #
# # . # #
# . . . #
# . # # #
# . . . E
```

`#` = wall, `.` = path, `P` = start (row 0, col 0), `E` = exit (row 4, col 4)

## Features

- Maze stored as a 2D list and printed after every valid move with the player's position
- Move with W/A/S/D (case-insensitive); multiple moves can be entered together, separated by commas (e.g. `D, D, S`)
- Moves into walls or outside the maze are blocked and not counted
- Invalid keys show an error and are not counted
- Winning message with total moves when the player reaches `E`
- BFS finds and displays the shortest path length from start to exit


Menu:

1. Play Maze Game
2. Shortest path
3. Exit

## Algorithm: Shortest Path (BFS)

1. Start from (0, 0) with distance 0 and add it to the queue.
2. Remove the first cell from the queue and try all 4 directions (up, down, left, right).
3. Skip cells that are outside the maze, walls, or already visited.
4. Add each new cell to the queue with distance + 1.
5. When the exit (4, 4) is reached, return its distance. If the queue empties, return -1 (no path).

BFS explores cells level by level, so the first time it reaches the exit is guaranteed to be the shortest path.
