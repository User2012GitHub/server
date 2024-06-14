from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def get_start():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.add(KeyboardButton("/start")).insert(KeyboardButton("/help"))
    btn.insert(KeyboardButton("/sticker")).insert(KeyboardButton("/photo"))
    return btn