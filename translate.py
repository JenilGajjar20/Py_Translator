import os
from tabulate import tabulate
# from googletrans import Translator
from deep_translator import GoogleTranslator


class Simple_Translator:
    def __init__(self, word, language):
        self.word = word
        self.language = language
        # self.translator = Translator()
        self.translator = GoogleTranslator(source='auto', target=self.language)

    def translation(self):
        translation = self.translator.translate(self.word)
        print("translation: ", translation)
        print("self.word: ", self.word)

        translated_text = translation if isinstance(
            translation, str) else translation['translatedText']

        print("translated_Text: ", translated_text)
        data = [["Original Word/Sentence:", "Translated Word/Sentence:"],
                [self.word, translated_text]]
        return tabulate(data, headers="firstrow", tablefmt="fancy_grid")

    def __str__(self):
        return self.translation()


if __name__ == "__main__":
    sentence = input("Enter the string to translate: ")
    os.system('cls' if os.name == 'nt' else 'clear')

    translator = Simple_Translator(sentence, "en")
    print(translator)
