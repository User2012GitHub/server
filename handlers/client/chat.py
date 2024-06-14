import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from keyboards.inline import get_voice
from keyboards.default import get_start
from states.main import MyStates
from utils.database import users
from loader import bot, dp, ADMIN
from filters import isStr
like, dislike = 0, 0
@dp.callback_query_handler()
async def callback_query(call: types.CallbackQuery):
    global like, dislike
    data = call.data
    if data == "like":
        like += 1
        await call.answer(f"like {like}")
    elif data == "dislike":
        dislike += 1
        await call.answer(f"dislike {dislike}")


async def get_start_admin():
    pass


@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    if message.from_user.id == int(ADMIN):

        await message.answer("Assalomu aleykum ADMIN!", reply_markup=await get_start_admin())
    else:
        fio = f"{message.from_user.first_name} {message.from_user.last_name}"
        users.create_user(fio, message.from_user.id, message.from_user.username)
        await message.answer("Assalomu aleykum, mening botimga xush kelibsiz", reply_markup=await get_start())
        await message.answer("F.I.O kiriting: ")
        await MyStates.fio.set()

@dp.message_handler(state=MyStates.fio)
async def about(message: types.Message, state: FSMContext):
    print("fio - ", message.text)
    await message.answer("Qaysi kursda o'qimoqdasiz?", reply_markup=ReplyKeyboardRemove())
    await MyStates.phone.set()

# @dp.message_handler(state=MyStates.courses)
# async def about(message: types.Message, state: FSMContext):
#     print("about - ", message.text)
#     await message.answer("Rahmat")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer("Tanlang: /photo yoki /sticker ?", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(commands=["sticker"])
async def send_sticker(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEMIwZmR3eP4npgcmZapbWosbfcfPpHogACKAADWbv8JfgsEeujOU5LNQQ")

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact(message: types.Message):
    print(message)
    await message.answer("Qabul qilindi!")

@dp.message_handler(commands=["photo"])
async def send_sticker(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://st3.depositphotos.com/8950810/17657/v/450/depositphotos_176577870-stock-illustration-cute-smiling-funny-robot-chat.jpg", caption = "sizga yoqdimi?", reply_markup=await get_voice())



@dp.message_handler(commands=["about_me"])
async def about(message: types.Message):
    global text
    if message.from_user.id == message.chat.id:
        info = users.about_me(message.from_user.id)
        for item in info:
            text = (f"<i>FIO</i> - <b>{item[1]}</b>\n"
                    f"<i>USERNAME</i> - <b>{item[2]}</b>\n"
                    f"<i>CHAT ID</i> - <b>{item[3]}</b>\n"
                    f"<i>PHONE NUMBER</i> - <b>{item[1]}</b>\n")
    await message.answer(text=text, parse_mode="HTML")

@dp.message_handler(commands=["wheather"])
async def wheather(message: types.Message):
    res = requests.get("https://api.weatherapi.com/v1/current.json?key=637a0367057542d9936143247240705&q=Tashkent")
    if res.status_code==200:
        response = res.json()
        name = response["location"]["name"]
        country = response["location"]["country"]
        tz = response["location"]["tz_id"]
        temp_c = response["current"]["temp_c"]

        text = (f"<em>Shahar</em> - <b>{name}</b>\n"
                f"<em>Davlat</em> - <b>{country}</b>\n"
                f"<em>Vaqt mintaqasi</em> - <b>{tz}</b>\n"
                f"<em>Harorat</em> - <b>{temp_c}°C</b>\n")
        await message.answer(text, parse_mode="HTML")

@dp.message_handler(commands=['currrency'])
async def currency(message: types.Message):
    res = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    if res.status_code==200:
        response = res.json()
        for item in response:
            ccy = item["Cyy"]
            name = item["CcyNm_UZ"]
            rate = item["Rate"]
            if ccy == 'USD' or ccy == 'EUR' or ccy == 'RUB':
                text = (f"<b>{ccy}</b>\n"
                       f"1 {name} - {rate} sum")
                await message.answer(text, parse_mode="HTML")

@dp.message_handler(commands=['books'])
async def books(message: types.Message):
    global item
    res = requests.get("https://www.googleapis.com/books/v1/volumes/F3d8EAAAQBAJ")
    if res.status_code==200:
        response = res.json()
        for item in response:

            name = item["Backend Developer in 30 Days"]
            photo = item["https://bpbonline.com/cdn/shop/products/595_Front_600x.jpg?v=1658303837"]
            author = item["Pedro Marquez-Soto"]

            text = (f"<em>Kitob nomi</em> - <b>{name}</b>\n"
                    f"<em>Rasmi</em> - <b>{photo}</b>\n"
                    f"<em>Yozuvchi</em> - <b>{author}</b>\n")
            await message.answer(text, parse_mode="HTML")

@dp.message_handler(isStr())
async def echo(message: types.Message):
    await message.answer(message.text)

