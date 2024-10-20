# handlers/create_vocab.py
MSG_ENTER_VOCAB_NAME = 'Введіть назву словника.'
MSG_ERROR_VOCAB_SAME_NAME = (
    'Нова назва словника не може бути такою ж, як і поточна.\n\n'
    'Введіть, будь-ласка, нову назву словника або натисніть на кнопку "Залишити поточну назву".')
MSG_SUCCESS_VOCAB_NAME_CREATED = (
    'Назва словника успішно збережена!\n\n'
    'Введіть примітку до словника')
MSG_SUCCESS_VOCAB_NOTE_CREATED = 'Примітка до словника успішно збережена!'
MSG_VOCAB_NAME_ERRORS = (
    'У назві словника "{vocab_name}" є помилки:\n'
    '{errors}')
MSG_VOCAB_NOTE_ERRORS = ('У примітці "{vocab_note}" до словника "{vocab_name}" є помилки:\n{errors}')
MSG_VOCAB_WORDPAIRS_SAVED_INSTRUCTIONS = ('Введіть "словникові пари" у форматі:\n'
                                          'w1 | tr1 , w2 | tr2 : t1, t2 : a\n\n'
                                          '- w — слово\n'
                                          '- tr — транскрипція (опціонально).\n'
                                          '- t — переклад.\n'
                                          '- a — анотація (опціонально).\n\n'
                                          '*Слово, переклад, анотація розділяються символом ":"\n'
                                          '*Слово та транскрипція розділяються символом "|"\n'
                                          '*Можна додати декілька слів чи перекладів, розділяючи їх символом "," (опціонально)\n\n'
                                          '(В одному повідомленні можна ввести декілька словникових пар розділених, кожну у новому рядку)')
MSG_VOCAB_WORDPAIRS_SAVED_SMALL_INSTRUCTIONS = ('Введіть "словникові пари" у форматі:\n'
                                               'w1 | tr1 , w2 | tr2 : t1, t2 : a')
MSG_ENTER_NEW_VOCAB_NAME = 'Введіть, будь-ласка, нову назву словника або натисніть на кнопку "Залишити поточну назву".'
MSG_ENTER_NEW_VOCAB_NAME = 'Введіть, будь-ласка, нову назву словника або натисніть на кнопку "Залишити поточну назву".'
MSG_CONFIRM_CANCEL_CREATE_VOCAB = 'Ви дійсно хочете скасувати створення словника?'
MSG_ADDED_WORDPAIRS = '✅ Додані словникові пари:\n{wordpairs}'
MSG_NO_ADDED_WORDPAIRS = '❌ Не додані словникові пари:\n{wordpairs}'
MSG_NO_ERRORS_WORDPAIRS = '🎉 Немає помилок серед введених пар!'
MSG_ERROR_NO_VALID_WORDPAIRS = '⚠️ Немає валідних словникових пар.'
MSG_SUCCESS_VOCAB_SAVED_TO_DB: str = 'Словник "{vocab_name}" успішно збережено до бази словників!\n\n{MSG_MENU}'
MSG_ERROR_NO_ADD_WORDPAIRS = 'Немає доданих словникових пар.\n\n{MSG_VOCAB_WORDPAIRS_SAVED_SMALL_INSTRUCTIONS}'

# handlers/menu.py
MSG_MENU = 'Головне меню'
MSG_MENU_FOR_NEW_USER = 'Привіт! 👋 Вітаємо у боті для вивчення слів!\n\nГоловне меню'



# handlers/vocab_base.py
MSG_ERROR_VOCAB_BASE_EMPTY = 'У вашій базі поки що немає словників.\nСтворіть новий словник, щоб почати.'
MSG_ENTER_VOCAB = 'Оберіть словник із вашої бази або створіть новий.'
