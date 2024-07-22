import pytest
import requests
from src.EnricherService import EnricherService


def mock_requests_post_success(url, json, headers):
    class MockResponse:
        @staticmethod
        def json():
            return {"status": "success", "data": {"outputs": [{"text": "Texto enriquecido"}]}}
    return MockResponse()


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
    monkeypatch.setattr(requests, 'post', mock_requests_post_success)
    expected_output = EnricherService.wrap_text("Texto enriquecido", 100).split('\n')
    assert enricher_service.enrich("Texto de prueba") == expected_output


def test_enrich_failure(enricher_service, monkeypatch):
    monkeypatch.setattr(requests, 'post', mock_requests_post_failure)
    assert enricher_service.enrich("Texto de prueba") is None

