import marimo

__generated_with = "0.11.12"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import re
    import math
    return math, mo, re


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        #Day 8: Haunted Wasteland
        You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about **ghosts** a few minutes ago.

        One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of **network** of labeled nodes.

        It seems like you're meant to use the **left/right** instructions to **navigate the network**. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

        After examining the maps for a bit, two nodes stick out: `AAA` and `ZZZ`. You feel like `AAA` is where you are now, and you have to follow the left/right instructions until you reach `ZZZ`.

        This format defines each **node** of the network individually. For example:
        ```
        RL

        AAA = (BBB, CCC)
        BBB = (DDD, EEE)
        CCC = (ZZZ, GGG)
        DDD = (DDD, DDD)
        EEE = (EEE, EEE)
        GGG = (GGG, GGG)
        ZZZ = (ZZZ, ZZZ)
        ```

        Starting with `AAA`, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of `AAA`, `CCC`. Then, `L` means to choose the **left** element of `CCC`, `ZZZ`. By following the left/right instructions, you reach `ZZZ` in `2` steps.

        Of course, you might not find `ZZZ` right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means `RLRLRLRLRLRLRLRL...` and so on. For example, here is a situation that takes `6` steps to reach `ZZZ`:
        ```
        LLR

        AAA = (BBB, BBB)
        BBB = (AAA, ZZZ)
        ZZZ = (ZZZ, ZZZ)
        ```
        Starting at `AAA`, follow the left/right instructions. **How many steps are required to reach `ZZZ`?**
        """
    )
    return


@app.cell
def _():
    sample = '''RL

    AAA = (BBB, CCC)
    BBB = (DDD, EEE)
    CCC = (ZZZ, GGG)
    DDD = (DDD, DDD)
    EEE = (EEE, EEE)
    GGG = (GGG, GGG)
    ZZZ = (ZZZ, ZZZ)'''

    print(sample)
    return (sample,)


@app.cell
def _(sample):
    _start = 'AAA'
    map_start = sample.find(f'{_start} = ')
    map_start
    return (map_start,)


@app.cell
def _(map_start, sample):
    # start of coord in sample
    print(sample[10])
    # end of coord in sample
    print(sample[19])
    # full coord
    print(sample[10:20])

    # finding the strings for the left and right
    print(f'Left is {sample[11:14]}')
    print(f'Right is {sample[16:19]}')

    # finding the string with start point from .find() function
    print(f'Left is {sample[(map_start+7):(map_start+10)]}')
    print(f'Right is {sample[(map_start+12):(map_start+15)]}')
    return


@app.cell
def _(sample):
    def get_instructions(map):
        intstructions = map.splitlines()[0]
        return intstructions

    print(get_instructions(sample))
    return (get_instructions,)


@app.cell
def _(sample):
    def next_node(map, start, side):
        node_loc = map.find(f'{start} = ')
        if side == 'L':
            return map[(node_loc+7):(node_loc+10)]
        elif side == 'R':
            return map[(node_loc+12):(node_loc+15)]

    print(next_node(sample, 'AAA', 'L'))
    return (next_node,)


@app.cell
def _(get_instructions, next_node, sample):
    def follow_map_steps(map):
        start = 'AAA'
        steps = 0
        while start != 'ZZZ':
            for instruction in get_instructions(map):
                steps += 1
                print(f'Starting at: {start}')
                start = next_node(map, start, instruction)
                print(f' Next Start: {start}')
                if start == 'ZZZ':
                    print('Done!')
                    break
        print(steps)

    follow_map_steps(sample)
    return (follow_map_steps,)


@app.cell
def _():
    day08 = open('./data/day08.txt').read()
    day08
    return (day08,)


@app.cell
def _(day08, follow_map_steps):
    follow_map_steps(day08)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #Part Two
        The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

        What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

        After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

        For example:

        ```
        LR

        11A = (11B, XXX)
        11B = (XXX, 11Z)
        11Z = (11B, XXX)
        22A = (22B, XXX)
        22B = (22C, 22C)
        22C = (22Z, 22Z)
        22Z = (22B, 22B)
        XXX = (XXX, XXX)
        ```

        Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

        Step 0: You are at 11A and 22A.
        Step 1: You choose all of the left paths, leading you to 11B and 22B.
        Step 2: You choose all of the right paths, leading you to 11Z and 22C.
        Step 3: You choose all of the left paths, leading you to 11B and 22Z.
        Step 4: You choose all of the right paths, leading you to 11Z and 22B.
        Step 5: You choose all of the left paths, leading you to 11B and 22C.
        Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
        So, in this example, you end up entirely on nodes that end in Z after 6 steps.

        Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
        """
    )
    return


@app.cell
def _():
    ghost_sample = '''LR

    11A = (11B, XXX)
    11B = (XXX, 11Z)
    11Z = (11B, XXX)
    22A = (22B, XXX)
    22B = (22C, 22C)
    22C = (22Z, 22Z)
    22Z = (22B, 22B)
    XXX = (XXX, XXX)'''
    return (ghost_sample,)


@app.cell
def _(day08, ghost_sample, re):
    def find_starting_points(map):
        # find all points where the node ends in A
        pattern = r'\w+A = '
        matches = [x[:3] for x in re.findall(pattern, map)]
        return matches

    print(find_starting_points(day08))
    print(find_starting_points(ghost_sample))
    return (find_starting_points,)


@app.cell
def _(day08, re):
    re.findall(r'\w+A = ', day08)
    return


@app.cell
def _():
    'HVA = '[2]
    return


@app.cell
def _(find_starting_points, get_instructions, ghost_sample, next_node):
    #starting_points = find_starting_points(map)
    #for i, node in enumerate(starting_points):
    #    starting_points[i] = next_node()


    def follow_ghost_steps(map):
        starting_points = find_starting_points(map)
        last_letters = [x[2] for x in starting_points]
        #print(last_letters)
        steps = 0
        instructions = get_instructions(map)
        while set(last_letters) != {'Z'}:
            for instruction in instructions:
                #print(instruction)
                steps += 1
                #print(f'Starting at: {starting_points}')
                for i, node in enumerate(starting_points):
                    starting_points[i] = next_node(map, node, instruction)
                    #print(starting_points)
                    last_letters[i] = starting_points[i][2]
                    #print(last_letters)
                #print(f' Next Start: {starting_points}')
                if set(last_letters) == {'Z'}:
                    #print('Done!')
                    break
        print(steps)

    follow_ghost_steps(ghost_sample)
    return (follow_ghost_steps,)


@app.cell
def _():
    # Runtime to long
    #follow_ghost_steps(day08)
    return


@app.cell
def _(find_starting_points, get_instructions, ghost_sample, math, next_node):
    def follow_ghost_steps_v2(map):
        starting_points = find_starting_points(map)
        last_letters = [x[2] for x in starting_points]
        fewest_steps = []
        #print(last_letters)
        instructions = get_instructions(map)
        for starting_point in starting_points:
            steps = 0
            while starting_point[-1] != 'Z':
                for instruction in instructions:
                    #print(instruction)
                    steps += 1
                    #print(f'Starting at: {starting_points}')
                    starting_point = next_node(map, starting_point, instruction)
                    #print(starting_points)
                    #print(last_letters)
                    #print(f' Next Start: {starting_points}')
                    if starting_point[-1] == 'Z':
                        #print('Done!')
                        fewest_steps.append(steps)
                        break
        print(fewest_steps)
        return math.lcm(*fewest_steps)

    follow_ghost_steps_v2(ghost_sample)
    return (follow_ghost_steps_v2,)


@app.cell
def _(day08, follow_ghost_steps_v2):
    follow_ghost_steps_v2(day08)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
