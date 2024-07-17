from ScraperService import ScraperService
import textwrap

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
