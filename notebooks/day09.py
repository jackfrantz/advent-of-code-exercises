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
        # Day 9: Mirage Maintenance
        You ride the camel through the sandstorm and stop where the ghost's maps told you to stop. The sandstorm subsequently subsides, somehow seeing you standing at an **oasis**!

        The camel goes to get some water and you stretch your neck. As you look up, you discover what must be yet another giant floating island, this one made of metal! That must be where the parts to **fix the sand machines come from**.

        There's even a **hang glider** partially buried in the sand here; once the sun rises and heats up the sand, you might be able to use the glider and the hot air to get all the way up to the metal island!

        While you wait for the sun to rise, you admire the oasis hidden here in the middle of Desert Island. It must have a delicate ecosystem; you might as well take some ecological readings while you wait. Maybe you can report any environmental instabilities you find to someone so the oasis can be around for the next sandstorm-worn traveler.

        You pull out your handy **Oasis And Sand Instability Sensor** and analyze your surroundings. The OASIS produces a report of many values and how they are changing over time (your puzzle input). Each line in the report contains the **history** of a single value. For example:
        ```
        0 3 6 9 12 15
        1 3 6 10 15 21
        10 13 16 21 30 45
        ```
        To best protect the oasis, your environmental report should include a **prediction of the next value** in each history. To do this, start by making a new sequence from the **difference at each step** of your history. If that sequence is **not** all zeroes, repeat this process, using the sequence you just generated as the input sequence. Once all of the values in your latest sequence are zeroes, you can extrapolate what the next value of the original history should be.

        In the above dataset, the first history is `0 3 6 9 12 15`. Because the values increase by 3 each step, the first sequence of differences that you generate will be `3 3 3 3 3`. Note that this sequence has one fewer value than the input sequence because at each step it considers two numbers from the input. Since these values aren't **all zero**, repeat the process: the values differ by 0 at each step, so the next sequence is `0 0 0 0`. This means you have enough information to extrapolate the history! Visually, these sequences can be arranged like this:
        ```
        0   3   6   9  12  15
          3   3   3   3   3
            0   0   0   0
        ```
        To extrapolate, start by adding a new zero to the end of your list of zeroes; because the zeroes represent differences between the two values above them, this also means there is now a placeholder in every sequence above it:

        ```
        0   3   6   9  12  15   B
          3   3   3   3   3   A
            0   0   0   0   0
        ```

        You can then start filling in placeholders from the bottom up. `A` needs to be the result of increasing 3 (the value to its left) by 0 (the value below it); this means A must be 3:
        ```
        0   3   6   9  12  15   B
          3   3   3   3   3   3
            0   0   0   0   0
        ```
        Finally, you can fill in `B`, which needs to be the result of increasing `15` (the value to its left) by `3` (the value below it), or `18`:
        ```
        0   3   6   9  12  15  18
          3   3   3   3   3   3
            0   0   0   0   0
        ```
        So, the next value of the first history is `18`.

        Finding all-zero differences for the second history requires an additional sequence:
        ```
        1   3   6  10  15  21
          2   3   4   5   6
            1   1   1   1
              0   0   0
        ```
        Then, following the same process as before, work out the next value in each sequence from the bottom up:
        ```
        1   3   6  10  15  21  28
          2   3   4   5   6   7
            1   1   1   1   1
              0   0   0   0
        ```
        So, the next value of the second history is `28`.

        The third history requires even more sequences, but its next value can be found the same way:
        ```
        10  13  16  21  30  45  68
           3   3   5   9  15  23
             0   2   4   6   8
               2   2   2   2
                 0   0   0
        ```
        So, the next value of the third history is `68`.

        If you find the next value for each history in this example and add them together, you get `114`.

        Analyze your OASIS report and extrapolate the next value for each history. **What is the sum of these extrapolated values**?


        """
    )
    return


@app.cell
def _():
    sample = '''0 3 6 9 12 15
    1 3 6 10 15 21
    10 13 16 21 30 45'''
    return (sample,)


@app.cell
def _(sample):
    sample_hist  = [int(x) for x in sample.splitlines()[0].split()]
    sample_hist
    return (sample_hist,)


@app.cell
def _(sample_hist):
    _last_numbers = [sample_hist[-1]]
    _predictions = sample_hist
    while set(_predictions) != {0}:
        print(_predictions)
        _predictions = [(_predictions[i+1]-_predictions[i]) for i in range(len(_predictions)-1)]
        _last_numbers.append(_predictions[-1])
    print(_last_numbers)
    print(sum(_last_numbers))
    return


@app.cell
def _(sample_hist):
    def extrapolate_history(history):
        last_numbers = [history[-1]]
        predictions = history
        while set(predictions) != {0}:
            #print(predictions)
            predictions = [(predictions[i+1]-predictions[i]) for i in range(len(predictions)-1)]
            last_numbers.append(predictions[-1])
        #print(last_numbers)
        #print(sum(last_numbers))
        return sum(last_numbers)

    extrapolate_history(sample_hist)
    return (extrapolate_history,)


@app.cell
def _(extrapolate_history, sample):
    extrapolate_history([int(x) for x in sample.splitlines()[1].split()])
    return


@app.cell
def _(extrapolate_history, sample):
    extrapolate_history([int(x) for x in sample.splitlines()[2].split()])
    return


@app.cell
def _(extrapolate_history, sample):
    def sum_extra_values(history):
        sum = 0
        for history in history.splitlines():
            sum += extrapolate_history([int(x) for x in history.split()])
        return sum

    sum_extra_values(sample)
    return (sum_extra_values,)


@app.cell
def _():
    day09 = open('./data/day09.txt').read()
    return (day09,)


@app.cell
def _(day09, sum_extra_values):
    sum_extra_values(day09)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #Part Two
        Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

        For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

        In particular, here is what the third example history looks like when extrapolating back in time:
        ```
        5  10  13  16  21  30  45
          5   3   3   5   9  15
           -2   0   2   4   6
              2   2   2   2
                0   0   0
        ```
        Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

        Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

        Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
        """
    )
    return


@app.cell
def _(sample):
    sample_hist_3 = [int(x) for x in sample.splitlines()[2].split()]
    return (sample_hist_3,)


@app.cell
def _(sample):
    sample_hist_2 = [int(x) for x in sample.splitlines()[1].split()]
    return (sample_hist_2,)


@app.cell
def _(sample_hist_3):
    def previous_history(history):
        first_numbers = [history[0]]
        predictions = history
        while set(predictions) != {0}:
            #print(predictions)
            predictions = [(predictions[i+1]-predictions[i]) for i in range(len(predictions)-1)]
            first_numbers.append(predictions[0])
        #print(first_numbers)
        prev_prediction = 0
        first_numbers.reverse()
        #print(first_numbers)
        for i in range(len(first_numbers)-1):
            prev_prediction = first_numbers[i+1] - prev_prediction
            #print(prev_prediction)
        return prev_prediction

    previous_history(sample_hist_3)
    return (previous_history,)


@app.cell
def _():
    first_numbers = [1, 2, 1, 0]
    range(len(first_numbers))
    first_numbers.reverse()
    first_numbers
    return (first_numbers,)


@app.cell
def _(previous_history, sample):
    def sum_prev_values(history):
        sum = 0
        for history in history.splitlines():
            sum += previous_history([int(x) for x in history.split()])
        return sum

    sum_prev_values(sample)
    return (sum_prev_values,)


@app.cell
def _(day09, sum_prev_values):
    sum_prev_values(day09)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
