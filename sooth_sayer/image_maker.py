import requests
from bs4 import BeautifulSoup


class MirrorMirror:
    def __init__(self):

        response = requests.get(
            url=f'https://en.wikipedia.org/wiki/Rider-Waite_tarot_deck')
        response.raise_for_status()
        source = response.text
        self.document = BeautifulSoup(source, 'html.parser')

        # finds card face images
        def fetch_images(doc):
            raw_images = doc.find_all('img')
            raw_images_list = []

            for i in raw_images:
                a = i['src'][2:]
                # ad hoc error handling — source website switches between .webp and .jpg
                if '.webp' in a:
                    raw_images_list.append(a)
                elif '.jpg' in a:
                    raw_images_list.append(a)

            return raw_images_list

        # reformats card face images by house
        def arrange_images(sources):

            sorted_imgs = {'major_arcana': [], 'wands': [], 'cups': [], 'swords': [], 'pentacles': [], }

            maj_imgs = []
            wands_imgs = []
            pent_imgs = []
            sword_imgs = []
            cups_imgs = []

            # checks for house name in entry
            for i in sources:
                if 'Wands' in i:
                    wands_imgs.append(i)
                elif 'Pents' in i:
                    pent_imgs.append(i)
                elif 'Cups' in i:
                    cups_imgs.append(i)
                elif 'Swords' in i:
                    sword_imgs.append(i)
                else:
                    maj_imgs.append(i)

            # add entries to dictionary
            sorted_imgs['major_arcana'] = maj_imgs
            sorted_imgs['wands'] = wands_imgs
            sorted_imgs['cups'] = cups_imgs
            sorted_imgs['swords'] = sword_imgs
            sorted_imgs['pentacles'] = pent_imgs

            return sorted_imgs

        imgs = fetch_images(doc=self.document)
        self.formatted_images = arrange_images(sources=imgs)
