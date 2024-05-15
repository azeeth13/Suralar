import asyncio
import logging
import sys
import os
import aiohttp
import re
from aiogram.filters import CommandStart, and_f
from os import getenv
from aiogram import types
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery,InlineKeyboardMarkup
from button import *
from check import ChecsUpChannel
from check import *
from token_1 import TOKEN
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from state import Ayat
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))




dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
  await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=36aa19cd7a31038bb9792a1eef401d7bdbb94728-12475602-images-thumbs&n=13",caption=f"Assalomu aleykum {html.bold(message.from_user.full_name)}!\nQur'on Suralari botiga xush kelibsiz 📚\nBu bot orqali siz Qur'on suralari va oyatlarini bilib olishingiz mumkin 🕋",reply_markup=menu)

# @dp.message(ChecsUpChannel())
# async def echo_handler(message:types.Message):
    
#     await message.answer(f"Kanalga obuna bo'lmasangiz bot ishlamaydi",reply_markup=menyu1)




   

# @dp.message(F.text)
# async def command_begin(message: Message) -> None:
#    await message.answer_photo(,caption="Islomiy Ta'lim",reply_markup=menu)


@dp.callback_query(F.data == "suralar")
async def viloyat(callback: CallbackQuery,state:FSMContext):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Barcha Suralar 🕋 ",reply_markup=suralar.as_markup())
    await state.set_state(Ayat.number)





@dp.callback_query(Ayat.number)
async def get_oyat(callback:CallbackQuery,state:FSMContext):
    ayatlar2 = callback.data
    print(ayatlar2)
    await state.update_data(
        {"ayat":ayatlar2}
    )
    ayatlar1 = InlineKeyboardBuilder()
    ls = []        
    
    for i in url['data']["surahs"]:
        if i['englishName']==ayatlar2:
            for j in i['ayahs']:
                ab= j['text']
                ls.append(ab)        
                ayatlar1.add(InlineKeyboardButton(text=str(j["numberInSurah"]),callback_data=str(j['numberInSurah'])))
            
            
            # ['text']
            # ls.append(ab)
            # ayatlar1.add(InlineKeyboardButton(text=str(i['ayahs']["numberInSurah"]),callback_data=str(i['numberInSurah'])))    
    
    
    
    
    
    
    # for i in url['data']["surahs"][0]['ayahs']:
    #     ab= i['text']
    #     ls.append(ab)        
    #     ayatlar1.add(InlineKeyboardButton(text=str(i["numberInSurah"]),callback_data=str(i['numberInSurah'])))
    ayatlar1.adjust(1)
    await callback.message.answer("Oyatlar",reply_markup=ayatlar1.as_markup())     
    await state.set_state(Ayat.text)
    
@dp.callback_query(Ayat.text)
async def text1(call:CallbackQuery,state:FSMContext):
    text = call.data 
    print(text)
    r= await state.get_data()
    d = r.get("ayat")
    for i in url['data']["surahs"]:
        if i['englishName']==d:
            for j in i['ayahs']:
                if str(text)==str(j['numberInSurah']):
                    print(j["text"])
                    await call.message.answer(j["text"])    

    




@dp.callback_query(F.data == "namoz")
async def get_namaz(callback:CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=2a00000179e278ac5dd9801b780b81566628-4828420-images-thumbs&n=13",caption="Xorazm vaqti bo'yicha 5 vaqt namoz vaqti:\n🌄 Bomdod : 3:57 ✨\n☀️ Quyosh : 5:30 ✨\n☀️ Peshin namozi : 12:59 ✨\n⛅️ Asr namozi : 18:02 ✨\n🌙 Shom  namozi: 20:15 ✨\n🌙  Xufton namozi : 21:45 ✨")


@dp.callback_query(F.data == "kitoblar")
async def get_kitab(callback:CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=17aa7d7685aba30bac6690002c0cb6a0994342b8-5682239-images-thumbs&n=13",caption="Sahih al-Bukhari",reply_markup=book)
    await callback.message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=1c6e28c7aa7148e5c7e70c51595c7326d237abd1-10667780-images-thumbs&n=13",caption="Sahih Muslim",reply_markup=book)
    
    
    
@dp.message(F.chat.type=="supergroup",F.new_chat_members)
async def get_new_chat(message:Message):
    
    for new_chat in message.new_chat_members:
        await message.answer(f"Salom {new_chat.full_name} guruhga hush kelibsiz")
        
        await message.delete()

@dp.message(F.chat.type=="supergroup",F.left_chat_member)
async def get_new_chat(message:Message):
    await message.answer(f" {message.left_chat_member.full_name} Guruhni tark etdi.")



@dp.message(F.chat.type=="supergroup",and_f(F.text=="Yoza olmaysiz",F.reply_to_message))
async def get_banned_chat(message:Message):
    user_id=message.reply_to_message.from_user.id
    permission=types.ChatPermissions(can_send_messages=False)
    await message.chat.restrict(user_id,permission)
    await message.answer(f"Siz noto'g'ri so'zdan foydalandingiz❌\n{message.reply_to_message.from_user.full_name}")
   
@dp.message(F.chat.type=="supergroup",and_f(F.text=="Yoza olasiz",F.reply_to_message))
async def get_not_ban_chat(message:Message):
    user_id=message.reply_to_message.from_user.id
    permission=types.ChatPermissions(can_send_messages=True)
    await message.chat.restrict(user_id,permission)
    await message.answer(f"Endi yozishingiz mumkin\n✅{message.reply_to_message.from_user.full_name}")



 
@dp.message()
async def echo_handler(message: Message) -> None:
   await message.send_copy(chat_id=message.chat.id)

@dp.message(F.contact)
async def get_phone(message:Message):
    await message.answer_contact("asda")







async def main() -> None:
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    await dp.start_polling(bot)




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
