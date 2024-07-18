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
            title = soup.find_all('h1')
            parag = soup.find_all('p')
            paragraphs = title + parag
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

    def format_paragraphs(self, paragraphs, width=100, max_paragraphs=5):
        wrapper = textwrap.TextWrapper(width=width)
        formatted_paragraphs = []
        for i in range(min(max_paragraphs, len(paragraphs))):
            paragraph_text = paragraphs[i].text.strip()
            wrapped_text = wrapper.fill(paragraph_text)
            formatted_paragraphs.append(wrapped_text)
        return formatted_paragraphs