import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter


base_url = "http://quotes.toscrape.com/"


def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        response = requests.get(f"{base_url}{url}")
        print(f"Now Scraping {base_url}{url}...")
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")

        for quote in quotes:
            all_quotes.append({
                "text": quote.find(class_="text").get_text(),
                "author": quote.find(class_="author").get_text(),
                "Bio_link": quote.find("a")["href"]
            })
        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
    print(all_quotes)
    return all_quotes


def start_games(get_quotes):
    quote = choice(get_quotes)
    remaining_guesses = 4
    print("Here´s a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess = " "
    while guess.lower() != quote["author"].lower() and remaining_guesses > 0:
        guess = input(f"Who said this quote? Guess remaining: {remaining_guesses} ")
        if guess.lower() == quote["author"].lower():
            print("You got it right!")
            break
        remaining_guesses -= 1
        if remaining_guesses == 3:
            inf_author = requests.get(f"{base_url}{quote['Bio_link']}")
            Soup = BeautifulSoup(inf_author.text, "html.parser")
            birth_date = Soup.find(class_="author-born-date").get_text()
            birth_place = Soup.find(class_="author-born-location").get_text()
            print(f"Here´s a hint: The author was born on {birth_date} {birth_place} ")
        elif remaining_guesses == 2:
            print(f"Here´s a second hint: The author´s first name, stars with: {quote['author'][0]}")
        elif remaining_guesses == 1:
            last_initial = quote["author"].split(" ")[1][0]
            print(f"Here´s a second hint: The author´s last name, stars with: {last_initial}")
        else:
            print(f"Sorry you ran out of guesses. The answer was {quote['author']}")

    again = ' '
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again Y/N ?")
        if again.lower() in ('y', 'yes'):
            return start_games(get_quotes)
        else:
            print("Goodbye")


get_quotes = scrape_quotes()
start_games(get_quotes)
