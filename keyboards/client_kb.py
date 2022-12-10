from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_but = KeyboardButton('/menu')
help_but = KeyboardButton('/help')
about_but = KeyboardButton('/about')

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

menu_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

menu_client.row(menu_but, help_but, about_but)
