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
        r"""
        #Day 1: Trebuchet?!
        Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

        You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

        Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

        You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

        As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

        The newly-improved calibration document consists of lines of text; each line originally contained a specific **calibration value** that the Elves now need to recover. On each line, the calibration value can be found by combining the **first digit** and the **last digit** (in that order) to form a single **two-digit number**.

        For example:

        1abc2<br>
        pqr3stu8vwx<br>
        a1b2c3d4e5f<br>
        treb7uchet<br>

        In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

        Consider your entire calibration document. **What is the sum of all of the calibration values?**
        """
    )
    return


@app.cell
def _():
    sample = '''1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet'''
    sample
    return (sample,)


@app.cell
def _(sample):
    sample_lines = sample.splitlines()
    sample_lines
    return (sample_lines,)


@app.cell
def _(sample_lines):
    x = sample_lines[2]
    x
    return (x,)


@app.cell
def _(x):
    ## for loop to find first digit of calibration value
    for _char in x:
        if _char.isdigit() == True:
            first = _char
            break
    first
    return (first,)


@app.cell
def _(x):
    ## for loop to find second digit of calibration value
    for _char in x:
        if _char.isdigit() == True:
            last = _char
    last
    return (last,)


@app.cell
def _(first, last):
    first+last
    return


@app.cell
def _():
    def cal_value(x):
        for char in x:
            if char.isdigit() == True:
                first = char
                break
        for char in x:
            if char.isdigit() == True:
                last = char
        value = int(first+last)
        return value
    return (cal_value,)


@app.cell
def _(cal_value, x):
    cal_value(x)
    return


@app.cell
def _(cal_value, sample_lines):
    # set initital calibration value to 0
    _total_cal_value = 0
    # execute cal_value() on each line in the sample adding each line to the total 
    for line in sample_lines:
        _total_cal_value += cal_value(line)
    _total_cal_value
    return (line,)


@app.cell
def _(cal_value, sample):
    # create function that can run on a string
    def _calibration_sum(text):
        # turn text into list
        text_lines = text.splitlines()
        # set total cal value to 0
        total_cal_value = 0
        # get cal value for each line and add it to the total cal value
        for line in text_lines:
            total_cal_value += cal_value(line)
        #return sum of all the line calibration values
        return total_cal_value

    _calibration_sum(sample)
    return


@app.cell
def _():
    # we need to read in the text file that we want to run our function on
    file_path = './data/day01.txt'

    with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
    text
    return file, file_path, text


@app.cell
def _(cal_value):
    # create function that can run given a text file
    def calibration_sum(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        # turn text into list
        text_lines = text.splitlines()
        # set total cal value to 0
        total_cal_value = 0
        # get cal value for each line and add it to the total cal value
        for line in text_lines:
            total_cal_value += cal_value(line)
        #return sum of all the line calibration values
        return total_cal_value
    return (calibration_sum,)


@app.cell
def _(calibration_sum, file_path):
    # this function should will now return the total calibration value for our file
    calibration_sum(file_path)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ##Part Two

        Your calculation isn't quite right. It looks like some of the digits are actually **spelled out with letters:** one, two, three, four, five, six, seven, eight, and nine **also** count as valid "digits".

        Equipped with this new information, you now need to find the real first and last digit on each line. For example:

        two1nine<br>
        eightwothree<br>
        abcone2threexyz<br>
        xtwone3four<br>
        4nineeightseven2<br>
        zoneight234<br>
        7pqrstsixteen<br>

        In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces **281**.

        **What is the sum of all of the calibration values?**
        """
    )
    return


@app.cell
def _():
    sample2 = '''two1nine
    eightwothree
    abcone2threexyz
    xtwone3four
    4nineeightseven2
    zoneight234
    7pqrstsixteen'''
    return (sample2,)


@app.cell
def _(sample2):
    sample2_lines = sample2.splitlines()
    sample2_lines
    return (sample2_lines,)


@app.cell
def _(sample2_lines):
    y = sample2_lines[0]

    positions = {}
    for i, char in enumerate(y):
        if char.isdigit():
            positions[i] = char

    positions
    return char, i, positions, y


@app.cell
def _():
    # Create a dictionary for number words to digits
    number_map = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    number_map.items()
    return (number_map,)


@app.cell
def _(number_map, y):
    # identifying a word in a string
    for word, digit in number_map.items():
        if word in y:
            print(number_map[word])
    return digit, word


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
