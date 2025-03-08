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


@app.cell
def _():
    def find_borders(num_coords):
        # empty list of the coordinates for cells that border numbers
        border_coords = []
        row = num_coords[0]
        col = num_coords[1]
        for pos in list(range(-1,2)):
            border_coords.append((row+pos, col))
            border_coords.append((row, col+pos))
            border_coords.append((row+pos, col+pos))
            border_coords.append((row+pos, col-pos))
        borders = list(set(border_coords))
        return(borders)
    return (find_borders,)


@app.cell
def _(find_borders, find_numbers, sample):
    _x = find_numbers(sample)[0]
    print(_x)
    print(find_borders(_x))
    return


@app.cell
def _(find_borders, find_symbols, sample):
    # check each coordinate that borders (0, 2)
    for coord in find_borders((0, 2)):
        # check if coordinate is in our list of symbol coordinates
        if coord in find_symbols(sample):
            print('symbol found')
    return (coord,)


@app.cell
def _(find_symbols, sample):
    # creates list of coordinates for all symbols in text
    find_symbols(sample)
    return


@app.cell
def _(find_borders):
    # creates list of the bordering coordinates of a cell
    find_borders((0,0))
    return


@app.cell
def _(find_borders, find_symbols):
    # This function has print functions built in for debugging purposes

    def sum_parts(engine_scheme):
        # starting sum of 0
        sum = 0
        # string that we will append digits to
        current_number = ''
        # coordinates of the digits of the number we are working on
        current_positions = []

        # split our input into lines
        lines = engine_scheme.splitlines()
        symbols = find_symbols(engine_scheme)

        # loop through each line, creating a row index 
        for row_idx, line in enumerate(lines):
            #print(f'Row {row_idx} Start')
            # loop through each char, creating a column index
            for col_idx, char in enumerate(line):
                # check if character is a digit 
                if char.isdigit():
                    #print(f'{char} is a digit')
                    # add it to the current_number
                    current_number += char
                    # add the coordinates to current_positions
                    current_positions.append(find_borders((row_idx, col_idx)))
                # if not a digit but you were just working on a current number
                elif not char.isdigit() and len(current_number) > 0:
                    # loop through each coord in current_positions and flatten the list so we can take only unique coords
                    for border_coord in set([coord for sublist in current_positions for coord in sublist]):
                        # check if coordinate is in our list of symbol coordinates
                        if border_coord in symbols:
                            sum += int(current_number)
                            #print(f'{current_number} borders a symbol')
                            #print(f'Sum is now {sum}')
                            break
                    # if no symbol found, reset current number   
                    current_number = ''
                    current_positions = []
                    #print(f'Number reset: {current_number}')
            # At end of row if there is a current number, check its borders
            if len(current_number) > 0:
                for border_coord in set([coord for sublist in current_positions for coord in sublist]):
                        # check if coordinate is in our list of symbol coordinates
                        if border_coord in symbols:
                            sum += int(current_number)
                            #print(f'{current_number} borders a symbol')
                            #print(f'Sum is now {sum}')
                # After the symbol check, reset current number   
                current_number = ''
                current_positions = []
                #print(f'Number reset: {current_number}')
            #print(f'end of Row {row_idx}')
        #print(sum)
        return sum
    return (sum_parts,)


@app.cell
def _(sample, sum_parts):
    sum_parts(sample)
    return


@app.cell
def _(sample):
    print(sample)
    return


@app.cell
def _():
    # we need to read in the text file that we want to run our function on
    file_path = './data/day03.txt'

    with open(file_path, "r", encoding="utf-8") as file:
            day03 = file.read()
    #day03
    return day03, file, file_path


@app.cell
def _(day03, sum_parts):
    sum_parts(day03)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #Part Two
        The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

        You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

        Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

        The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

        This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

        Consider the same engine schematic again:

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

        In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

        What is the sum of all of the gear ratios in your engine schematic?


        """
    )
    return


@app.cell
def _():
    # function to find the coordinates of all gears
    def find_gears(engine_scheme):
        # empty list to store gear positions
        gear_positions = []
        # split engine schematic into lines
        lines = engine_scheme.splitlines()
        # label each row with an index
        for row_idx, line in enumerate(lines):
            # label each char in row with an index
            for col_idx, char in enumerate(line):
                # if char is a gear ('*') add its position
                if char == '*':
                    # store coordinates of symbol
                    gear_positions.append((row_idx, col_idx))
        return gear_positions
        #print(lines)
    return (find_gears,)


@app.cell
def _(find_gears, sample):
    find_gears(sample)
    return


@app.cell
def _(find_borders, find_gears):
    def find_gear_parts(engine_scheme):
        gear_dict = {}
        # string that we will append digits to
        current_number = ''
        # coordinates of the digits of the number we are working on
        current_positions = []

        # split our input into lines
        lines = engine_scheme.splitlines()
        gears = find_gears(engine_scheme)
        sum = 0

        # loop through each line, creating a row index 
        for row_idx, line in enumerate(lines):
            #print(f'Row {row_idx} Start')
            # loop through each char, creating a column index
            for col_idx, char in enumerate(line):
                # check if character is a digit 
                if char.isdigit():
                    #print(f'{char} is a digit')
                    # add it to the current_number
                    current_number += char
                    # add the coordinates to current_positions
                    current_positions.append(find_borders((row_idx, col_idx)))
                    # if not a digit but you were just working on a current number
                elif not char.isdigit() and len(current_number) > 0:
                    # loop through each coord in current_positions and flatten the list so we can take only unique coords
                    for border_coord in set([coord for sublist in current_positions for coord in sublist]):
                        # check if coordinate is in our list of symbol coordinates
                        if border_coord in gears:
                            if border_coord in list(gear_dict.keys()):
                                gear_ratio = int(gear_dict[border_coord]) * int(current_number)
                                sum += gear_ratio
                                #print(f'{current_number} borders a symbol')
                                #print(f'Sum is now {sum}')
                                break
                            else:
                                gear_dict[border_coord] = current_number
                    # if no symbol found, reset current number   
                    current_number = ''
                    current_positions = []
                    #print(f'Number reset: {current_number}')
            # At end of row if there is a current number, check its borders
            if len(current_number) > 0:
                for border_coord in set([coord for sublist in current_positions for coord in sublist]):
                        # check if coordinate is in our list of symbol coordinates
                        if border_coord in gears:
                            if border_coord in list(gear_dict.keys()):
                                gear_ratio = int(gear_dict[border_coord]) * int(current_number)
                                sum += gear_ratio
                                #print(f'{current_number} borders a symbol')
                                #print(f'Sum is now {sum}')
                                break
                            else:
                                gear_dict[border_coord] = current_number
                # After the symbol check, reset current number   
                current_number = ''
                current_positions = []
        return sum
    
    return (find_gear_parts,)


@app.cell
def _():
    test = {}
    test['one'] = 1
    test['two'] = 2
    list(test.keys())
    return (test,)


@app.cell
def _(find_gear_parts, sample):
    find_gear_parts(sample)
    return


@app.cell
def _(day03, find_gear_parts):
    find_gear_parts(day03)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
