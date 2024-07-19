import pytest
from translator import TranslatorText, TranslatorService


def mock_get_user_input(prompt):
    responses = {
        'Ingresa un texto: ': 'hola',
        'Tu lenguaje: ': 'es',
        'Lenguaje deseado: ': 'en'
    }
    return responses[prompt]


def test_translation(monkeypatch, capsys):
    # Usar monkeypatch para reemplazar get_user_input con nuestra función simulada.
    monkeypatch.setattr('translator.get_user_input', mock_get_user_input)

    # Crear una instancia de TranslatorText y ejecutar el método main.
    translator = TranslatorText()
    translator.main()

    # Capturar la salida estándar.
    captured = capsys.readouterr()

    # Verificar que la salida es la esperada.
    assert captured.out.strip() == 'hello'


def test_translation_language_error(monkeypatch, capsys):
    # Usar monkeypatch para reemplazar get_user_input con nuestra función simulada.
    # Esta vez simula un error en el idioma de origen.
    responses = {
        'Ingresa un texto: ': 'hola',
        'Tu lenguaje: ': 'xx',  # Idioma inexistente o incorrecto.
        'Lenguaje deseado: ': 'en'
    }
    monkeypatch.setattr('translator.get_user_input', lambda prompt: responses[prompt])

    # Crear una instancia de TranslatorText y ejecutar el método main.
    translator = TranslatorText()
    translator.main()

    # Capturar la salida estándar.
    captured = capsys.readouterr()

    # Verificar que la salida es la esperada para un error de idioma.
    assert captured.out.strip() == 'Translation not found'
