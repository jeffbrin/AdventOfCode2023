from math import floor

INPUT_FILE = "input.txt"
with open(INPUT_FILE, 'r') as file:
    cards = file.readlines()

total = 0
for card in cards:
    numbers = card.split(":")[1]
    winners, my_numbers = numbers.split("|")

    winners = set(winners.split())
    my_numbers = my_numbers.split()

    matches = 0
    for num in my_numbers:
        if num in winners:
           matches += 1

    # Remove 2^-1
    total += floor(2 ** (matches-1))

print(total) 