from src.TranslatorService import TranslatorService
from utils.input_handler import get_user_input

class TranslatorText:
    def main(self):
        text_input = get_user_input('Ingresa un texto: ')
        src_lang_input = get_user_input('Tu lenguaje: ')
        tgt_lang_input = get_user_input('Lenguaje deseado: ')
        translation = TranslatorService.translate_text(text_input, src_lang_input, tgt_lang_input)
        print(translation)

def get_user_input(prompt):
    return input(prompt)

class TranslatorService:
    @staticmethod
    def translate_text(text, src_lang, tgt_lang):
        # Este es un ejemplo de implementación ficticia.
        translations = {
            ('hola', 'es', 'en'): 'hello',
            ('hello', 'en', 'es'): 'hola',
        }
        return translations.get((text, src_lang, tgt_lang), 'Translation not found')
