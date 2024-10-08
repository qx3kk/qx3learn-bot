import logging
from typing import Any

import sqlalchemy
from sqlalchemy.orm.query import Query

from db.models import Vocabulary
# from tools.escape_markdown import escape_markdown
from tools.read_data import app_data


class WordPairValidator:
    def __init__(self,
                 wordpair: str,
                 user_id: int,
                 max_count_words: int,
                 max_count_translations: int,
                 max_length_word: int,
                 max_length_translation: int) -> None:
        self.wordpair: str = wordpair.strip()  # Словникова пара без зайвих пробілів
        self.user_id: int = user_id
        self.max_count_words: int = max_count_words  # Максимальна кількість слів у словниковій парі
        self.max_count_translation: int = max_count_translations  # Максимальна кількість перекладів у словниковій парі
        self.max_length_word: int = max_length_word  # Максимальна кількість символів слова
        self.max_length_translation: int = max_length_translation  # Максимальна кількість символів перекладу
        self.errors_lst: list = []  # Список помилок

    def _add_error(self, error_text: str) -> None:
        """Додає помилку до списку помилок"""
        self.errors_lst.append(error_text)

    def valid_format(self) -> bool:
        """Перевіряє, що словникова пара має правильну структуру (мінімум слово та переклад)"""
        parts_wordpair: list[str] = self.wordpair.split(':')  # Розділяємо на частини за двокрапкою
        if len(parts_wordpair) < 2:
            self._add_error('Помилка формату словникової пари! Словникова пара повинна містити щонайменше одне слово та один переклад, розділені символом ":".')
            logging.warning(f'Помилка! Словникова пара "{self.wordpair}" має неправильний формат.')
            return False
        if len(parts_wordpair) > 3:
            self._add_error('Помилка формату словникової пари! Максимальна кількість частин у словниковій парі - три (слова, переклади, анотація).')
            logging.warning(f'Помилка! Словникова пара "{self.wordpair}" містить більше трьох частин.')
            return False
        return True

    def valid_words(self) -> bool:
        """Перевіряє коректність слів у словниковій парі"""
        words_lst: list[str] = self.wordpair.split(':')[0].split(',')
        words_lst_cleared: list[str] = [word.strip() for word in words_lst]
        count_words: int = len(words_lst)

        if not (1 <= count_words <= self.max_count_words):
            self._add_error(f'Словникова пара повинна містити від 1 до {self.max_count_words} слів.')
            logging.warning(f'Помилка! Словникова пара "{self.wordpair}" містить некоректну кількість слів: {count_words}.')
            return False

        for word in words_lst_cleared:
            if not (1 <= len(word) <= self.max_length_word):
                self._add_error(f'Слово "{word}" повинно містити від 1 до {self.max_length_word} символів.')
                logging.warning(f'Помилка! Слово "{word}" містить некоректну кількість символів.')
                return False
            if not all(char.isalnum() or char in '-_ ' for char in word):

                self._add_error(f'Слово "{word}" має містити лише літери, цифри, пробіли, тире та підкреслення.')
                logging.warning(f'Помилка! Слово "{word}" містить некоректні символи.')
                return False
        return True

    def valid_translations(self) -> bool:
        """Перевіряє коректність перекладів у словниковій парі"""
        translations_lst: list[str] = self.wordpair.split(':')[1].split(',')
        translations_lst_cleared: list[str] = [translation.strip() for translation in translations_lst]
        count_translations: int = len(translations_lst)

        if not (1 <= count_translations <= self.max_count_translation):
            self._add_error(f'Словникова пара повинна містити від 1 до {self.max_count_translation} перекладів.')
            logging.warning(f'Помилка! Словникова пара "{self.wordpair}" містить некоректну кількість перекладів: {count_translations}.')
            return False

        for translation in translations_lst_cleared:
            if not (1 <= len(translation) <= self.max_length_translation):
                self._add_error(f'Переклад "{translation}" повинен містити від "1" до "{self.max_length_translation}" символів.')
                logging.warning(f'Помилка! Переклад "{translation}" містить некоректну кількість символів.')
                return False
            if not all(char.isalnum() or char in '-_ ' for char in translation):
                self._add_error(f'Переклад "{translation}" має містити лише літери, цифри, пробіли, тире та підкреслення.')
                logging.warning(f'Помилка! Переклад "{translation}" містить некоректні символи.')
                return False
        return True

    def extract_data(self) -> dict:
        """Повертає слова, переклади та анотацію з валідної пари"""
        parts_wordpair: list[str] = self.wordpair.split(':')  # Розбита словникова пара

        # Слова словникової пари
        words: list[str] = [word.strip() for word in parts_wordpair[0].split(',')]

        # Переклади словникової пари
        translations: list[str] = [translation.strip() for translation in parts_wordpair[1].split(',')]

        # Анотація словникової пари
        annotation: str | None = parts_wordpair[2].strip() if len(parts_wordpair) == 3 else None

        # Словник словникової пари
        wordpair_data: dict[str, Any] = {'words': words,
                                         'translations': translations,
                                         'annotation': annotation}
        return wordpair_data

    def is_valid(self) -> bool:
        """Перевіряє словникову пару на коректність"""
        self.errors_lst = []  # Очищення списку помилок
        if self.valid_format():
            checks: list[bool] = [self.valid_words(), self.valid_translations()]
            return all(checks)
        return False

    def format_errors(self) -> str:
        """Форматує список помилок у зручний для виведення формат"""
        formatted_errors_lst: list = [f'{num}. {error}' for num, error in enumerate(self.errors_lst, start=1)]
        logging.info(f'Всі помилки словникової пари "{self.wordpair}" відформатовані у рядок.')

        return '\n'.join(formatted_errors_lst)
