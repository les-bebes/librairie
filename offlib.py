import json
from urllib.request import urlopen

base_url_search = "https://fr.openfoodfacts.org/cgi/"
base_url_infos = "https://world.openfoodfacts.org/api/v0/"

favorties = list()


def search(label):
    url = f"{base_url_search}search.pl?action=process&search_terms={label}&page_size=20&json=1"
    with urlopen(url) as response:
        products = json.load(response)['products']
    return products


# Infos aliment
def infos(product_id):
    url = f"{base_url_infos}product/{product_id}.json"
    with urlopen(url) as response:
        product = json.load(response)['product']
    return product


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


# BONUS: alternatives aux aliments (même catégorie)
def alternatives(id):
    pass
