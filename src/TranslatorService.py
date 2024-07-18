from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound
from utils.input_handler import get_user_input
class TranslatorService:

    def __init__(self):
        pass


    def translate_text(self, text, src_lang, tgt_lang):
        try:
            translated_text = GoogleTranslator(source=src_lang, targ=tgt_lang).translate(text)
            return translated_text
        except TranslationNotFound:
            return "Translation not found"
        except Exception as e:
            return f"An unexpected error was found: {e}"



translator_service = TranslatorService()

text_input = get_user_input('ingresa un texto: ')
src_lang_input = get_user_input('tu lenguaje: ')
tgt_lang_input = get_user_input('lenguaje deseado: ')

print(translator_service.translate_text(text_input, src_lang_input, tgt_lang_input))
