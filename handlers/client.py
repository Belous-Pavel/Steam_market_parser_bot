from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import menu_client


# @dp.message_handler(commands=['start', 'help'])
async def welcome_start(message: types.Message):
    try:
        mess = f'Welcome, <b>{message.from_user.first_name}</b>.\n' \
               f'This bot will help you trade your skins, and find all the info about skins you need\n' \
               f'Enter /menu to view bot commands'
        await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=menu_client)
        await message.delete()
    except:
        await message.reply('Start the conversation entering /start')


async def help_func(message: types.Message):
    mess = f'smth'
    await bot.send_message(message.chat.id, mess, parse_mode='html')


async def menu(message: types.Message):
    pass


# if bot didn't get the command write the message
async def echo_all(message: types.Message):
    await message.reply('Unknown command')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome_start, commands=['start'])
    dp.register_message_handler(echo_all, state="*", commands=['*'])
    dp.register_message_handler(help_func, commands=['help'])
