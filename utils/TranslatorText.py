from src.TranslatorService import TranslatorService
from utils.input_handler import get_user_input


class TranslatorText:
    def main(self, text_input, src_lang_input, tgt_lang_input):

        translation = TranslatorService.translate_text(text_input, src_lang_input, tgt_lang_input)
        return translation


