import pytest
from src.FileManager import FileManager, Content
# Test para get_filename
def test_get_filename(monkeypatch):
    # Simula la entrada del usuario
    monkeypatch.setattr('builtins.input', lambda _: 'testfile')
    fm = FileManager(Content.original_content, 'default')
    filename = fm.get_filename('.pdf')
    assert filename == 'testfile.pdf'

def test_get_filename_with_default(monkeypatch):
    # Simula una entrada vacía del usuario
    monkeypatch.setattr('builtins.input', lambda _: '')
    fm = FileManager(Content.original_content, 'default')
    filename = fm.get_filename('.pdf')
    assert filename == 'default.pdf'

if __name__ == '__main__':
    pytest.main()
