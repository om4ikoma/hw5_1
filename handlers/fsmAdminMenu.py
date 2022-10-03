from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot, ADMIN


class FsmAdminMenu(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FsmAdminMenu.photo.set()
        await message.answer("Отправьте фото блюда")
    else:
        await message.answer("Напишите в личку")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as menu:
        menu['photo'] = message.photo[0].file_id
    await FsmAdminMenu.next()
    await message.answer("Название блюда?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as menu:
        menu['name'] = message.text
    await FsmAdminMenu.next()
    await message.answer("Описание")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as menu:
        menu['description'] = message.text
    await FsmAdminMenu.next()
    await message.answer("Цена")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as menu:
        menu['price'] = message.text
        await bot.send_photo(message.from_user.id, menu['photo'],
                             caption=f"Name: {menu['name']}\n"
                                     f"Description: {menu['description']}\n"
                                     f"Price: {menu['price']}")

    await state.finish()
    await message.answer("Блюдо добавлено")


def register_hanlers_fsmAdminMenu(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FsmAdminMenu.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FsmAdminMenu.name)
    dp.register_message_handler(load_description, state=FsmAdminMenu.description)
    dp.register_message_handler(load_price, state=FsmAdminMenu.price)
