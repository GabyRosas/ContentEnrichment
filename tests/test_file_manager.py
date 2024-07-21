import pytest
from src.FileManager import FileManager, Content


def test_get_filename(monkeypatch):
    content = Content(original_content="Este es el contenido de prueba")

    monkeypatch.setattr('builtins.input', lambda _: 'testfile')
    fm = FileManager(content.original_content, 'default')
    filename = fm.get_filename('.pdf')
    assert filename == 'testfile.pdf'


def test_get_filename_with_default(monkeypatch):
    content = Content(original_content="Este es el contenido de prueba")

    monkeypatch.setattr('builtins.input', lambda _: '')
    fm = FileManager(content.original_content, 'default')
    filename = fm.get_filename('.pdf')
    assert filename == 'default.pdf'


if __name__ == '__main__':
    pytest.main()
