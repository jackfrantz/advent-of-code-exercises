import marimo

__generated_with = "0.11.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        #Day 10: Pipe Maze
        You use the hang glider to ride the hot air from Desert Island all the way up to the floating metal island. This island is surprisingly cold and there definitely aren't any thermals to glide on, so you leave your hang glider behind.

        You wander around for a while, but you don't find any people or animals. However, you do occasionally find signposts labeled "Hot Springs" pointing in a seemingly consistent direction; maybe you can find someone at the hot springs and ask them where the desert-machine parts are made.

        The landscape here is alien; even the flowers and trees are made of metal. As you stop to admire some metal grass, you notice something metallic scurry away in your peripheral vision and jump into a big pipe! It didn't look like any animal you've ever seen; if you want a better look, you'll need to get ahead of it.

        Scanning the area, you discover that the entire field you're standing on is densely packed with pipes; it was hard to tell at first because they're the same metallic silver color as the "ground". You make a quick sketch of all of the surface pipes you can see (your puzzle input).

        The pipes are arranged in a two-dimensional grid of tiles:

        `|` is a **vertical pipe** connecting north and south.<br>
        `-` is a **horizontal pipe** connecting east and west.<br>
        `L` is a **90-degree bend** connecting north and east.<br>
        `J` is a **90-degree bend** connecting north and west.<br>
        `7` is a **90-degree bend** connecting south and west.<br>
        `F` is a **90-degree bend** connecting south and east.<br>
        `.` is **ground**; there is no pipe in this tile.<br>
        `S` is the **starting position** of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.<br>
        Based on the acoustics of the animal's scurrying, you're confident the pipe that contains the animal is **one large, continuous loop**.

        For example, here is a square loop of pipe:
        ```
        .....
        .F-7.
        .|.|.
        .L-J.
        .....
        ```
        If the animal had entered this loop in the northwest corner, the sketch would instead look like this:
        ```
        .....
        .S-7.
        .|.|.
        .L-J.
        .....
        ```
        In the above diagram, the S tile is still a 90-degree F bend: you can tell because of how the adjacent pipes connect to it.

        Unfortunately, there are also many pipes that **aren't connected to the loop**! This sketch shows the same loop as above:
        ```
        -L|F7
        7S-7|
        L|7||
        -L-J|
        L|-JF
        ```
        In the above diagram, you can still figure out which pipes form the main loop: they're the ones connected to `S`, pipes those pipes connect to, pipes **those** pipes connect to, and so on. Every pipe in the main loop connects to its two neighbors (including `S`, which will have exactly two pipes connecting to it, and which is assumed to connect back to those two pipes).

        Here is a sketch that contains a slightly more complex main loop:
        ```
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...
        ```
        Here's the same example sketch with the extra, non-main-loop pipe tiles also shown:
        ```
        7-F7-
        .FJ|7
        SJLL7
        |F--J
        LJ.LJ
        ```
        If you want to **get out ahead of the animal**, you should find the tile in the loop that is **farthest** from the starting position. Because the animal is in the pipe, it doesn't make sense to measure this by direct distance. Instead, you need to find the tile that would take the longest number of steps **along the loop** to reach from the starting point - regardless of which way around the loop the animal went.

        In the first example with the square loop:
        ```
        .....
        .S-7.
        .|.|.
        .L-J.
        .....
        ```
        You can count the distance each tile in the loop is from the starting point like this:
        ```
        .....
        .012.
        .1.3.
        .234.
        .....
        ```
        In this example, the farthest point from the start is `4` steps away.

        Here's the more complex loop again:
        ```
        ..F7.
        .FJ|.
        SJ.L7
        |F--J
        LJ...
        ```
        Here are the distances for each tile on that loop:
        ```
        ..45.
        .236.
        01.78
        14567
        23...
        ```
        Find the single giant loop starting at `S`. **How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?**
        """
    )
    return


@app.cell
def _():
    simple = '''.....
    .S-7.
    .|.|.
    .L-J.
    .....'''
    print(simple)

    print('*'*10)

    complex = '''7-F7-
    .FJ|7
    SJLL7
    |F--J
    LJ.LJ'''
    print(complex)
    return complex, simple


@app.cell
def _(np, simple):
    simple_grid = np.array([list(line) for line in simple.splitlines()])
    print(simple_grid)
    return (simple_grid,)


@app.cell
def _(np, simple_grid):
    samp_start_row, samp_start_col = np.where(simple_grid=='S')[0][0], np.where(simple_grid=='S')[1][0]
    print(f'North is: {simple_grid[samp_start_row-1][samp_start_col]}')
    print(f'East is: {simple_grid[samp_start_row][samp_start_col+1]}')
    print(f'South is: {simple_grid[samp_start_row+1][samp_start_col]}')
    print(f'West is: {simple_grid[samp_start_row][samp_start_col-1]}')
    return samp_start_col, samp_start_row


@app.cell
def _(find_next_pipe, np, simple, start_path):
    def find_path(pipes):
        # turn grid into array
        grid = np.array([list(line) for line in pipes.splitlines()])
        # find starting position
        s_row, s_col = np.where(grid=='S')[0][0], np.where(grid=='S')[1][0]
        #print(s_row)
        #print(s_col)
        # list to add path
        path = []
        # Find connecting pipe
        pipe, row, col, source = start_path(s_row, s_col, grid)
        path.append((row, col))
        while (row, col) != (s_row, s_col):
            pipe, row, col, source = find_next_pipe(pipe, row, col, source, grid)
            path.append((row, col))
            #print(path)
        midpoint = int((len(path)/2))
        #print(midpoint)
        return midpoint


    find_path(simple)
    return (find_path,)


@app.cell
def _(complex, find_path):
    find_path(complex)
    return


@app.cell
def _(find_path):
    day10 = open('./data/day10.txt').read()
    day10
    find_path(day10)
    return (day10,)


@app.cell
def _(samp_start_col, samp_start_row, simple_grid):
    def start_path(row, col, grid):
        pipes = ['|', '-', 'L', 'F', 'J', '7']
        if grid[row-1][col] in ['|', 'F', '7']:
            pipe, row, col = grid[row-1][col], row-1, col
            source = 'south'
            print(f'North is: {grid[row-1][col]}')
        elif grid[row][col+1] in ['-', 'J', '7']:
            pipe, row, col = grid[row][col+1], row, col+1
            source = 'west'
            print(f'East is: {grid[row][col+1]}')
        elif grid[row+1][col] in ['|', 'L', 'J']:
            pipe, row, col = grid[row+1][col], row+1, col
            source = 'north'
            print(f'South is: {grid[row+1][col]}')
        elif grid[row][col-1] in ['-', 'L', 'F']:
            pipe, row, col = grid[row][col-1], row, col+1
            source = 'east'
            print(f'West is: {grid[row][col-1]}')
        return pipe, row, col, source

    start_path(samp_start_row, samp_start_col, simple_grid)
    start_path(1, 1, simple_grid)
    return (start_path,)


@app.cell
def _(samp_start_col, samp_start_row, simple_grid, start_path):
    def find_next_pipe(pipe, row, col, source, grid):
        if pipe == '|' and source == 'north':
            pipe, row, col, source = grid[row+1][col], row+1, col, 'north'
        elif pipe == '|' and source == 'south':
            pipe, row, col, source = grid[row-1][col], row-1, col, 'south'
        elif pipe == '-' and source == 'east':
            pipe, row, col, source = grid[row][col-1], row, col-1, 'east'
        elif pipe == '-' and source == 'west':
            pipe, row, col, source = grid[row][col+1], row, col+1, 'west'
        elif pipe == 'L' and source == 'north':
            pipe, row, col, source = grid[row][col+1], row, col+1, 'west'
        elif pipe == 'L' and source == 'east':
            pipe, row, col, source = grid[row-1][col], row-1, col, 'south'
        elif pipe == 'F' and source == 'east':
            pipe, row, col, source = grid[row+1][col], row+1, col, 'north'
        elif pipe == 'F' and source == 'south':
            pipe, row, col, source = grid[row][col+1], row, col+1, 'west'
        elif pipe == 'J' and source == 'west':
            pipe, row, col, source = grid[row-1][col], row-1, col, 'south'
        elif pipe == 'J' and source == 'north':
            pipe, row, col, source = grid[row][col-1], row, col-1, 'east'
        elif pipe == '7' and source == 'west':
            pipe, row, col, source = grid[row+1][col], row+1, col, 'north'
        elif pipe == '7' and source == 'south':
            pipe, row, col, source = grid[row][col-1], row, col-1, 'east'
        else:
            print('broken')
        return pipe, row, col, source

    print(start_path(samp_start_row, samp_start_col, simple_grid))
    _pipe, _row, _col, _source = start_path(samp_start_row, samp_start_col, simple_grid)
    print(_pipe, _row, _col, _source)
    print(find_next_pipe(_pipe, _row, _col, _source, simple_grid))
    #_pipe, _row, _col, _source = find_next_pipe(_pipe, _row, _col, _source, simple_grid)
    #_pipe, _row, _col, _source
    return (find_next_pipe,)


@app.cell
def _(day10, np, start_path):
    day10_grid = np.array([list(line) for line in day10.splitlines()])
    day10_grid
    print(np.where(day10_grid=='S')[0][0], np.where(day10_grid=='S')[1][0])
    s_row, s_col = np.where(day10_grid=='S')[0][0], np.where(day10_grid=='S')[1][0]
    print(s_row, s_col)
    start_path(s_row, s_col, day10_grid)
    return day10_grid, s_col, s_row


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
