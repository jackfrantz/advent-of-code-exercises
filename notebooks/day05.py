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
        #Day 5: If You Give A Seed A Fertilizer
        You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

        "A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

        "Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

        "I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

        You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

        The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

        For example:

        ```
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
        ```
        The almanac starts by listing which seeds need to be planted: **seeds 79, 14, 55, and 13**.


        The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

        Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: **the destination range start, the source range start, and the range length**.

        Consider again the example seed-to-soil map:
        ```
        50 98 2
        52 50 48
        ```
        The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

        The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

        Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

        So, the entire list of seed numbers and their corresponding soil numbers looks like this:

        seed  soil
        0     0
        1     1
        ...   ...
        48    48
        49    49
        50    52
        51    53
        ...   ...
        96    98
        97    99
        98    50
        99    51
        With this map, you can look up the soil number required for each initial seed number:

        Seed number 79 corresponds to soil number 81.
        Seed number 14 corresponds to soil number 14.
        Seed number 55 corresponds to soil number 57.
        Seed number 13 corresponds to soil number 13.

        The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. **Using these maps, find the lowest location number that corresponds to any of the initial seeds.** To do this, you'll need to **convert each seed number through other categories until you can find its corresponding location number**. In this example, the corresponding types are:
        ```
        Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
        Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
        Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
        Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
        ```
        So, the lowest location number in this example is 35.

        **What is the lowest location number that corresponds to any of the initial seed numbers?**
        """
    )
    return


@app.cell
def _():
    sample = '''seeds: 79 14 55 13

    seed-to-soil map:
    50 98 2
    52 50 48

    soil-to-fertilizer map:
    0 15 37
    37 52 2
    39 0 15

    fertilizer-to-water map:
    49 53 8
    0 11 42
    42 0 7
    57 7 4

    water-to-light map:
    88 18 7
    18 25 70

    light-to-temperature map:
    45 77 23
    81 45 19
    68 64 13

    temperature-to-humidity map:
    0 69 1
    1 0 69

    humidity-to-location map:
    60 56 37
    56 93 4'''
    return (sample,)


@app.cell
def _():
    samp_seed_soil_map = '''seed-to-soil map:
    50 98 2
    52 50 48'''
    return (samp_seed_soil_map,)


@app.cell
def _():
    def seed_to_soil(seed, seed_soil_map):
        soil = seed
        for line in seed_soil_map.splitlines()[1:]:
            print(line)
            dest_range_start = int(line.split()[0])
            source_range_start = int(line.split()[1])
            range_len = int(line.split()[2])
            if seed >= source_range_start and seed < (source_range_start+range_len):
                print(f'{seed} in range')
                soil = dest_range_start + (seed - source_range_start)
        return soil
    return (seed_to_soil,)


@app.cell
def _(samp_seed_soil_map, seed_to_soil):
    seed_to_soil(79, samp_seed_soil_map)
    return


@app.cell
def _():
    def map_converter(source, map):
        # set default destination value equal to source except mapped otherwise
        destination = source
        for line in map.splitlines()[1:]:
            # get the range values
            dest_range_start, source_range_start, range_len = [int(x) for x in line.split()]
            # check if source is in range of this line of the map
            if source >= source_range_start and source < (source_range_start+range_len):
                # set destination value based on the map
                destination = dest_range_start + (source - source_range_start)
                break
        return destination
    return (map_converter,)


@app.cell
def _(map_converter, samp_seed_soil_map):
    map_converter(79, samp_seed_soil_map)
    return


@app.cell
def _(sample):
    sample.split('\n\n')[1].splitlines()[1:]
    return


@app.cell
def _(map_converter, sample):
    # seed 79 should have a final location of 82
    seed = 79
    for map in sample.split('\n\n')[1:]:
        print(f'Input is {seed}')
        print(map)
        seed = map_converter(seed, map)
        print(f'Output is {seed}')
        print('*'*20)
    print(seed)
    return map, seed


@app.cell
def _(map_converter):
    def location_finder(seed, almanac):
        value = seed
        for map in almanac.split('\n\n')[1:]:
            value = map_converter(value, map)
        return value
    return (location_finder,)


@app.cell
def _(location_finder, sample):
    location_finder(79, sample)
    return


@app.cell
def _(location_finder):
    def lowest_location_finder(almanac):
        # list to store locations
        locations = []
        # find locations of each seed
        for seed in [int(x) for x in almanac.split('\n\n')[0].split(':')[1].split()]:
            locations.append(location_finder(seed, almanac))
        return min(locations)
    return (lowest_location_finder,)


@app.cell
def _(lowest_location_finder, sample):
    lowest_location_finder(sample)
    return


@app.cell
def _():
    file_path = './data/day05.txt'
    with open(file_path) as file:
        day05 = file.read()
    day05
    return day05, file, file_path


@app.cell
def _(day05, lowest_location_finder):
    lowest_location_finder(day05)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        #Part Two
        Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes **ranges of seed numbers**.

        The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

        seeds: 79 14 55 13
        This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

        Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

        In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

        Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
        """
    )
    return


@app.cell
def _(location_finder):
    def lowest_location_finder_seed_ranges(almanac):
        # list to store locations
        locations = []
        # find seed ranges
        seed_numbers = [int(x) for x in almanac.split('\n\n')[0].split(':')[1].split()]
        seed_ranges = [(seed_numbers[i], seed_numbers[i+1]) for i in range(0, len(seed_numbers), 2)]
        # find locations of each seed in the range
        #for seed in [seed for range_start, length in seed_ranges for seed in list(range(range_start, range_start+length))]:
            #locations.append(location_finder(seed, almanac))
        for range_start, length in seed_ranges:
            modifier = 0
            while modifier < length:
                location = location_finder(range_start+modifier, almanac)
                if locations == [] or location < min(locations):
                    locations.append(location)
                modifier+=1
    
        return min(locations)
    return (lowest_location_finder_seed_ranges,)


@app.cell
def _(sample):
    nums = [int(x) for x in sample.split('\n\n')[0].split(':')[1].split()]
    ranges = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
    print(ranges)
    #seeds = [seed for seed in list(range(range_start, range_start+length)) for range_start, length in ranges]
    #seeds
    for _range_start, _length in ranges:
    #    print(range_start)
    #    print(length)
    #    print('*********')
        _seed_range = list(range(_range_start, _range_start+_length))
        print(_seed_range)

    [z for x, y in ranges for z in list(range(x, x+y))]
    return nums, ranges


@app.cell
def _(lowest_location_finder_seed_ranges, sample):
    lowest_location_finder_seed_ranges(sample)
    return


@app.cell
def _():
    #lowest_location_finder_seed_ranges(day05)
    return


@app.cell
def _():
    # The following solution functions were written with the assistance of Anthropics claude-sonnet API

    def find_mapped_ranges(input_ranges, mapping_rules):
        # Add debug print
        print(f"Processing ranges: {input_ranges}")
        print(f"With rules: {mapping_rules}")
    
        if not mapping_rules:  # Handle case with no rules
            return input_ranges
        
        # Sort mapping rules by source start for efficient processing
        sorted_rules = sorted(mapping_rules, key=lambda x: x[1])
        output_ranges = []
    
        # Process each input range
        for start, length in input_ranges:
            current = start
            end = start + length
            mapped = False
        
            # Check each mapping rule
            for dest_start, src_start, rule_length in sorted_rules:
                src_end = src_start + rule_length
            
                # If current range starts before mapping rule
                if current < src_start:
                    # Add unmapped portion
                    if current < end:
                        output_ranges.append((current, min(src_start - current, end - current)))
                    current = src_start
            
                # If current position is within mapping rule
                if current < src_end and current >= src_start and current < end:
                    # Map the overlapping portion
                    mapped_start = dest_start + (current - src_start)
                    mapped_length = min(src_end, end) - current
                    output_ranges.append((mapped_start, mapped_length))
                    current = current + mapped_length
                    mapped = True
            
                if current >= end:
                    break
                
            # Add any remaining unmapped portion
            if current < end and not mapped:
                output_ranges.append((current, end - current))
    
        print(f"Output ranges: {output_ranges}")
        return output_ranges
    return (find_mapped_ranges,)


@app.cell
def _(find_mapped_ranges):
    def improved_lowest_location_finder(almanac):
        # Parse initial seed ranges
        seed_numbers = [int(x) for x in almanac.split('\n\n')[0].split(':')[1].split()]
        ranges = [(seed_numbers[i], seed_numbers[i+1]) for i in range(0, len(seed_numbers), 2)]
    
        print(f"Initial ranges: {ranges}")
        current_ranges = ranges
    
        # Process each mapping section
        for section in almanac.split('\n\n')[1:]:
            print(f"\nProcessing section:\n{section}")
            # Parse mapping rules
            rules = []
            for line in section.splitlines()[1:]:
                numbers = [int(x) for x in line.split()]
                dest_start, src_start, length = numbers
                rules.append((dest_start, src_start, length))
            
            # Apply mapping rules to current ranges
            current_ranges = find_mapped_ranges(current_ranges, rules)
            print(f"After mapping: {current_ranges}")
    
        # Find minimum start value from final ranges
        if not current_ranges:
            return None
        return min(start for start, _ in current_ranges)
    return (improved_lowest_location_finder,)


@app.cell
def _(improved_lowest_location_finder, sample):
    # Test with a smaller subset of the input first
    test_result = improved_lowest_location_finder(sample)
    print(f"\nTest result: {test_result}")
    return (test_result,)


@app.cell
def _(improved_lowest_location_finder, sample):
    # Test with sample first
    print("Sample result:", improved_lowest_location_finder(sample))
    return


@app.cell
def _(day05, improved_lowest_location_finder):
    # Then with full input
    print("Full input result:", improved_lowest_location_finder(day05))
    return


@app.cell
def _():
    initial_ranges = [(79, 14), (55, 13)]
    seed_soil_map = [(50, 98, 2), (52, 50, 48)]
    return initial_ranges, seed_soil_map


@app.cell
def _():
    def range_processor(source_ranges, rules):
        for range in source_ranges:
            input_range_start, range_len = range
            for rule in rules:
                dest_range_start, source_range_start, rule_len = rule
                print(input_range_start, range_len)
                print(dest_range_start, source_range_start, rule_len)
                if input_range_start > source_range_start:
                    if (input_range_start+range_len-1) < (source_range_start+rule_len-1):
                        output_range = (input_range_start+(dest_range_start-source_range_start), range_len)
                        print(output_range)
                    
        return output_range
    return (range_processor,)


@app.cell
def _(initial_ranges, range_processor, seed_soil_map):
    range_processor(initial_ranges, seed_soil_map)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
