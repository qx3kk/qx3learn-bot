from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from db.database import Session
from db.models import User
from src.keyboards.menu_kb import get_inline_kb_menu
from tools.read_data import app_data

router = Router(name='menu')


@router.callback_query(F.data == 'neutral_call')
async def process_neutral_call(callback: CallbackQuery) -> None:
    """Заглушка для callback"""
    # Відповідаємо на callback-запит без відправлення повідомлення
    await callback.answer()


@router.message(Command(commands=['start', 'menu']))
async def cmd_menu(message: Message) -> None:
    """Відстежує введення команд "start, menu".
    Відправляє користувачу повідомлення головного меню.
    """
    kb: InlineKeyboardMarkup = get_inline_kb_menu()

    tg_user: User | None = message.from_user

    with Session() as db:
        # Чи є користувач у БД
        is_user_exists: bool = db.query(User).filter(User.user_id == tg_user.id).first() is not None

        if is_user_exists:
            title_menu: str = "app_data['menu']['title']"
        else:
            title_menu: str = "app_data['menu']['title_for_new_user']"
            # Додавання користувача до БД
            user = User(user_id=tg_user.id,
                        username=tg_user.username,
                        first_name=tg_user.first_name,
                        last_name=tg_user.last_name)
            db.add(user)
            db.commit()

    await message.answer(
        text=title_menu,
        reply_markup=kb)


@router.callback_query(F.data == 'menu')
async def process_btn_back_to_menu(callback: CallbackQuery) -> None:
    """Відстежує натискання на кнопку "меню".
    Відправляє користувачу повідомлення головного меню.
    """
    title_menu: str = "app_data['menu']['title']"
    kb: InlineKeyboardMarkup = get_inline_kb_menu()

    await callback.message.edit_text(
        text=title_menu,
        reply_markup=kb)
