from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

Token = config("TOKEN")
bot =Bot(Token)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN = [1121073609]



# async def load_name(message: types.Message, state: FSMContext):
#      async with state.proxy() as data:
#          data['name'] = message.text
#          # await bot.send_message(message.from_user.id, data['photo'])
#          # await bot.send_message(message.from_user.id,
#          #                        f"Name: {data['name']}\n"
#          #                        f"Description: {data['description']}\n"
#          #                        f"Price: {data['price']}"
#      await state.finish()
#      await message.answer("Описание блюда")
