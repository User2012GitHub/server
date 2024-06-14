from aiogram.dispatcher.filters.state import StatesGroup, State

class MyStates(StatesGroup):
    courses = State()
    fio = State()
    phone = State()

class MyAdminStates(StatesGroup):
    request_message = State()
