import requests
import string
from bs4 import BeautifulSoup

enter_input = input("Search: ")
u_i = string.capwords(enter_input)
word_list = u_i.split()
word = "_".join(word_list)

url = "https://es.wikipedia.org/wiki/"+word

def wiki_search(url):
    url_open = requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    details = soup.find_all('table',{'class':'infobox'})
    for i in details:
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and detail is not None:
                for x,y in zip(heading,detail):
                    print("{}  ::  {}".format(x.text, y.text))
                    print("------------------")
    paragraphs = soup.find_all('p')
    for i in range(min(5, len(paragraphs))):
        print(paragraphs[i].text)
wiki_search(url)

