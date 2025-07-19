from aiogram.filters.state import State
from aiogram.filters.state import StatesGroup

class MainMenu(StatesGroup):
    welcome = State()
    ask = State()

class Reg(StatesGroup):
    confirm = State()
    number = State()
    