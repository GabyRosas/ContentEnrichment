from utils.ChooseFile import ChooseFile
from ScraperService import ScraperService
from utils.input_handler import get_user_input
from utils.TranslatorText import TranslatorService

#Aquí es donde tenemos que poner los bucles para que vaya primero una cosa u otra.
class ContentEnricher:
    def main(self):
        scraper_service = ScraperService()
        search_query = get_user_input("Search: ")
        paragraphs = scraper_service.get_wiki_content(search_query)
        formatted_paragraphs = scraper_service.format_paragraphs(paragraphs)
        for paragraph in formatted_paragraphs:
            print(paragraph)
            print()

        ScraperService().main()
        ChooseFile().main()


if __name__ == "__main__":
    ContentEnricher().main()

