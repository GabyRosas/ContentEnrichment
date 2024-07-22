import os
import re
import requests
import string
from bs4 import BeautifulSoup
import textwrap
from dotenv import load_dotenv

load_dotenv()


class ScraperService:
    def __init__(self):
        try:
            self.base_url = os.getenv('WIKI_URL_BASE')
            if not self.base_url:
                raise ValueError("La URL base no está configurada en el archivo .env")
        except Exception as e:
            print(f'Error al cargar la URL base: {e}')
            self.base_url = ""

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
            cleaned_paragraphs = [self.remove_text_patterns(self.remove_zwsp(p.text)) for p in paragraphs]
            return cleaned_paragraphs
        except requests.exceptions.RequestException as e:
            print(f'Error de red: El tema ingresado no existe o está mal escrito')
            raise
        except ValueError as e:
            print(f'Error: {e}')
            raise
        except Exception as e:
            print(f'Ocurrió un error: {e}')
            raise


    def format_content(self, content):
        try:
            capitalized_content = string.capwords(content)
            word_list = capitalized_content.split()
            formatted_content = "_".join(word_list)
            return formatted_content
        except Exception as e:
            print(f'Error al formatear el contenido: {e}')
            return ""


    def format_paragraphs(self, paragraphs, width=100, max_paragraphs=6):
        try:
            wrapper = textwrap.TextWrapper(width=width)
            formatted_paragraphs = []
            for i in range(min(max_paragraphs, len(paragraphs))):
                paragraph_text = paragraphs[i].strip()
                wrapped_text = wrapper.fill(paragraph_text)
                formatted_paragraphs.append(wrapped_text)
            return formatted_paragraphs
        except Exception as e:
            print(f'Error al formatear los párrafos: {e}')
            return []


    def remove_zwsp(self, text):
        try:
            zwsp_chars = ['\u200b', '\u200c', '\u200d', '\uFEFF']
            for char in zwsp_chars:
                text = text.replace(char, '')
            return text
        except Exception as e:
            print(f'Error al eliminar ZWSP: {e}')
            return text


    def remove_text_patterns(self, text):
        try:
            text = re.sub(r'\[\d+\]', '', text)
            text = re.sub(r'\[nota \d+\]', '', text)
            text = re.sub(r'\[\d+ nota\]', '', text)
            text = re.sub(r'\[\w+\]', '', text)
            return text
        except Exception as e:
            print(f'Error al eliminar patrones de texto: {e}')
            return text


