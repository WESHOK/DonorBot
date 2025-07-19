from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from sulguk import AiogramSulgukMiddleware

from src.config import BotConfig


async def setup_bot(config: BotConfig) -> Bot:
    
    bot: Bot = Bot(
        token=config.token.get_secret_value(),
        default=DefaultBotProperties(
            parse_mode=ParseMode.MARKDOWN_V2,
        ),
    )

    # https://github.com/Tishka17/sulguk#example-for-aiogram-users
    bot.session.middleware(AiogramSulgukMiddleware())

    await bot.delete_my_commands()

    return bot


__all__ = ['setup_bot']