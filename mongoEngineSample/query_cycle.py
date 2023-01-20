from models import Author, Quote
from pprint import pprint

def output_response(response):
    for record in response:
        print(record.to_json())
    
def query_db_cycle():
    authors = Author.objects
    quotes = Quote.objects
    while True:
        command: str = input("Enter query(command:values): ")

        if command.lower() == 'exit':
            break

        command, values = command.split(":")

        if command.lower() == "name":
            print(f"Authors with name '{values}':")
            output_response(authors(fullname__istartswith=values))

        elif command.lower() == "tag":
            if ',' in values:
                values = values.split(',')
                for value in values:
                    print(f"Quotes with tag '{value}':")
                    output_response(quotes(tags__contains=value))
            else:
                print(f"Quotes with tag '{values}':")
                output_response(quotes(tags__contains=values))
        

if __name__ == '__main__':

    query_db_cycle()
        