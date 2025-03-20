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
        # Day 11: Cosmic Expansion
        You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.

        He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.

        Maybe you can help him with the analysis to speed things up?

        The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

        ```
        ...#......
        .......#..
        #.........
        ..........
        ......#...
        .#........
        .........#
        ..........
        .......#..
        #...#.....
        ```

        The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

        Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

        In the above example, three columns and two rows contain no galaxies:

        ```
           v  v  v
         ...#......
         .......#..
         #.........
        >..........<
         ......#...
         .#........
         .........#
        >..........<
         .......#..
         #...#.....
           ^  ^  ^
        ```

        These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

        ```
        ....#........
        .........#...
        #............
        .............
        .............
        ........#....
        .#...........
        ............#
        .............
        .............
        .........#...
        #....#.......
        ```

        Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

        ```
        ....1........
        .........2...
        3............
        .............
        .............
        ........4....
        .5...........
        ............6
        .............
        .............
        .........7...
        8....9.......
        ```

        In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

        For example, here is one of the shortest paths between galaxies 5 and 9:

        ```
        ....1........
        .........2...
        3............
        .............
        .............
        ........4....
        .5...........
        .##.........6
        ..##.........
        ...##........
        ....##...7...
        8....9.......
        ```

        This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

        Between galaxy 1 and galaxy 7: 15
        Between galaxy 3 and galaxy 6: 17
        Between galaxy 8 and galaxy 9: 5
        In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

        Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
        """
    )
    return


@app.cell
def _():
    sample = '''...#......
    .......#..
    #.........
    ..........
    ......#...
    .#........
    .........#
    ..........
    .......#..
    #...#.....'''
    return (sample,)


@app.cell
def _(np, sample):
    sample_lines = sample.splitlines()
    sample_grid = np.array([list(line) for line in sample_lines])
    print(sample_grid)

    def add_rows(grid):
        empty_rows = np.where(np.all(grid == '.', axis=1))[0]
        for i, row in enumerate(empty_rows):
            new_row = np.array(['.'] * grid.shape[1])
            grid = np.insert(grid, row+i, new_row, axis=0)
            print(f'new row at {row+i}')
        return grid

    add_rows(sample_grid)
    return add_rows, sample_grid, sample_lines


@app.cell
def _(np, sample_grid):
    empty_rows = np.where(np.all(sample_grid == '.', axis=1))[0]
    empty_rows
    return (empty_rows,)


@app.cell
def _(np, sample_grid):
    empty_cols = np.where(np.all(sample_grid == '.', axis=0))[0]
    empty_cols
    return (empty_cols,)


@app.cell
def _(np, sample_grid):
    def add_cols(grid):
        empty_cols = np.where(np.all(grid == '.', axis=0))[0]
        for i, col in enumerate(empty_cols):
            new_col = np.array(['.'] * grid.shape[0])
            grid = np.insert(grid, col+i, new_col, axis=1)
            print(f'new col at {col+i}')
        return grid

    add_cols(sample_grid)
    return (add_cols,)


@app.cell
def _(add_cols, add_rows, sample_grid):
    def expand_grid(grid):
        grid = add_rows(grid)
        grid = add_cols(grid)
        return grid

    expand_grid(sample_grid)
    return (expand_grid,)


@app.cell
def _(expand_grid, np):
    _day11 = np.array([list(line) for line in (open('./data/day11.txt').read()).splitlines()])
    expand_grid(_day11)
    return


@app.cell
def _(expand_grid, np, sample_grid):
    expanded = expand_grid(sample_grid)
    galaxy_positions = np.argwhere(expanded == '#')
    print(galaxy_positions)


    total_distance = 0
    for i, pos in enumerate(galaxy_positions):
        row, col = pos
        print(pos)
        print('*'*10)
        for pair_i in range(i+1,len(galaxy_positions)):
            print(pair_i)
            pair_row, pair_col = galaxy_positions[pair_i]
            distance = abs(row-pair_row)+abs(col-pair_col)
            total_distance+=distance
    print(total_distance)


    return (
        col,
        distance,
        expanded,
        galaxy_positions,
        i,
        pair_col,
        pair_i,
        pair_row,
        pos,
        row,
        total_distance,
    )


@app.cell
def _():
    day11 = open('./data/day11.txt').read()
    day11
    return (day11,)


@app.cell
def _(day11, np):
    def convert_to_grid(file):
        lines = file.splitlines()
        grid = np.array([list(line) for line in lines])
        return grid

    convert_to_grid(day11)
    return (convert_to_grid,)


@app.cell
def _(convert_to_grid, day11, expand_grid):
    expand_grid(convert_to_grid(day11))
    return


@app.cell
def _(day11, expand_grid, np):
    def solver(file):
        grid = np.array([list(line) for line in file.splitlines()])
        expanded_grid = expand_grid(grid)
        galaxy_positions = np.argwhere(expanded_grid == '#')
        print(galaxy_positions)
    
        total_distance = 0
        for i, pos in enumerate(galaxy_positions):
            row, col = pos
            #print(pos)
            #print('*'*10)
            for pair_i in range(i+1,len(galaxy_positions)):
                #print(pair_i)
                pair_row, pair_col = galaxy_positions[pair_i]
                distance = abs(row-pair_row)+abs(col-pair_col)
                total_distance+=distance
        return total_distance

    solver(day11)
    return (solver,)


@app.cell
def _():
    list(range(5))
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #Part Two
        The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

        Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

        (In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

        Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
        """
    )
    return


@app.cell
def _(convert_to_grid, day11, np):
    def find_empty_space(grid):
        empty_cols = np.where(np.all(grid == '.', axis=0))[0]
        empty_rows = np.where(np.all(grid == '.', axis=1))[0]
        return empty_rows, empty_cols

    find_empty_space(convert_to_grid(day11))
    return (find_empty_space,)


@app.cell
def _(convert_to_grid, day11, find_empty_space):
    _empty_rows = find_empty_space(convert_to_grid(day11))[0]
    _empty_rows
    _filtered = _empty_rows[(_empty_rows>0) & (_empty_rows<200)]
    _filtered
    return


@app.cell
def _():
    def expanded_pos(row, col, empty_rows, empty_cols):
        exp_row = row + (len(empty_rows[(empty_rows<row)])*999999)
        exp_col = col + (len(empty_cols[(empty_cols<col)])*999999)
        return exp_row, exp_col
    return (expanded_pos,)


@app.cell
def _(day11, expanded_pos, find_empty_space, np):
    def solverv2(file):
        grid = np.array([list(line) for line in file.splitlines()])
        #expanded_grid = expand_grid(grid)
        galaxy_positions = np.argwhere(grid == '#')
        empty_rows, empty_cols = find_empty_space(grid)
        total_distance = 0
        expand_coordinate = lambda pos: expanded_pos(pos[0], pos[1], empty_rows, empty_cols)
        exp_positions = np.array([expand_coordinate(pos) for pos in galaxy_positions])
        for i, pos in enumerate(exp_positions):
            #print(pos)
            row, col = pos
            #print('*'*10)
            for pair_i in range(i+1,len(exp_positions)):
                #print(pair_i)
                pair_row, pair_col = exp_positions[pair_i]
                distance = abs(row-pair_row)+abs(col-pair_col)
                total_distance+=distance
        return total_distance

    solverv2(day11)
    return (solverv2,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
