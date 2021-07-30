from sooth_sayer.major_maker import MajorMaker
from sooth_sayer.minor_maker import MinorMaker
import csv
import pandas


# this function should only be run in the absence of an extant csv file
# saves time scraping, prevents bot flagging, makes data static
def write_deck():
    major_arcana = MajorMaker().major_cards
    minor_arcana = MinorMaker().minor_cards

    deck = major_arcana + minor_arcana

    with open('tarot_deck.csv', 'a', newline='') as file:
        fields = ['name', 'img_url', 'meaning_upright', 'meaning_reversed']
        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        for card in deck:
            writer.writerow({'name': card['name'], 'img_url': card['img_url'],
                             'meaning_upright': card['meaning']['Upright'],
                             'meaning_reversed': card['meaning']['Reversed']})

def fetch_deck():
    df = pandas.read_csv('tarot_deck.csv')
    # translates df to iterrable dictionary
    card_dict = df.to_dict('index')

    d = []

    # reformats entries into recognizable template
    # with the addition of an id inherited from csv/dataframe
    for i in card_dict:
        card = {
            'id': i,
            'name': card_dict[i]['name'],
            'img_url': card_dict[i]['img_url'],
            'meaning': {'Upright': card_dict[i]['meaning_upright'],
                        'Reversed': card_dict[i]['meaning_reversed']},
        }
        d.append(card)

    return d
