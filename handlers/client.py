from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import random
from database.db import sql_command_random


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Начинаю работать")


async def meme(message: types.Message):
    # photo = [
    #     "photo\img1.png",
    #     "photo\img2.jpg",
    #     "photo\img3.jpg",
    # ]
    # img = open(random.choice(photo), "rb")
    img = open('photo\img1.png', 'rb')
    await bot.send_photo(message.from_user.id, photo=img)



async def victorina(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "почему ты изучаешь python?"
    answers = [
        "чтобы быть умнее",
        "для себя",
        "интересно",
        "чтобы зарабатывать",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        reply_markup=markup,
    )


async def victorina(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Next", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "почему ты изучаешь python?"
    answers = [
        "чтобы быть умнее",
        "для себя",
        "интересно",
        "чтобы зарабатывать",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        reply_markup=markup,
    )


# async def show_random_dish(message: types.Message):
#     await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(meme, commands=['meme'])
    dp.register_message_handler(victorina, commands=['victorina'])
    dp.register_message_handler(show_random_dish, commands=['get'])
