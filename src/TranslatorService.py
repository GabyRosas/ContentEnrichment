from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound
from utils.input_handler import get_user_input
class TranslatorService:

    def __init__(self):
        pass

    @staticmethod
    def translate_text(text, src_lang, tgt_lang):
        try:
            translated_text = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
            return translated_text
        except TranslationNotFound:
            return "Translation not found"
        except Exception as e:
            return f"An unexpected error was found: {e}"




