from croupier import fortune_teller
from deck_writer import write_deck, fetch_deck
from pprint import pprint
import os.path

# checks to see if csv exists
# if not, runs functions to scrape and format card info
if not os.path.exists('tarot_deck.csv'):
    write_deck()

# retrieves info from csv file
tarot_deck = fetch_deck()

# fortune contains information w/o visual output unless printed
fortune = fortune_teller(deck=tarot_deck, spread=4)

# prints fortune data
for card in fortune:
    pprint(list(card.values()))


