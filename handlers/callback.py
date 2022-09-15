from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp


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

async def victorina_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Next", callback_data="button_call_2")
    markup.add(button_call_3)

    question = "Какой лучший фастфуд?"
    answers = [
        "Шаурма",
        "Бургер",
        "Сэндвич",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        reply_markup=markup,
    )


# a
async def victorina_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Next", callback_data="button_call_3")
    markup.add(button_call_3)

    question = "Какой лучший фастфуд?"
    answers = [
        "Шаурма"
        "Бургер"
        "Сэндвич"
    ]
    await bot.send_poll(
        question=question,
        chat_id=call.message.chat.id,
        options=answers,
        is_anonymous=False,

    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(victorina_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(victorina_3, lambda call: call.data == "button_call_2")
