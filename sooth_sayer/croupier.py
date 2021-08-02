import random


# determines positional of the card
def flip_card():
    pos = [0, 1]
    position = random.choice(pos)

    if position == 0:
        return 'Upright'
    elif position == 1:
        return 'Reversed'

# selects and compiles cards given a chosen spread, deck
def fortune_teller(deck, spread):
    reading = []
    check = []
    while len(reading) < spread:
        for _ in range(spread):
            card = random.choice(deck)
            position = flip_card()
            fortune = {
                'id': card['id'],
                'name': card['name'],
                'img_url': card['img_url'],
                # indicates the position, though should be visual reference as well
                'meaning': f'{position}: ' + card['meaning'][position],
            }
            # check ensures no duplicates by card id
            if card['id'] not in check:
                reading.append(fortune)
                check.append(card['id'])

    return reading
