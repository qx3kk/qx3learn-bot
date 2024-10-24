from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from src.keyboards.help_kb import get_inline_kb_help
from text_data import MSG_HELP

router = Router()


@router.callback_query(F.data == 'help')
async def process_btn_help(callback: CallbackQuery) -> None:
    """Відстежує натискання на кнопку допомоги".
    Відправляє користувачу повідомлення з допомогою.
    """
    title_help: str = MSG_HELP
    kb: InlineKeyboardMarkup = get_inline_kb_help()

    await callback.message.edit_text(text=title_help,
                                     reply_markup=kb)
