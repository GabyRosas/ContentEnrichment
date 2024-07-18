from src.TranslatorService import TranslatorService
from utils.input_handler import get_user_input


text_input = get_user_input('ingresa un texto: ')
src_lang_input = get_user_input('tu lenguaje: ')
tgt_lang_input = get_user_input('lenguaje deseado: ')

print(TranslatorService.translate_text(text_input, src_lang_input, tgt_lang_input))