from math import floor
from time import time

INPUT_FILE = "input.txt"
with open(INPUT_FILE, 'r') as file:
    cards = file.readlines()

cache = {}
def get_cards(card_row: int, caching: bool = True) -> int:
        """Returns the number of cards acquired from this card."""
        
        if card_row >= len(cards):
             return 0

        # Check cache
        if caching:
            try:
                return cache[card_row]
            except KeyError:
                pass

        # Get winners and pulled nums
        numbers = cards[card_row].split(":")[1]
        winners, my_numbers = numbers.split("|")

        winners = set(winners.split())
        my_numbers = my_numbers.split()

        # Find matches
        matches = 0
        for num in my_numbers:
            if num in winners:
                matches += 1

        # Recursively find cards from next rows
        acquired_cards = 1 + sum([get_cards(card_row+offset, caching) for offset in range(1, matches+1)])
        cache[card_row] = acquired_cards
        return acquired_cards

start = time()
total = 0
ENABLE_CACHING = True
for card_row in range(len(cards)):
    total += get_cards(card_row, ENABLE_CACHING)
end = time()

print(total)
print(f"Algo Runtime: {round((end - start), 4)}s")