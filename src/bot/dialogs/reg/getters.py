from aiogram_dialog import DialogManager
from src.db.database import Database
from aiogram.types import User

async def check_window_getter(
        dialog_manager: DialogManager,
        **kwargs,
):
    return dialog_manager.dialog_data['input']

async def check_user_getter(
        dialog_manager: DialogManager,
        **kwargs,
):
    db: Database = dialog_manager.middleware_data['db']
    user: User = dialog_manager.middleware_data['event_from_user']

    if await db.quiz_user.get(user.id) == None:
        return {
        'is_db_user': False
        }
    
    return {
        'is_db_user': True
    }