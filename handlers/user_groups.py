from aiogram import Router, types, F
from aiogram.filters import Command
from filters.chat_types import ChatTypeFilter
from string import punctuation

user_gr_rout = Router()
user_gr_rout.message.filter(ChatTypeFilter(["group", "supergroup"]))

bad_words = {'bad', 'word', 'badword', 'bad_word'}

def clean_words(text:str):
    return text.translate(str.maketrans('','', punctuation)).lower()

@user_gr_rout.message()
async def check_words(message: types.Message):
    if bad_words.intersection(message.text.lower().split()):
        clean_words(message.text.lower())
        await message.answer("you are using bad words! >:(")
        await message.delete()
        # await message.chat.ban(message.from_user.id)
 