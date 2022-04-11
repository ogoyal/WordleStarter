# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import requests
from bs4 import BeautifulSoup


def get_page():
    URL = "https://www.stockq.org/life/wordle-answers.php"
    page = requests.get(URL)
    return page


def all_five_letter_words():
    word_site = "http://www.instructables.com/files/orig/FLU/YE8L/H82UHPR8/FLUYE8LH82UHPR8.txt"
    page = requests.get(word_site)
    word_list = page.text.split()
    return {word for word in word_list if len(word) == 5}


if __name__ == '__main__':
    page = get_page()
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("td")
    words = set()
    for result in results:
        if len(result.text) == 5:
            words.add(result.text.lower())

    five_letter_words = all_five_letter_words()
    remaining_words = five_letter_words - words
    choice = random.choice(tuple(remaining_words))
    print(choice)
