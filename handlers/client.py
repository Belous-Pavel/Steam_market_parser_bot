from aiogram import types, Dispatcher
from create_bot import bot
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import State, StatesGroup
# import pytesseract
# from PIL import Image
# from keyboards import kb_client
# from keyboards import kb_profile
# from keyboards import kb_faq
# from keyboards import kb_game
# from keyboards import kb_marketplace
# from aiogram.dispatcher.filters import Text
# from aiogram.types import InputFile
# import os


# @dp.message_handler(commands=['start', 'help'])
async def welcome_start(message: types.Message):
    try:
        mess = f'Welcome, <b>{message.from_user.first_name}</b>.\n' \
               f'This bot will help you trade your skins, and find all the info about skins you need\n' \
               f'Enter /menu to view bot commands'
        await bot.send_message(message.chat.id, mess, parse_mode='html')
        await message.delete()
    except:
        await message.reply('Start the conversation entering /start')


# if bot didn't get the command write the message
async def echo_all(message: types.Message):
    await message.reply('Unknown command')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome_start, commands=['start', 'help'])
    dp.register_message_handler(echo_all, state="*", commands=['*'])
