import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

CHANNELS = [{"name": "mychannelmy123", "channel_id": "-1002181478617"}]

ADMIN = os.getenv('ADMIN')
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher(bot, storage=storage)
