from ChooseFile import ChooseFile
from ScraperService import ScraperService
from input_handler import get_user_input

if __name__ == "__main__":
    scraper_service = ScraperService()
    search_query = get_user_input("Search: ")
    paragraphs = scraper_service.get_wiki_content(search_query)
    formatted_paragraphs = scraper_service.format_paragraphs(paragraphs)
    for paragraph in formatted_paragraphs:
        print(paragraph)
        print()

if __name__ == "__main__":
    ChooseFile().main()


