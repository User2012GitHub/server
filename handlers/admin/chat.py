from aiogram import types

from loader import ADMIN, bot, dp
from utils.database import users
from filters import IsAdmin
from states.main import MyAdminStates



@dp.message_handler(IsAdmin(), commands=["post"])
async def send_post(message: types.Message):
    if message.from_user.id == int(ADMIN):
        await message.answer("Xabarni kiriting:")
        await MyAdminStates.request_message.set()

@dp.message_handler(state=MyAdminStates.request_message)
async def send_message(message: types.Message):
    if message.from_user.id == int(ADMIN):
        user = users.get_users_all()
        if len(user) > 0:
            for item in user:
                print(item)
                await bot.send_message(item[2], message.text)