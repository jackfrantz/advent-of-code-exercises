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
        #Day 2: Cube Conundrum
        You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

        The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

        As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

        To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

        You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

        For example, the record of a few games might look like this:

        ```Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green```

        In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

        The Elf would first like to know which games would have been possible if the bag contained **only 12 red cubes, 13 green cubes, and 14 blue cubes?**

        In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been **impossible** because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been **impossible** because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get ```8```.

        Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. **What is the sum of the IDs of those games?**
        """
    )
    return


@app.cell
def _():
    sample = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
    sample
    return (sample,)


@app.cell
def _(sample):
    sample_lines = sample.splitlines()
    sample_lines[0]
    return (sample_lines,)


@app.cell
def _(sample_lines):
    sample_line = sample_lines[0]
    return (sample_line,)


@app.cell
def _(sample_line):
    x = sample_line.split(': ')[1].split('; ')
    for _i in x:
        rounds = _i.split(', ')
        print(rounds)
    return rounds, x


@app.cell
def _(x):
    [i.split(', ') for i in x]
    return


@app.cell
def _(x):
    _flattened = [item for sublist in x for item in sublist.split(', ')]
    print(_flattened)
    return


@app.cell
def _(x):
    _flattened = [_item for _sublist in x for _item in _sublist.split(', ')]
    print(_flattened)


    _dict = {}
    for _i in _flattened:
        print(_i.split(' '))
        _quant = _i.split(' ')[0]
        _color = _i.split(' ')[1]
        if _color in _dict:  # check if we have seen the color before
            _dict[_color] = max(_dict[_color], _quant) # keep the maximum value seen
            print(_dict)
        # else if color has not been seen yet, add it to the dictionary
        else:
            _dict[_color] = _quant
            print(_dict)
    print(_dict)

    sample_dict = _dict
    return (sample_dict,)


@app.cell
def _(sample_dict):
    sample_dict
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
