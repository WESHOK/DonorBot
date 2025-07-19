from aiogram.types import ContentType
from aiogram import F
from aiogram_dialog import Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.kbd import Row
from aiogram_dialog.widgets.kbd import SwitchTo
from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const

from src.constants import ROOT_DIR
from src.bot.states import MainMenu
from src.bot.states import Reg
from .getters import *


def welcome_window():
    return Window(
        StaticMedia(
            path=ROOT_DIR + '/images/menu.jpg',
            type=ContentType.PHOTO
        ),
        Const(
            '🌟 Добро пожаловать\\! 🌟\n\n' +
            '🩸 День донора МИФИ 🩸\n' +
            '_Ваш персональный помощник в донорстве_\n\n' +
            '📌*Возможности бота*:\n' +
            '   • 📅 Запись на донацию крови\n' + 
            '   • 💉 Запись в регистр костного мозга\n' +
            '   • 📊 История ваших донаций\n' +
            '   • ℹ️ Полезная информация\n\n' +
            '🔐 Для начала работы требуется *авторизация*'
        ),
        Row(
            Start(
                Const('Регистрация'),
                id='reg',
                state=Reg.confirm,
                when=~F['is_db_user'],
            ),
            SwitchTo(
                Const('Помощь'),
                id='help',
                state=MainMenu.ask,
                when=F['is_db_user'],
            ),
        ),
        getter=check_user_getter,
        state=MainMenu.welcome,
    )

def help_window():
    return Window(
        Const('Пока ничего тут нету\\. Но скоро появится'),
        SwitchTo(
            Const('НАЗАД'),
            id='back',
            state=MainMenu.welcome,
        ),
        state=MainMenu.ask,
    )