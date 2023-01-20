import json
from datetime import datetime
from random import choice

from models import Author, Quote

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

def load_authors_into_db(filename):
    data: dict = load_json(filename)
    for author in data:
        Author(fullname=author['fullname'],
                born_date=datetime.strptime(author['born_date'], "%B %d, %Y").date(),
                born_location=author['born_location'],
                description=author['description']).save()

def load_quotes_into_db(filename):
    data: dict = load_json(filename)
    authors = Author.objects()
    for quote in data:
        Quote(tags=quote['tags'],
                author=(choice(authors)).id,
                quote=quote['quote']).save()


if __name__ == '__main__':
    load_authors_into_db(r'json_data\authors.json')
    load_quotes_into_db(r'json_data\quotes.json')