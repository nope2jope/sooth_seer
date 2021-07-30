from sooth_sayer.image_maker import MirrorMirror
import requests
import re
from bs4 import BeautifulSoup


class MajorMaker:
    def __init__(self):
        self.template = {
            'name': '',
            'id': '',
            'img_url': '',
            'meaning': {
                'Upright': '',
                'Reversed': '',
            }
        }

        response = requests.get(url='https://www.alittlesparkofjoy.com/tarot-cards-list/')
        response.raise_for_status()
        source = response.text

        self.document = BeautifulSoup(source, 'html.parser')

        # splits text elements by first instance of capitals (i.e. "Foo barFoobar" -> ["Foo bar", "Foobar"]
        def break_string(string):
            output = filter(None, re.split("([A-Z][^A-Z]*)", string))
            d = [e for e in output]
            return d

        # finds card name
        def fetch_labels(doc):
            labels = doc.find_all('h4')
            labels_list = []

            for label in labels:
                if "(" in label.text:
                    l = label.text
                    labels_list.append(l)

            return labels_list

        # finds and formats simple card meanings
        def fetch_majors(doc):
            majors = doc.find_all(class_='wp-block-table')
            majors_list = []

            for entry in majors:
                m_data = break_string(entry.text)
                majors_list.append(m_data)

            return majors_list

        # compile and formats list elements into maj arcana dictionary
        def compile_majors(labels, majors, images):
            deck = []
            ids = [i for i in range(22)]
            for i in ids:
                card_name = labels[i].split(str(i))[0].strip('()').rstrip()
                card = {
                    'name': card_name,
                    'img_url': images[i],
                    'meaning': {
                        'Upright': majors[i][1],
                        'Reversed': majors[i][3],
                    }
                }
                deck.append(card)
            return deck

        # images retrieved from image_maker module
        l = fetch_labels(doc=self.document)
        m = fetch_majors(doc=self.document)
        i = MirrorMirror().formatted_images['major_arcana']

        # overall output of the Class
        self.major_cards = compile_majors(labels=l, majors=m, images=i)
