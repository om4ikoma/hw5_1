from aiogram.utils import executor
from config import dp
import logging
from handlers import client, callback, extra, fsmAdminMenu, notification, inline
from database import db
# from database.db import sql_create
import asyncio


async def on_startup(_):
    asyncio.create_task(notification.schedule())
    # db.sql_create()


client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_hanlers_fsmAdminMenu(dp)
inline.register_handlers_inline(dp)
notification.register_handlers_notification(dp)

# extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
