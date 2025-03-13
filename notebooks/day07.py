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
        #Day 7: Camel Cards
        Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a cool airship!) It drops you off at the edge of a vast desert and descends back to Island Island.

        "Did you bring the parts?"

        You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

        "Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

        "The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

        After riding a bit across the sands of Desert Island, you can see what look like very large rocks covering half of the horizon. The Elf explains that the rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

        You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

        Because the journey will take a few days, she offers to teach you the game of Camel Cards. Camel Cards is sort of similar to poker except it's designed to be easier to play while riding a camel.

        In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

        Every hand is exactly one type. From strongest to weakest, they are:

        Five of a kind, where all five cards have the same label: AAAAA

        Four of a kind, where four cards have the same label and one card has a different label: AA8AA

        Full house, where three cards have the same label, and the remaining two cards share a different label: 23332

        Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98

        Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432

        One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4

        High card, where all cards' labels are distinct: 23456

        Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

        If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

        So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

        To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

        ```
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
        ```

        This example shows five hands; each hand is followed by its bid amount. **Each hand wins an amount equal to its bid multiplied by its rank**, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

        So, the first step is to put the hands in order of strength:

        32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
        KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
        T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
        Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

        **Find the rank of every hand in your set. What are the total winnings?**
        """
    )
    return


@app.cell
def _():
    sample = '''32T3K 765
    T55J5 684
    KK677 28
    KTJJT 220
    QQQJA 483'''
    sample
    return (sample,)


@app.cell
def _(sample):
    sample.splitlines()
    sample_line = sample.splitlines()[0]
    return (sample_line,)


@app.cell
def _(sample):
    cards_list = []
    for line in sample.splitlines():
        cards_list.append(line.split(' ')[0])
    cards_list
    return cards_list, line


@app.cell
def _(five, four, full_house, high, one_pair, three, two_pair):
    from collections import Counter

    def score(hand):
        chars = Counter(hand.split(' ')[0]).most_common()
        if chars[0][1] == 5:
            #print(f'{cards}: 5 of a Kind')
            return five
        elif chars[0][1] == 4:
            #print(f'{cards}: 4 of a Kind')
            return four
        elif chars[0][1] == 3 and chars[1][1] == 2:
            #print(f'{cards}: Full House')
            return full_house
        elif chars[0][1] == 3:
            #print(f'{cards}: 3 of a Kind')
            return three
        elif chars[0][1] == 2 and chars[1][1] == 2:
            #print(f'{cards}: Two Pair')
            return two_pair
        elif chars[0][1] == 2:
            #print(f'{cards}: One Pair')
            return one_pair
        else:
            #print(f'{cards}: High Card')
            return high


    return Counter, score


@app.cell
def _():
    #for _cards in cards_list:
        #score(_cards)
    return


@app.cell
def _(Counter, hand_sorter):
    # Psuedocode
    def sum_winning_wagers(hands):
        # sort all hands in file
        hands_sorted = hand_sorter(hands.splitlines())
        # score each hand and put it into lists by score
        high = []
        one_pair = []
        two_pair = []
        three = []
        full_house = []
        four = []
        five = []
    
        def score(hand):
            chars = Counter(hand.split(' ')[0]).most_common()
            if chars[0][1] == 5:
                #print(f'{cards}: 5 of a Kind')
                return five
            elif chars[0][1] == 4:
                #print(f'{cards}: 4 of a Kind')
                return four
            elif chars[0][1] == 3 and chars[1][1] == 2:
                #print(f'{cards}: Full House')
                return full_house
            elif chars[0][1] == 3:
                #print(f'{cards}: 3 of a Kind')
                return three
            elif chars[0][1] == 2 and chars[1][1] == 2:
                #print(f'{cards}: Two Pair')
                return two_pair
            elif chars[0][1] == 2:
                #print(f'{cards}: One Pair')
                return one_pair
            else:
                #print(f'{cards}: High Card')
                return high
        for hand in hands_sorted:
            score(hand).append(hand)
        
        # concat all lists together in order
        all_hands_sorted = high + one_pair + two_pair + three + full_house + four + five
        score = 0
        for i, hand in enumerate(all_hands_sorted):
            score += (i+1)*int(hand.split(' ')[1])
        return score
        

        # enumerate from lowest to highest score and multiply wager by index
    return (sum_winning_wagers,)


@app.cell
def _(sample, sum_winning_wagers):
    sum_winning_wagers(sample)
    return


@app.cell
def _():
    card_values = {card: value for value, card in enumerate('AKQJT9876543210 '[::-1])}
    card_values
    return (card_values,)


@app.cell
def _(card_values, sample):
    _hand = sample.splitlines()[0].split(' ')[0]
    print(_hand)
    [card_values[card] for card in _hand]
    return


@app.cell
def _(sample):
    def hand_sorter(hands):
        card_values = {card: value for value, card in enumerate('AKQJT9876543210 '[::-1])}

        # Key function to map each card to a value for sorting
        def key_function(hand):
            return [card_values[card] for card in hand]

        # Return sorted cards using key
        return sorted(hands, key=key_function)

    hand_sorter(sample.splitlines())
    return (hand_sorter,)


@app.cell
def _():
    test_list = ['1']
    def functional(thing):
        if thing == 1:
            return test_list.append(thing)
    functional(1)
    return functional, test_list


@app.cell
def _():
    file_path = './data/day07.txt'
    with open(file_path) as file:
        day07 = file.read()
    return day07, file, file_path


@app.cell
def _(day07, sum_winning_wagers):
    sum_winning_wagers(day07)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
