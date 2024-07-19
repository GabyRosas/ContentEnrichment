from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound

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

    @staticmethod
    def translate_paragraphs(paragraphs, src_lang, tgt_lang):
        translated_paragraphs = []
        for paragraph in paragraphs:
            try:
                translated_paragraph = TranslatorService.translate_text(paragraph, src_lang, tgt_lang)
                translated_paragraphs.append(translated_paragraph)
            except Exception as e:
                translated_paragraphs.append(f"Error translating: {str(e)}")
        return translated_paragraphs


class TranslatorText:
    def main(self, text_input, src_lang_input, tgt_lang_input):
        translation = TranslatorService.translate_text(text_input, src_lang_input, tgt_lang_input)
        return translation


