from aiogram.filters import Filter
from token_1 import kanal_id
from aiogram import Bot
from aiogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup

class ChecsUpChannel(Filter):
    async def __call__(self,message:Message,bot:Bot):
      for kanal in kanal_id:
        user_status=await bot.get_chat_member(kanal,message.from_user.id) 
        if user_status.status in ['creator','administrator','member']:
            return False
        
        menyu1=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Obuna bo'lish ✅",url="https://t.me/lollifamily/175")],
                [InlineKeyboardButton(text="Obuna bo'lish ✅",url="https://t.me/acodesa")],
            ]
        )

        return True
