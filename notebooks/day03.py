import marimo

__generated_with = "0.11.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        #Day 3: Gear Ratios
        You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

        It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

        "Aaah!"

        You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

        The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

        The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently **any number adjacent to a symbol**, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

        Here is an example engine schematic:
        ```
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
        ```
        In this schematic, two numbers are **not** part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so **is** a part number; their sum is 4361.

        Of course, the actual engine schematic is much larger. **What is the sum of all of the part numbers in the engine schematic?**
        """
    )
    return


@app.cell
def _():
    sample = '''467..114..
    ...*......
    ..35..633.
    ......#...
    617*......
    .....+.58.
    ..592.....
    ......755.
    ...$.*....
    .664.598..
    '''
    sample
    return (sample,)


@app.cell
def _(sample):
    sample_lines = sample.splitlines()
    sample_lines
    return (sample_lines,)


@app.cell
def _():
    def find_symbols(file):
        # empty list to store symbol positions
        symbol_positions = []
        # split file into lines
        lines = file.splitlines()
        # label each row with an index
        for row_idx, line in enumerate(lines):
            # label each char in row with an index
            for col_idx, char in enumerate(line):
                # if char is not a number or a '.' it is a symbol
                if not char.isdigit() and char != '.':
                    # store coordinates of symbol
                    symbol_positions.append((row_idx, col_idx))
        return symbol_positions
        #print(lines)
    return (find_symbols,)


@app.cell
def _(find_symbols, sample):
    find_symbols(sample)
    return


@app.cell
def _():
    # for a symbol at (row 1, col 3) what are the eligible border positions
    # (row 0, col 2-4)
    # (row 1, col 2 or col 4)
    # (row 2, col 2-4)
    # so anything in the row +-1, and the col+-1 is eligible
    return


@app.cell
def _():
    # after creating this function, I am realizing it may be easier to find the numbers first, then check if a symbol borders them
    return


@app.cell
def _():
    # we can make a function that finds all the numbers, and their border coordinates, and check if any of the coordinates are in our list of symbol coordinates
    return


@app.cell
def _():
    def find_numbers(file):
        # copy of find_symbols() funct to find number positions
        number_positions = []
        lines = file.splitlines()
        for row_idx, line in enumerate(lines):
            for col_idx, char in enumerate(line):
                if char.isdigit():
                    number_positions.append((row_idx, col_idx))
        return number_positions
    return (find_numbers,)


@app.cell
def _(find_numbers, sample):
    find_numbers(sample)
    return


app._unparsable_cell(
    r"""
    def find_borders(num_coords):
        border_coords = []
        for (row_idx, col_idx) in num_coords:
        
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
