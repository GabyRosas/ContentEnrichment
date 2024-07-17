import os
import requests
import string
from bs4 import BeautifulSoup
import textwrap
from dotenv import load_dotenv

load_dotenv()


class ScraperService:
    def __init__(self):
        self.base_url = os.getenv('WIKI_URL_BASE')

    def get_wiki_content(self, search_query):
        try:
            formatted_query = self.format_content(search_query)
            url = self.base_url + formatted_query
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            paragraphs = soup.find_all('p')
            return paragraphs
        except requests.exceptions.RequestException as e:
            print(f'Error de red: {e}')
            return []
        except ValueError as e:
            print(f'Error: {e}')
            return []

    def format_content(self, content):
        capitalized_content = string.capwords(content)
        word_list = capitalized_content.split()
        formatted_content = "_".join(word_list)
        return formatted_content


if __name__ == "__main__":
    scraper_service = ScraperService()
    search_query = input("Search: ")
    paragraphs = scraper_service.get_wiki_content(search_query)

    wrapper = textwrap.TextWrapper(width=100)
    for i in range(min(5, len(paragraphs))):
        paragraph_text = paragraphs[i].text.strip()
        wrapped_text = wrapper.fill(paragraph_text)
        print(wrapped_text)
        print()



