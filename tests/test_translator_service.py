import pytest
from utils.TranslatorText import TranslatorText

def test_invalid_language():
    translator = TranslatorText()
    text_input = 'Hola mundo'
    src_lang_input = 'es'
    tgt_lang_input = 'xx'

    result = translator.main(text_input, src_lang_input, tgt_lang_input)

    assert result == "Translation not found" or "An unexpected error was found" in result


def test_valid_translation():
    translator = TranslatorText()
    text_input = 'Hola mundo'
    src_lang_input = 'es'
    tgt_lang_input = 'en'

    result = translator.main(text_input, src_lang_input, tgt_lang_input)

    assert result == 'Hello World'
