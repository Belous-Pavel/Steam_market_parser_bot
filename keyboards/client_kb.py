from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

menu_but = KeyboardButton('/menu')
help_but = KeyboardButton('/help')
about_but = KeyboardButton('/about')

menu_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

menu_client.row(menu_but, help_but, about_but)
