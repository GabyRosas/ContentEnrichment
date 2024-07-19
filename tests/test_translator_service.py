import pytest
from src.TranslatorService import TranslatorText

def test_invalid_language():
    translator = TranslatorText()
    text_input = 'Hola mundo'
    src_lang_input = 'es'
    tgt_lang_input = 'xx'  # Lenguaje incorrecto

    result = translator.main(text_input, src_lang_input, tgt_lang_input)

    assert result == "Translation not found" or "An unexpected error was found" in result


def test_valid_translation():
    translator = TranslatorText()
    text_input = 'Hola mundo'
    src_lang_input = 'es'
    tgt_lang_input = 'en'  # Lenguaje correcto

    result = translator.main(text_input, src_lang_input, tgt_lang_input)

    # Verificar que la traducción sea la esperada
    assert result == 'Hello World'