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
        #Day 4: Scratchcards
        The gondola takes you up. Strangely, though, the ground doesn't seem to be coming with you; you're not climbing a mountain. As the circle of Snow Island recedes below you, an entire new landmass suddenly appears above you! The gondola carries you to the surface of the new island and lurches into the station.

        As you exit the gondola, the first thing you notice is that the air here is much warmer than it was on Snow Island. It's also quite humid. Is this where the water source is?

        The next thing you notice is an Elf sitting on the floor across the station in what seems to be a pile of colorful square cards.

        "Oh! Hello!" The Elf excitedly runs over to you. "How may I be of service?" You ask about water sources.

        "I'm not sure; I just operate the gondola lift. That does sound like something we'd have, though - this is Island Island, after all! I bet the gardener would know. He's on a different island, though - er, the small kind surrounded by water, not the floating kind. We really need to come up with a better naming scheme. Tell you what: if you can help me with something quick, I'll let you borrow my boat and you can go visit the gardener. I got all these scratchcards as a gift, but I can't figure out what I've won."

        The Elf leads you over to the pile of colorful cards. There, you discover dozens of scratchcards, all with their opaque covering already scratched off. Picking one up, it looks like each card has two lists of numbers separated by a vertical bar (|): a list of winning numbers and then a list of numbers you have. You organize the information into a table (your puzzle input).

        As far as the Elf has been able to figure out, you have to figure out which of the numbers you have appear in the list of winning numbers. The first match makes the card worth one point and each match after the first doubles the point value of that card.

        For example:
        ```
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        ```
        In the above example, card 1 has five winning numbers (41, 48, 83, 86, and 17) and eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53). Of the numbers you have, four of them (48, 83, 17, and 86) are winning numbers! That means card 1 is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

        Card 2 has two winning numbers (32 and 61), so it is worth 2 points.
        Card 3 has two winning numbers (1 and 21), so it is worth 2 points.
        Card 4 has one winning number (84), so it is worth 1 point.
        Card 5 has no winning numbers, so it is worth no points.
        Card 6 has no winning numbers, so it is worth no points.
        So, in this example, the Elf's pile of scratchcards is worth 13 points.

        Take a seat in the large pile of colorful cards. How many points are they worth in total?
        """
    )
    return


@app.cell
def _():
    sample = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
    return (sample,)


@app.cell
def _(sample):
    sample_card = sample.splitlines()[0]
    return (sample_card,)


@app.cell
def _(sample_card):
    sample_card.split(': ')
    return


@app.cell
def _(sample_card):
    sample_card.split(': ')[1].split(' | ')
    sample_card_winners = sample_card.split(': ')[1].split(' | ')[0]
    sample_card_nums = sample_card.split(': ')[1].split(' | ')[1]
    print(sample_card_winners)
    print(sample_card_nums)
    return sample_card_nums, sample_card_winners


@app.cell
def _(sample_card_nums):
    sample_card_nums.split()
    return


@app.cell
def _():
    def split_card(card):
        card_num = card.split(': ')[0].split()[1]
        winning_numbers = card.split(': ')[1].split(' | ')[0].split()
        lottery_numbers = card.split(': ')[1].split(' | ')[1].split()
        return card_num, winning_numbers, lottery_numbers
    return (split_card,)


@app.cell
def _(sample_card, split_card):
    split_card(sample_card)
    return


@app.cell
def _():
    def point_check(winning_numbers, lottery_numbers):
        #print(winning_numbers)
        matches = 0
        for n in winning_numbers:
            #print(f'Num: {n}')
            if n in lottery_numbers:
                matches += 1
                #print(f'Matches: {matches}')
            #print('*'*10)
        if matches == 0:
            points = 0
        else:
            points = 2**(matches-1)
        return points
    return (point_check,)


@app.cell
def _(point_check, sample, split_card):
    point_check(split_card(sample)[1], split_card(sample)[2])
    return


@app.cell
def _(point_check, split_card):
    def card_points(cards):
        # running count of points
        points = 0
        # loop through each card in list of cards
        for card in cards.splitlines():
            # check the points for the card and add to the total
            points += point_check(split_card(card)[1], split_card(card)[2])
        return points
    return (card_points,)


@app.cell
def _(card_points, sample):
    card_points(sample)
    return


@app.cell
def _():
    # we need to read in the text file that we want to run our function on
    file_path = './data/day04.txt'

    with open(file_path, "r", encoding="utf-8") as file:
            day04 = file.read()
    day04
    return day04, file, file_path


@app.cell
def _(card_points, day04):
    card_points(day04)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        #Part Two
        Just as you're about to report your findings to the Elf, one of you realizes that the rules have actually been printed on the back of every card this whole time.

        There's no such thing as "points". Instead, scratchcards only cause you to win more scratchcards equal to the number of winning numbers you have.

        Specifically, you win copies of the scratchcards below the winning card equal to the number of matches. So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.

        Copies of scratchcards are scored like normal scratchcards and have the same card number as the card they copied. So, if you win a copy of card 10 and it has 5 matching numbers, it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)

        This time, the above example goes differently:

        ```
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        ```

        Card 1 has four matching numbers, so you win one copy each of the next four cards: cards 2, 3, 4, and 5.
        Your original card 2 has two matching numbers, so you win one copy each of cards 3 and 4.
        Your copy of card 2 also wins one copy each of cards 3 and 4.
        Your four instances of card 3 (one original and three copies) have two matching numbers, so you win four copies each of cards 4 and 5.
        Your eight instances of card 4 (one original and seven copies) have one matching number, so you win eight copies of card 5.
        Your fourteen instances of card 5 (one original and thirteen copies) have no matching numbers and win no more cards.
        Your one instance of card 6 (one original) has no matching numbers and wins no more cards.
        Once all of the originals and copies have been processed, you end up with 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances of card 4, 14 instances of card 5, and 1 instance of card 6. In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards!

        Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, how many total scratchcards do you end up with?


        """
    )
    return


@app.cell
def _():
    cards = [1, 2, 3]
    for card in cards:
        print(card)
        #cards.append(card)
    return card, cards


@app.cell
def _():
    def matches_check(winning_numbers, lottery_numbers):
        #print(winning_numbers)
        matches = 0
        for n in winning_numbers:
            #print(f'Num: {n}')
            if n in lottery_numbers:
                matches += 1
                #print(f'Matches: {matches}')
            #print('*'*10)
        return matches
    return (matches_check,)


@app.cell
def _(matches_check, sample_card, split_card):
    matches_check(split_card(sample_card)[1], split_card(sample_card)[2])
    return


@app.cell
def _():
    return


@app.cell
def _(matches_check, sample, split_card):
    def winning_copies(cards):
        # list of card copies won
        card_copies = []
        cards = cards.splitlines()
        # loop through each card, labeling with index
        for card_idx, card in enumerate(cards):
            # find quantity of matches in card
            matches = matches_check(split_card(card)[1], split_card(card)[2])
            print(f'Card {card_idx+1} has {matches} matches')
            # 
            for i in list(range(0, matches)):
                card_copies.append(cards[card_idx+i+1])
                #print(f'Copy of Card {card_idx+i+2} added for match {i+1}')
            #print('*'*10)
        print(len(card_copies))
        for card in card_copies:
            card_number, winning_numbers, lottery_numbers = split_card(card)
            matches = matches_check(winning_numbers, lottery_numbers)
            for i in list(range(0, matches)):
                card_copies.append(cards[int(card_number)+i])
        #print('*'*10)
        #print(card_copies)
        print(len(cards) + len(card_copies))

    winning_copies(sample)
    return (winning_copies,)


@app.cell
def _():
    #winning_copies(day04)
    return


@app.cell
def _(matches_check, sample, split_card):
    def winning_copies_samp(cards):
        # list of card copies won
        card_copies = []
        cards = cards.splitlines()
        # loop through each card, labeling with index
        for card_idx, card in enumerate(cards):
            # find quantity of matches in card
            matches = matches_check(split_card(card)[1], split_card(card)[2])
            print(f'Card {card_idx+1} has {matches} matches')
            # 
            for i in list(range(0, matches)):
                card_copies.append((card_idx, matches))
                #print(f'Copy of Card {card_idx+i+2} added for match {i+1}')
            #print('*'*10)
        print(len(card_copies))
        #for card in card_copies:
        
        #print('*'*10)
        #print(card_copies)
        print(len(cards) + len(card_copies))
        print(card_copies)
    winning_copies_samp(sample)
    return (winning_copies_samp,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
