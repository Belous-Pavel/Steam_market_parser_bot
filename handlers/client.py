from aiogram import types, Dispatcher
from create_bot import bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import pytesseract
from PIL import Image
from keyboards import kb_client
from keyboards import kb_profile
from keyboards import kb_faq
from keyboards import kb_game
from keyboards import kb_marketplace
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile
import os


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

# @dp.message_handler(state="*", commands=['*']


async def echo_all(message: types.Message):
    await message.reply('Unknown command')


# @dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    try:
        mess = f'What u wanna do?\n' \
               f'<i>Note: Press Profile to view ur account data\n' \
               f'Press Price comparison to use the nain features of our parser\n' \
               f'Press FAQ to learn how does this bot works</i>'
        await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Start the conversation entering /start')


class FSMPatient(StatesGroup):
    steam_url = State()


async def profile_settings(message: types.Message):
    mess = f'What u wanna do?\n' \
               f'<i>Note: Press View Profile to view ur account data\n' \
               f'Press Buy Subscription to buy high-level tool</i>'
    await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=kb_profile)

# Начало диалога для загрузки информации о пользователе
# @dp.message_handler(commands='Profile', state=None)


async def info_collecting(message: types.Message):
    await FSMPatient.steam_url.set()
    mess = f'Enter your Steam URL\n' \
           f'<i>Note: You can enter /cancel to cancel the process</i>'
    await bot.send_message(message.chat.id, mess, parse_mode='html')


# Exit State

async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')


# @dp.message_handler(state=FSMAdmin.first_name)
async def load_steam_url(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['steam_url'] = message.text


# Забираем Имя
# @dp.message_handler(state=FSMAdmin.last_name)

    # async with state.proxy() as data:
    await bot.send_message(message.chat.id, 'Data uploaded')

    directory = 'C:/Users/Pasha/PycharmProjects/pythonProject5/user_steam_url/'
    count = len(os.listdir(directory))
    count = str(count)
    src = 'C:/Users/Pasha/PycharmProjects/pythonProject5/user_steam_url/' + 'user_' + count + '_steam_url.txt'

    with open(src, 'a') as review:
        review.write(f"steam_url: {data['steam_url']}\n")

    review.close()

    await state.finish()


async def send_faq_info(message: types.Message):

    mess = 'Here is the main information that can help you to use our bot\n' \
           '<i>Note: You can enter /cancel to cancel the process</i>'
    await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=kb_faq)


async def about_us(message: types.Message):
    await bot.send_message(message.chat.id, "Steam parser was develeped by ostis fans\n Team Lead: Pavel Belous\n Core developer: Ilya Gnuda \n SubCore developer: Andrei Shevchuk\n Dev Ops: Vyacheslav Gordienko\n Test: Konstantin Zavatskiy\n If you got some issues mail us steam.parser_support@gmail.com", parse_mode='html')


class FSMPriceComparison(StatesGroup):
    game = State()
    market_place_1 = State()
    market_place_2 = State()
    item_name = State()


async def price_info_collecting(message: types.Message):
    await FSMPriceComparison.game.set()
    mess = f'Enter the Game name\n' \
           f'<i>Note: You can enter /cancel to cancel the process</i>'
    await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=kb_game)


async def load_game_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['game_name'] = message.text
    await FSMPriceComparison.next()
    mess = f'Enter the first marketplace name\n' \
           f'<i>Note: You can enter /cancel to cancel the process</i>'
    await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=kb_marketplace)


async def load_first_marketplace_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_marketplace_name'] = message.text
    await FSMPriceComparison.next()
    mess = f'Enter the second marketplace name\n' \
           f'<i>Note: You can enter /cancel to cancel the process</i>'
    await bot.send_message(message.chat.id, mess, parse_mode='html',reply_markup= kb_marketplace)


async def load_second_marketplace_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['second_marketplace_name'] = message.text
    await FSMPriceComparison.next()
    mess = f'Enter the item name\n' \
           f'<i>Note: You can enter /cancel to cancel the process</i>'
    await bot.send_message(message.chat.id, mess, parse_mode='html')


async def load_item_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['item_name'] = message.text
    await bot.send_message(message.chat.id, 'Data uploaded')

    directory = 'C:/Users/Pasha/PycharmProjects/pythonProject5/price_info_parser/'
    count = len(os.listdir(directory))
    count = str(count)
    src = 'C:/Users/Pasha/PycharmProjects/pythonProject5/price_info_parser/' + 'user_' + count + 'parse.txt'

    with open(src, 'a') as review:
        review.write(f"Game name: {data['game_name']}\n"
                     f"First marketplace name: {data['first_marketplace_name']}\n"
                     f"Second marketplace name: {data['second_marketplace_name']}\n"
                     f"Item name: {data['item_name']}\n")

    review.close()

    await state.finish()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome_start, commands=['start', 'help'])
    dp.register_message_handler(echo_all, state="*", commands=['*'])
    dp.register_message_handler(menu, commands=['menu'])
    dp.register_message_handler(profile_settings, Text(equals='Profile', ignore_case=True), state=None)
    dp.register_message_handler(info_collecting, Text(equals='View Profile', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler, Text(equals='Cancel', ignore_case=True), state="*")
    dp.register_message_handler(cancel_handler, state="*", commands=['cancel'])
    dp.register_message_handler(load_steam_url, state=FSMPatient.steam_url)
    dp.register_message_handler(price_info_collecting, Text(equals='Price comparison', ignore_case=True), state=None)
    dp.register_message_handler(load_game_name, state=FSMPriceComparison.game)
    dp.register_message_handler(load_first_marketplace_name, state=FSMPriceComparison.market_place_1)
    dp.register_message_handler(load_second_marketplace_name, state=FSMPriceComparison.market_place_2)
    dp.register_message_handler(load_item_name, state=FSMPriceComparison.item_name)
    dp.register_message_handler(send_faq_info, Text(equals='FAQ', ignore_case=True), state=None)
    dp.register_message_handler(about_us, Text(equals='About us', ignore_case=True), state=None)


# @dp.message_handler(commands=['Ввести данные вручную2'])
# def insert_data(message: types.Message):
#        mess = bot.send_message(message.chat.id, "Пришлите фото отчета", parse_mode='html')
#        bot.register_next_step_handler(mess, get_user_photo)
#        return


# @dp.message_handler(content_types=['text'])
# def get_user_text(message):
#    bot.send_message(message.chat.id, "Ваше Имя")
#    if message.text == "Hello":
#        bot.send_message(message.chat.id, "Здарова", parse_mode='html')
#    elif message.text == "id":
#        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
#    elif message.text == "photo":
#        photo = open('75HVDcdg_no.png', 'rb')
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')

# @dp.message_handler(content_types=['photo'])
# def get_user_photo(message):

#    try:

#        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
#        downloaded_file = bot.download_file(file_info.file_path)

#        src = 'C:/Users/Pasha/PycharmProjects/pythonProject4/received/' + file_info.file_path

#        with open(src, 'wb') as new_file:
#            new_file.write(downloaded_file)
#        bot.reply_to(message, "Фото добавлено")
#        img = Image.open(src)
#        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#        text = pytesseract.image_to_string(img)
#        bot.send_message(message.chat.id, text, parse_mode='html')

#    except Exception as e:
#        bot.reply_to(message, e)


# @dp.message_handler(content_types=['document'])
# def handle_docs_photo(message):

#    try:

#        file_info = bot.get_file(message.document.file_id)
#        downloaded_file = bot.download_file(file_info.file_path)

#        src = 'C:/Users/Pasha/PycharmProjects/pythonProject4/received/docs/' + message.document.file_name

#        with open(src, 'wb') as new_file:
#            new_file.write(downloaded_file)
#        bot.reply_to(message, "Файл добавлен")
#        doc = new_file(message.text)
#        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#        text = pytesseract.image_to_string(img)
#        bot.send_message(message.chat.id, doc)

#    except Exception as e:
#        bot.reply_to(message, e)


# @bot.message_handler(content_types=['photo'])
# def handle_docs_photo(message):

#    file_info = bot.get_file(message.photo)
#    downloaded_file = bot.download_file(file_info.file_path)

#   src = 'C:/Users/Pasha/PycharmProjects/pythonProject4/received/' + message.document.file_name
#    with open(src, 'wb') as new_file:
#        new_file.write(downloaded_file)
#    img = Image.open(src)
#    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#    text = pytesseract.image_to_string(img)
#    bot.send_message(message.chat.id, text, parse_mode='html')


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#    bot.send_message(message.chat.id, 'Лучше скинь сиськи!', parse_mode='html')


# @dp.message_handler(commands=['website'])
# def website(message):
#    markup = types.InlineKeyboardMarkup()
#    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://www.youtube.com"))
#    bot.send_message(message.chat.id, "Кликай", reply_markup=markup)


# @dp.message_handler(commands=['help'])
# def help_user(message):
#    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#    website_n = types.KeyboardButton('Website')
#    start = types.KeyboardButton('Start')
#    markup.add(website_n, start)
#    bot.send_message(message.chat.id, "Чем могу помочь?", reply_markup=markup)

# f"concept_first_name->{data['first_name']};;\n"
# f"concept_last_name->{data['last_name']};;\n")
