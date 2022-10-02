# import sqlite3
# from config import bot
# import random
#
#
# def sql_create():
#     global db, cursor
#     db = sqlite3.connect("bot.sqlite3")
#     cursor = db.cursor()
#
#     if db:
#         print("База данных подключена")
#
#     db.execute("CREATE TABLE IF NOT EXISTS menu "
#                "(photo TEXT, "
#                "name TEXT PRIMARY KEY, "
#                "description TEXT, "
#                "price INTEGER )")
#     db.commit()
#
#
# async def sql_command_insert(state):
#     async with state.proxy() as data:
#         cursor.execute("INSERT INTO menu VALUES"
#                        "(?,?,?,?)",
#                        tuple(data.values()))
#
#     db.commit()
#
#
# async def sql_command_random(message):
#     result = cursor.execute("SELECT * FROM menu").fetchall()
#     random_dish = random.choice(result)
#     await bot.send_photo(message.from_user.id, random_dish[2],
#                          f"Name: {random_dish[3]}\n"
#                          f"Description: {random_dish[4]}\n"
#                          f"Price: {random_dish[5]}")
#
#
# async def sql_command_all():
#     user_list = cursor.execute("SELECT * FROM menu").fetchall()
#     return user_list
#
#
# async def sql_command_delete(name):
#     cursor.execute("DELETE FROM menu WHERE name == ?", (name,))
#     db.commit()
