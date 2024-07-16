import requests
import string
from bs4 import BeautifulSoup
import textwrap

enter_input = input("Search: ")
u_i = string.capwords(enter_input)
word_list = u_i.split()
word = "_".join(word_list)

url = "https://es.wikipedia.org/wiki/" + word

def wiki_search(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    paragraphs = soup.find_all('p')
    wrapper = textwrap.TextWrapper(width=100)
    for i in range(min(5, len(paragraphs))):
        paragraph_text = paragraphs[i].text.strip()
        wrapped_text = wrapper.fill(paragraph_text)
        print(wrapped_text)
        print()

wiki_search(url)