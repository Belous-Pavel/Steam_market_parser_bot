from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import inline_kb1, menu_client


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
    mess = f"choose the following filters to see skins"
    await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=inline_kb1)


async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


# if bot didn't get the command write the message
async def echo_all(message: types.Message):
    await message.reply('Unknown command')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome_start, commands=['start'])
    dp.register_message_handler(echo_all, state="*", commands=['*'])
    dp.register_message_handler(help_func, commands=['help'])
    dp.register_message_handler(menu, commands=['menu'])
    dp.callback_query_handler(func=lambda c: c.data == 'button1')
