from .base_validator import ValidatorBase

from config import MAX_LENGTH_VOCAB_NOTE, MIN_LENGTH_VOCAB_NOTE


class VocabNoteValidator(ValidatorBase):
    def __init__(self,
                 note: str,
                 vocab_name: str) -> None:
        super().__init__()  # Виклик конструктора базового класу
        self.note: str = note  # Примітка до словника
        self.vocab_name: str = vocab_name  # Назва словника

    def check_valid_length(self) -> bool:
        """Перевіряє, що коректна довжини"""
        length_note: int = len(self.note)
        if not MIN_LENGTH_VOCAB_NOTE <= length_note <= MAX_LENGTH_VOCAB_NOTE:
            error_text: str = 'Назва словника має містити від {min_length} до {max_length} символів.'.format(
                min_length=MIN_LENGTH_VOCAB_NOTE,
                max_length=MAX_LENGTH_VOCAB_NOTE)
            log_text: str = 'Назва до словника "{vocab_name}" не відповідає вимогам по довжині: довжина {current_length} символів. Допустима довжина: від {min_length} до {max_length}'.format(
                vocab_name=self.name,
                current_length=length_note,
                min_length=MIN_LENGTH_VOCAB_NOTE,
                max_length=MAX_LENGTH_VOCAB_NOTE)
            self.add_error_with_log(error_text, log_text)
            return False
        return True

    def is_valid(self) -> bool:
        """Запускає всі перевірки і повертає True, якщо всі вони пройдені"""
        checks: list[bool] = [self.check_valid_length()]
        return all(checks)
