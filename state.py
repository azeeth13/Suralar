from aiogram.fsm.state import State,StatesGroup

class Ayat(StatesGroup):
    number = State()
    text = State()