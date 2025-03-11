import marimo

__generated_with = "0.11.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        #Day 6: Wait For It
        The ferry quickly brings you across Island Island. After asking around, you discover that there is indeed normally a large pile of sand somewhere near here, but you don't see anything besides lots of water and the small island where the ferry has docked.

        As you try to figure out what to do next, you notice a poster on a wall near the ferry dock. "Boat races! Open to the public! Grand prize is an all-expenses-paid trip to Desert Island!" That must be where the sand comes from! Best of all, the boat races are starting in just a few minutes.

        You manage to sign up as a competitor in the boat races just in time. The organizer explains that it's not really a traditional race - instead, you will get a fixed amount of time during which your boat has to travel as far as it can, and you win if your boat goes the farthest.

        As part of signing up, you get a sheet of paper (your puzzle input) that lists the time allowed for each race and also the best distance ever recorded in that race. To guarantee you win the grand prize, you need to make sure you go farther in each race than the current record holder.

        The organizer brings you over to the area where the boat races are held. The boats are much smaller than you expected - they're actually toy boats, each with a big button on top. Holding down the button charges the boat, and releasing the button allows the boat to move. Boats move faster if their button was held longer, but time spent holding the button counts against the total race time. You can only hold the button at the start of the race, and boats don't move until the button is released.

        For example:
        ```
        Time:      7  15   30
        Distance:  9  40  200
        ```
        This document describes three races:

        The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters.
        The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters.
        The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters.
        Your toy boat has a starting speed of zero millimeters per millisecond. For each whole millisecond you spend at the beginning of the race holding down the button, the boat's speed increases by one millimeter per millisecond.

        So, because the first race lasts 7 milliseconds, you only have a few options:

        Don't hold the button at all (that is, hold it for 0 milliseconds) at the start of the race. The boat won't move; it will have traveled 0 millimeters by the end of the race.
        Hold the button for 1 millisecond at the start of the race. Then, the boat will travel at a speed of 1 millimeter per millisecond for 6 milliseconds, reaching a total distance traveled of 6 millimeters.
        Hold the button for 2 milliseconds, giving the boat a speed of 2 millimeters per millisecond. It will then get 5 milliseconds to move, reaching a total distance of 10 millimeters.
        Hold the button for 3 milliseconds. After its remaining 4 milliseconds of travel time, the boat will have gone 12 millimeters.
        Hold the button for 4 milliseconds. After its remaining 3 milliseconds of travel time, the boat will have gone 12 millimeters.
        Hold the button for 5 milliseconds, causing the boat to travel a total of 10 millimeters.
        Hold the button for 6 milliseconds, causing the boat to travel a total of 6 millimeters.
        Hold the button for 7 milliseconds. That's the entire duration of the race. You never let go of the button. The boat can't move until you let go of the button. Please make sure you let go of the button so the boat gets to move. 0 millimeters.
        Since the current record for this race is 9 millimeters, there are actually 4 different ways you could win: you could hold the button for 2, 3, 4, or 5 milliseconds at the start of the race.

        In the second race, you could hold the button for at least 4 milliseconds and at most 11 milliseconds and beat the record, a total of 8 different ways to win.

        In the third race, you could hold the button for at least 11 milliseconds and no more than 19 milliseconds and still beat the record, a total of 9 ways you could win.

        To see how much margin of error you have, determine the number of ways you can beat the record in each race; in this example, if you multiply these values together, you get 288 (4 * 8 * 9).

        Determine the number of ways you could beat the record in each race. What do you get if you multiply these numbers together?
        """
    )
    return


@app.cell
def _():
    sample = '''Time:      7  15   30
    Distance:  9  40  200'''
    return (sample,)


@app.cell
def _(sample):
    sample.splitlines()
    sample_times = [int(x) for x in sample.splitlines()[0].split(':')[1].split()]
    print(f'Times: {sample_times}')
    sample_records = [int(x) for x in sample.splitlines()[1].split(':')[1].split()]
    print(f'Records: {sample_records}')
    sample_races = list(zip(sample_times, sample_records))
    print(f'Races: {sample_races}')
    return sample_races, sample_records, sample_times


@app.cell
def _(sample_races):
    sample_race = sample_races[0]
    for race in sample_races:
        losers = 0
        for time_held in range(0, race[0]+1):
            print(time_held)
            speed = time_held
            travel_time = race[0]-time_held
            print(travel_time)
            distance_traveled = speed*travel_time
            print(distance_traveled)
            print('*'*20)
            if distance_traveled <= race[1]:
                losers += 1
            else:
                break
        print(f'{(race[0]+1)-(losers*2)} winners')
    return (
        distance_traveled,
        losers,
        race,
        sample_race,
        speed,
        time_held,
        travel_time,
    )


@app.cell
def _(sample_races):
    def winning_races(race):
        losers = 0
        for time_held in range(0, race[0]+1):
            speed = time_held
            travel_time = race[0]-time_held
            distance_traveled = speed*travel_time
            if distance_traveled <= race[1]:
                losers += 1
                print((time_held, distance_traveled))
            else:
                break
        return (race[0]+1)-(losers*2)

    winning_races(sample_races[2])
    return (winning_races,)


@app.cell
def _(sample, winning_races):
    def mult_winners(races):
        times = [int(x) for x in races.splitlines()[0].split(':')[1].split()]
        records = [int(x) for x in races.splitlines()[1].split(':')[1].split()]
        races = list(zip(times, records))
        winners = 1
        for race in races:
            winners *= winning_races(race)
        return winners

    mult_winners(sample)
    return (mult_winners,)


@app.cell
def _():
    file_path = './data/day06.txt'
    with open(file_path) as file:
        day06 = file.read()
    day06
    return day06, file, file_path


@app.cell
def _(day06, mult_winners):
    mult_winners(day06)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        #Part Two
        As the race is about to start, you realize the piece of paper with race times and record distances you got earlier actually just has very bad kerning. There's really only one race - ignore the spaces between the numbers on each line.

        So, the example from before:

        Time:      7  15   30
        Distance:  9  40  200
        ...now instead means this:

        Time:      71530
        Distance:  940200
        Now, you have to figure out how many ways there are to win this single race. In this example, the race lasts for 71530 milliseconds and the record distance you need to beat is 940200 millimeters. You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!

        How many ways can you beat the record in this one much longer race?
        """
    )
    return


@app.cell
def _(sample):
    sample.splitlines()[0].split(':')[1]
    return


@app.cell
def _(sample):
    def process_race(race_log):
        time = int(race_log.splitlines()[0].split(':')[1].replace(' ', ''))
        record = int(race_log.splitlines()[1].split(':')[1].replace(' ', ''))
        return (time, record)

    process_race(sample)
    return (process_race,)


@app.cell
def _(day06, process_race):
    process_race(day06)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        ## Vertex Form for Parabolic Equations

        $y = a(x - h)^2 + k$

        $x$ = Time held

        $h$ = ${RaceTime}\div{2}$

        $k$ = $Max Distance$
        """
    )
    return


@app.cell
def _():
    ## Solving Parabolas
    return


@app.cell
def _(np, process_race, sample):
    # find the minimum time we need to hold the boat to win the race
    def min_time_held(race):
        h = race[0]/2
        y = race[1]
        k = h*h
        # round up to ensure we win race
        return int(np.ceil(h - np.sqrt(k-y)))

    min_time_held(process_race(sample))
    return (min_time_held,)


@app.cell
def _(np, process_race, sample):
    # find the maximmim amount of time we can hold the boat and still win the race
    def max_time_held(race):
        h = race[0]/2
        y = race[1]
        k = h*h
        # round down to ensure we win race
        return int(np.floor(h + np.sqrt(k-y)))

    max_time_held(process_race(sample))
    return (max_time_held,)


@app.cell
def _(max_time_held, min_time_held, process_race, sample):
    def winning_races_v2(race_log):
        race = process_race(race_log)
        return max_time_held(race) - min_time_held(race) + 1

    winning_races_v2(sample)
    return (winning_races_v2,)


@app.cell
def _(day06, winning_races_v2):
    # solve part 2
    winning_races_v2(day06)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Graphing Our Distance Equation""")
    return


@app.cell
def _(day06, np, plt, process_race):
    # Parameters for y = a(x-h)^2 + k
    a = -1    # controls width and direction (positive opens upward)
    h = process_race(day06)[0]/2    # horizontal shift
    k = ((process_race(day06)[0])/2)*((process_race(day06)[0])-((process_race(day06)[0])/2))   # vertical shift

    # Create x values
    x = np.linspace(-10, process_race(day06)[0], 500)

    # Create y values for shifted/scaled parabola
    y = a*(x - h)**2 + k

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.grid(True)

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Parabola: y = {a}(x - {h})² + {k}')

    # Add the x and y axis lines
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    plt.axhline(y=process_race(day06)[1], color='r', linestyle='--', label=f'Distance Needed to Win')
    plt.legend()

    plt.gca()
    return a, h, k, x, y


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
