from aiogram import types, Dispatcher
from config import bot, dp
import random


async def echo(message: types.Message):
    emodji = [
        "⚽"
        "🎯"
        "🎳"
        "🎰"
        "🎲"
        "🏀"
    ]
    dice = open(random.choice(emodji), "rb")
    if message.text == "game":
        await bot.send_dice(message.chat.id)



def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
