import json
from urllib.request import urlopen

base_url = "https://fr.openfoodfacts.org/cgi/"


def search(label):
    url = base_url + f"search.pl?action=process&search_terms={label}&page_size=20&json=1"
    with urlopen(url) as response:
        products = json.load(response)['products']
    return products


# Infos aliment
def infos(id):
    pass


# Tops 10 par catégories (classement "nutriscore" & "alphabet")
def top(categorie_id, classement):
    pass


# Favoris volatiles
def add_favorite(id):
    pass


def remove_favorite(id):
    pass


def get_favorites():
    pass


# BONUS: alternatives aux aliments (même catégorie)
def alternatives(id):
    pass
