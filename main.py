from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import bot, dp
import logging

import random


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Начинаю работать")


@dp.message_handler(commands=['meme'])
async def meme(message: types.Message):
    photo = [
        "photo\img1.png",
        "photo\img2.jpg",
        "photo\img3.jpg",
    ]
    img = open(random.choice(photo), "rb")
    await bot.send_photo(message.from_user.id, photo=img)




@dp.message_handler(commands=['victorina'])
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


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def victorina_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Next", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Какой лучше напиток?"
    answers = [
        "Кола",
        "Султан чай",
        "Дюшес",
        "Фанта",
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        reply_markup=markup,
    )



@dp.message_handler()
async def echo(message: types.Message):

    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text)*int(message.text))
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)