from aiogram import types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp,ADMIN
import logging
import random



async def echo(message: types.Message):
    if message.from_user.id == ADMIN:
        games = ['🎲', '🏏', '⚽']
        # value = random.choice(games)
        if message.text.startswith('game'):
            await bot.send_message(message.chat.id, random.choice(games))
        if message.text.startswith('pin'):
            await bot.pin_chat_message(message.chat.id, message.message_id)
        await bot.send_message(message.chat.id, message.text)
        a = int(message.text)
        if a:
            await bot.send_message(message.chat.id, a ** 2)



def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)