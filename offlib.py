import json
from urllib.request import urlopen

base_url_fr = "https://fr.openfoodfacts.org"
base_url_ww = "https://world.openfoodfacts.org/api/v0"

favorties = list()


def search(label):
    url = f"{base_url_fr}/cgi/search.pl?action=process&search_terms={label}&page_size=20&json=1"
    with urlopen(url) as response:
        products = json.load(response)['products']
    return products


# Infos aliment
def infos(product_id):
    url = f"{base_url_ww}/product/{product_id}.json"
    with urlopen(url) as response:
        product = json.load(response)['product']
    return product


def categories():
    url = f"{base_url_fr}/categories.json"
    with urlopen(url) as response:
        cats = json.load(response)['tags']
    return cats


# Tops 10 par catégories (classement "nutriscore" & "alphabet")
def top(categorie_id, classement):
    pass


# Favoris volatiles
def add_favorite(product_id):
    if product_id not in favorties:
        favorties.append(product_id)


def remove_favorite(product_id):
    if product_id in favorties:
        favorties.remove(product_id)


def get_favorites():
    return favorties
