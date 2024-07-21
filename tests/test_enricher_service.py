import pytest
from src.EnricherService import EnricherService


# Es para simular que si enriquezca
def mock_requests_post_success(url, json, headers):
    class MockResponse:
        @staticmethod
        def json():
            return {"status": "success", "data": {"outputs": [{"text": "Texto enriquecido"}]}}
    return MockResponse()

# Y este para cuando no enriquezca
def mock_requests_post_failure(url, json, headers):
    class MockResponse:
        @staticmethod
        def json():
            return {"status": "error", "message": "Internal Server Error"}
    return MockResponse()

@pytest.fixture
def enricher_service(monkeypatch):
    monkeypatch.setenv('API_KEY', 'test_api_key')
    monkeypatch.setenv('API_URL', 'https://api.test.com')
    return EnricherService()

def test_enrich_success(enricher_service, monkeypatch):
    # Verifica enriquecimiento
    monkeypatch.setattr('requests.post', mock_requests_post_success)
    assert enricher_service.enrich("Texto de prueba") == "Texto enriquecido"

def test_enrich_failure(enricher_service, monkeypatch):
    # Verifica que hay un problema en el enriquecimiento y regresaria el None
    monkeypatch.setattr('requests.post', mock_requests_post_failure)
    assert enricher_service.enrich("Texto de prueba") is None