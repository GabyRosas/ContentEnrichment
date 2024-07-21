import pytest
from requests.exceptions import HTTPError
from src.ScraperService import ScraperService


@pytest.fixture
def scraper_service():
    return ScraperService()


def test_valid_search(scraper_service, monkeypatch):

    monkeypatch.setenv('WIKI_URL_BASE', 'https://es.wikipedia.org/wiki/')

    search_query = "Python"
    paragraphs = scraper_service.get_wiki_content(search_query)

    assert len(paragraphs) > 0, "No se obtuvieron párrafos para una búsqueda válida"


def test_invalid_search(scraper_service, monkeypatch):
    monkeypatch.setenv('WIKI_URL_BASE', 'https://es.wikipedia.org/wiki/')

    search_query = "fgjdfgjdfgjdfgjdfgj"

    with pytest.raises(HTTPError):
        scraper_service.get_wiki_content(search_query)

