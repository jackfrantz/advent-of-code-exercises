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
        r"""
        #Day 13: Point of Incidence
        With your help, the hot springs team locates an appropriate spring which launches you neatly and precisely up to the edge of Lava Island.

        There's just one problem: you don't see any lava.

        You do see a lot of ash and igneous rock; there are even what look like gray mountains scattered around. After a while, you make your way to a nearby cluster of mountains only to discover that the valley between them is completely full of large mirrors. Most of the mirrors seem to be aligned in a consistent way; perhaps you should head in that direction?

        As you move through the valley of mirrors, you find that several of them have fallen from the large metal frames keeping them in place. The mirrors are extremely flat and shiny, and many of the fallen mirrors have lodged into the ash at strange angles. Because the terrain is all one color, it's hard to tell where it's safe to walk or where you're about to run into a mirror.

        You note down the patterns of ash (.) and rocks (#) that you see as you walk (your puzzle input); perhaps by carefully analyzing these patterns, you can figure out where the mirrors are!

        For example:
        ```
        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#.

        #...##..#
        #....#..#
        ..##..###
        #####.##.
        #####.##.
        ..##..###
        #....#..#
        ```
        To find the reflection in each pattern, you need to find a perfect reflection across either a horizontal line between two rows or across a vertical line between two columns.

        In the first pattern, the reflection is across a vertical line between two columns; arrows on each of the two columns point at the line between the columns:
        ```
        123456789
            ><   
        #.##..##.
        ..#.##.#.
        ##......#
        ##......#
        ..#.##.#.
        ..##..##.
        #.#.##.#.
            ><   
        123456789
        ```
        In this pattern, the line of reflection is the vertical line between columns 5 and 6. Because the vertical line is not perfectly in the middle of the pattern, part of the pattern (column 1) has nowhere to reflect onto and can be ignored; every other column has a reflected column within the pattern and must match exactly: column 2 matches column 9, column 3 matches 8, 4 matches 7, and 5 matches 6.

        The second pattern reflects across a horizontal line instead:
        ```
        1 #...##..# 1
        2 #....#..# 2
        3 ..##..### 3
        4v#####.##.v4
        5^#####.##.^5
        6 ..##..### 6
        7 #....#..# 7
        ```
        This pattern reflects across the horizontal line between rows 4 and 5. Row 1 would reflect with a hypothetical row 8, but since that's not in the pattern, row 1 doesn't need to match anything. The remaining rows match: row 2 matches row 7, row 3 matches row 6, and row 4 matches row 5.

        To summarize your pattern notes, add up the number of columns to the left of each vertical line of reflection; to that, also add 100 multiplied by the number of rows above each horizontal line of reflection. In the above example, the first pattern's vertical line has 5 columns to its left and the second pattern's horizontal line has 4 rows above it, a total of 405.

        Find the line of reflection in each of the patterns in your notes. What number do you get after summarizing all of your notes?
        """
    )
    return


@app.cell
def _():
    # need to find which columns/rows are both the same AND next to each other to find the reflecting line
    return


@app.cell
def _():
    sample = '''#.##..##.
    ..#.##.#.
    ##......#
    ##......#
    ..#.##.#.
    ..##..##.
    #.#.##.#.

    #...##..#
    #....#..#
    ..##..###
    #####.##.
    #####.##.
    ..##..###
    #....#..#'''
    return (sample,)


@app.cell
def _(sample):
    sample_0 = sample.split('\n\n')[0]
    sample_0
    return (sample_0,)


@app.cell
def _(sample_0):
    sample_0_lines = sample_0.splitlines()
    sample_0_lines
    return (sample_0_lines,)


@app.cell
def _(np, sample_0_lines):
    sample_0_array = np.array([list(line) for line in sample_0_lines])
    sample_0_array
    return (sample_0_array,)


@app.cell
def _(np, sample, sample_0):
    def array_pattern(pattern):
        pattern_lines = pattern.splitlines()
        pattern_array = np.array([list(line) for line in pattern_lines])
        return pattern_array

    array_pattern(sample_0)
    sample_1_array = array_pattern(sample.split('\n\n')[1])
    return array_pattern, sample_1_array


@app.cell
def _(np, sample_0_array):
    col = 4
    np.array_equal(sample_0_array[:, col], sample_0_array[:, col+1])
    return (col,)


@app.cell
def _(sample_0_array):
    sample_0_array.shape
    return


@app.cell
def _(sample_1_array):
    print(sample_1_array)
    print('*'*40)
    print(sample_1_array[0:2][::-1])
    return


@app.cell
def _(np, sample_0_array):
    def vert_reflection(pattern_array):
        n_cols = pattern_array.shape[1]
        for i in range(n_cols-1):
            if np.array_equal(pattern_array[:, i], pattern_array[:, i+1]):
                for j in range(0, i):
                    sym = np.array_equal(pattern_array[:, i-j], pattern_array[:, i+1+j])
                    if not sym:
                        break
                if sym:
                    return i+1
        return 0

    vert_reflection(sample_0_array)
    return (vert_reflection,)


@app.cell
def _(np, sample_0_array):
    def horiz_reflection(pattern_array):
        n_rows = pattern_array.shape[1]
        for i in range(n_rows-1):
            print(f'i is {i}')
            if np.array_equal(pattern_array[i], pattern_array[i+1]):
                for j in range(1, i):
                    print(f'j is {j}')
                    sym = np.array_equal(pattern_array[i-j], pattern_array[i+1+j])
                    print(sym)
                    if not sym:
                        break
                if sym:
                    return i+1
        return 0

    horiz_reflection(sample_0_array)
    return (horiz_reflection,)


@app.cell
def _(array_pattern):
    def solve(text):

        patterns = text.split('\n\n')

        for pattern in patterns:
            pattern_array = array_pattern(pattern)

        pass
    return (solve,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
