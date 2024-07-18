from ScraperService import ScraperService
from TranslatorService import TranslatorService
from src.FileManager import FileManager
from src.FileManager import Content

from utils.ChooseFile import ChooseFile
from utils.input_handler import get_user_input


class ContentEnricher:
    def main(self):
        scraper_service = ScraperService()
        search_query = get_user_input("Introduce el término de búsqueda: ")
        paragraphs = scraper_service.get_wiki_content(search_query)
        formatted_paragraphs = scraper_service.format_paragraphs(paragraphs)

        content = Content()
        content.set_original_content("\n\n".join(formatted_paragraphs))

        print("\nContenido Original:\n")
        for paragraph in formatted_paragraphs:
            print(paragraph)
            print()

        src_lang_input = get_user_input('Tu lenguaje: ')
        tgt_lang_input = get_user_input('Lenguaje deseado: ')
        translated_paragraphs = TranslatorService.translate_paragraphs(formatted_paragraphs, src_lang_input,
                                                                       tgt_lang_input)

        content.set_translated_content("\n\n".join(translated_paragraphs))

        print("\nContenido Traducido:\n")
        for translated_paragraph in translated_paragraphs:
            print(translated_paragraph)
            print()

        ChooseFile().main(content)


if __name__ == "__main__":
    ContentEnricher().main()

