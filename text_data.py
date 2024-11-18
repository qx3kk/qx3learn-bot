# handlers/create_vocab.py
MSG_ENTER_VOCAB_NAME = 'Введіть назву словника.'
MSG_ENTER_NEW_VOCAB_NAME = 'Введіть, будь-ласка, нову назву словника або натисніть на кнопку "Залишити поточну назву".'

MSG_ENTER_VOCAB_DESCRIPTION = (
    'Введіть опис словника або натисніть на кнопку "Пропустити", якщо опис не потрібен.')

MSG_ENTER_WORDPAIRS = (
    'Введіть "словникові пари" у форматі:\n'
    'w1 | tr1 , w2 | tr2 : t1, t2 : a\n\n'
    '- w — слово\n'
    '- tr — транскрипція (опціонально).\n'
    '- t — переклад.\n'
    '- a — анотація (опціонально).\n\n'
    '*Слово, переклад, анотація розділяються символом ":"\n'
    '*Слово та транскрипція розділяються символом "|"\n'
    '*Можна додати декілька слів чи перекладів, розділяючи їх символом "," (опціонально)\n\n'
    '(В одному повідомленні можна ввести декілька словникових пар розділених, кожну у новому рядку)')

MSG_ENTER_WORDPAIRS_SMALL_INSTRUCTIONS = (
    'Введіть "словникові пари" у форматі:\n'
    'w1 | tr1 , w2 | tr2 : t1, t2 : a\n\n'
)

MSG_ERROR_VOCAB_NAME_DUPLICATE = (
    'Нова назва словника не може бути такою ж, як і поточна.\n\n'
    'Введіть, будь-ласка, нову назву словника або натисніть на кнопку "Залишити поточну назву".')
MSG_ERROR_VOCAB_NAME_INVALID = (
  'У назві словника "{vocab_name}" є помилки:\n'
  '{errors}')
MSG_ERROR_VOCAB_DESCRIPTION_INVALID = 'У примітці "{description}" до словника "{vocab_name}" є помилки:\n{errors}'

MSG_ERROR_WORDPAIRS_NO_VALID = '⚠️ Немає валідних словникових пар.'
MSG_ERROR_NO_VALID_WORDPAIRS_ADDED = 'Не було додано жодної валідної словникової пари.'

MSG_SUCCESS_VOCAB_SAVED_TO_DB = 'Словник "{vocab_name}" успішно збережено до бази словників!\n\n{instruction}'
MSG_SUCCESS_ALL_WORDPAIRS_VALID = '🎉 Немає помилок серед введених пар!'

MSG_INFO_ADDED_WORDPAIRS = '✅ Додані словникові пари:\n{wordpairs}'
MSG_INFO_NO_ADDED_WORDPAIRS = '❌ Не додані словникові пари:\n{wordpairs}'

MSG_CONFIRM_CANCEL_CREATE_VOCAB = 'Ви дійсно хочете скасувати створення словника?'


# handlers/menu.py
MSG_TITLE_MENU = 'Головне меню'
MSG_TITLE_MENU_FOR_NEW_USER = 'Привіт! 👋 Вітаємо у боті для вивчення слів!\n\nГоловне меню'


# handlers/vocab_base.py
MSG_CHOOSE_VOCAB = 'Оберіть словник із вашої бази або створіть новий.'

MSG_ERROR_VOCAB_BASE_EMPTY = 'У вашій базі поки що немає словників.\nСтворіть новий словник, щоб почати.'

TEMPLATE_WORDPAIR = ('{idx}. {words} ▪️ '
                     '{translations} ▪️ '
                     '{annotation}\n'
                     '🔺 Помилки: {number_errors}\n')

MSG_INFO_VOCAB = ('📚 Назва словника: {name}\n'
                  '📄 Опис: {description}\n'
                  '🔢 Кількість словникових пар: {wordpairs_count}\n'
                  '⚠️ Загальна кількість помилок: {number_errors}\n\n'
                  'Словникові пари:\n'
                  '{wordpairs}')


# handlers/vocab_trainer.py
MSG_ENTER_VOCAB_FOR_TRAIN = 'Оберіть словник із вашої бази для початку тренування.'


# handlers/help.py
MSG_TITLE_HELP = """
📚 Допомога: Як користуватися ботом для вивчення слів

1️⃣ Як додати новий словник

Кроки для створення словника:
1. Додати назву словника:
   Коли бот попросить ввести назву словника, введіть її в повідомленні. Назва має бути унікальною для вашого облікового запису.

2. Додати примітку до словника (опціонально):
   Якщо вам потрібна примітка (наприклад, тема словника або контекст його використання), ви можете додати її. Якщо примітка не потрібна, натисніть кнопку "Пропустити".

3. Додати словникові пари:
   Після створення словника вам потрібно додати слова та переклади. Словникові пари додаються у спеціальному форматі, який включає слова, транскрипції, переклади та анотації.

Формат словникових пар:
- Слово | транскрипція : переклад : анотація

Можна додавати декілька слів або перекладів через кому, але лише одну анотацію.

Приклади:
- слово | транскрипція : переклад (анотація необов'язкова)
  - cat | kæt : кіт
  - dog : пес

- слово | транскрипція : переклад, переклад2 : анотація
  - book | bʊk : книга, підручник : щось, що читають
  - sun : сонце : небесне тіло

Що означають поля:
- слово (обов’язкове): це слово, яке ви хочете додати до словника.
- транскрипція (опціонально): якщо ви хочете додати транскрипцію слова, вона пишеться після символу |.
- переклад (обов’язкове): переклад слова через двокрапку :.
- анотація (опціонально): додатковий опис або пояснення словникової пари, додається через двокрапку після перекладу.


2️⃣ Типи тренувань

Після того як ви створили словник та додали до нього слова, ви можете тренуватися. Існує два типи тренувань:

✅ Тренування на переклад:
Цей режим тренування допомагає вам вивчати переклади слів. Бот показує вам слово, і ваше завдання — ввести правильний переклад цього слова.

- Бот запитує слово з вашого словника, і ви маєте ввести відповідний переклад.
- Мета: перевірити, як добре ви пам’ятаєте переклад слів.

📝 Тренування на написання:
Цей режим допомагає вам практикуватися в написанні слів іноземною мовою. Бот показує переклад, а ви маєте правильно написати слово.

- Бот показує переклад, і вам потрібно ввести відповідне слово.
- Мета: перевірити, наскільки добре ви пам’ятаєте написання слів.


3️⃣ Додаткові можливості

- Перегляд бази словників: Ви можете переглядати всі свої словники та словникові пари через меню бази словників.
- Видалення або редагування: У разі помилок ви можете видаляти або редагувати словникові пари.

Цей бот допоможе вам ефективно вивчати нові слова, тренуватися на переклад або написання, а також підтримувати свої словники в порядку.
"""


# validators/vocab/vocab_name_validator.py
MSG_ERROR_VOCAB_NAME_UNIQUELY = 'У вашій базі словників вже є словник з назвою "{name}".'
MSG_ERROR_VOCAB_NAME_INVALID_LENGTH = 'Довжина назви словника має бути від {min_length} до {max_length} символів.'
MSG_ERROR_VOCAB_NAME_INVALID_CHARS = 'Назва словника може містити лише літери, цифри та символи: "{allowed_chars}".'


# validators/vocab/vocab_description_validator.py
MSG_ERROR_VOCAB_DESCRIPTION_INVALID_LENGTH = ('Довжина опису словника має бути від {min_length} до {max_length} '
                                              'символів.')


# validators/wordpair/wordpair_validator.py
MSG_ERROR_WORDPAIR_MIN_REQUIREMENT = ('Словникова пара повинна містити щонайменше одне слово та один переклад, '
                                      'розділені символом "{separator}".')
MSG_ERROR_WORDPAIR_MAX_REQUIREMENT = 'Словникова пара може містити максимум три частини: слово, переклад і анотацію.'
del_MSG_ERROR_WORDPAIR_WORD_IS_EMPTY = 'Слово словникової пари не може бути порожнім.'
del_MSG_ERROR_WORDPAIR_TRANSLATION_IS_EMPTY = 'Переклад словникової пари не може бути порожнім.'
del_MSG_ERROR_WORDPAIR_INVALID_WORDS_COUNT = 'Кількість слів до словникової пари має бути від {min_count} до {max_count}.'


# validators/wordpair/component_validator.py
MSG_ERROR_COMPONENT_INVALID_LENGTH = ('Довжина компонента "{component}" має бути від '
                                      '{min_length} до {max_length} символів.')
MSG_ERROR_COMPONENT_INVALID_CHARS = ('Компонент "{component}" може містити лише літери, цифри та символи: '
                                     '"{allowed_chars}".')


# custom exceptions
INVALID_VOCAB_INDEX_ERROR = 'Словника з ID "{id}" не було знайдено у БД'
USER_NOT_FOUND_ERROR = 'Користувача з ID "{id}" не було знайдено у БД'
