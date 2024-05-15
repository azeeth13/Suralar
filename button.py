from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import requests

url = requests.get("https://api.alquran.cloud/v1/quran/en.asad").json()
s=[] 
for i in url['data']["surahs"]:
    s.append(i['englishName'])

for i in url['data']["surahs"][0]['ayahs']:
    ab= i['text']    
        
print(ab)   
       


suralar = InlineKeyboardBuilder()
for i in s:
    suralar.add(InlineKeyboardButton(text=i,callback_data=i))
suralar.adjust(3)
    

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Qur'on Suralari 📚 ", callback_data="suralar"),
        InlineKeyboardButton(text="Admin bilan bog'lanish 👨🏼‍💻", url="https://t.me/XAVIERXCK")],
        [InlineKeyboardButton(text="Qur'on sayti 🕌 ",web_app=WebAppInfo(url="https://mp3quran.net/eng"))],
        [InlineKeyboardButton(text="Namoz vaqtlari 🧎🏼",callback_data="namoz")]
        ]
)


book=InlineKeyboardMarkup(
    inline_keyboard=[
[InlineKeyboardButton(text="Islomiy kitoblar",callback_data="kitoblar")]
    ]
)
# sura=InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Suralar",callback_data=s)]
#     ]
# )



        
        