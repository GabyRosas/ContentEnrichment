from .ScraperService import ScraperService
from .TranslatorService import TranslatorService
from src.FileManager import Content
from utils.ChooseFile import ChooseFile
from utils.input_handler import get_user_input
from .EnricherService import EnricherService
import sys

class ContentEnricher:
    @staticmethod
    def main():
        try:
            scraper_service = ScraperService()
            search_query = get_user_input("Introduce el término de búsqueda: ")
            paragraphs = scraper_service.get_wiki_content(search_query)
            formatted_paragraphs = scraper_service.format_paragraphs(paragraphs)

            content = Content()
            original_paragraphs = "\n\n".join(formatted_paragraphs)
            content.set_original_content(original_paragraphs)

            print("\nContenido Original:\n")
            print(original_paragraphs)
            print()

            src_lang_input = get_user_input('Tu lenguaje: ')
            tgt_lang_input = get_user_input('Lenguaje deseado: ')
            translated_paragraphs = TranslatorService.translate_paragraphs(formatted_paragraphs, src_lang_input,tgt_lang_input)

            version_translator = "\n\n".join(translated_paragraphs)
            content.set_translated_content(version_translator)
            print("\nContenido Traducido:\n")
            print(version_translator)
            print()

            enriched_content = EnricherService.enrich(original_paragraphs)

            version_plus = "\n".join(enriched_content)
            content.set_enriched_content(version_plus)

            print("\nAhora te mostraremos el contenido Enriquecido:\n")
            print(version_plus)
            print()

            ChooseFile().main(content)

        except Exception as e:
            print(f'Error crítico: {e}')
            sys.exit(1)
