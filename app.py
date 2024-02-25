from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv
import os
import random
load_dotenv(find_dotenv())
from handlers.user_private import user_pr_rout
from handlers.user_groups import user_gr_rout
from common.bot_cmds_list import listOfCommands

bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()


dp.include_routers(user_pr_rout)
dp.include_router(user_gr_rout)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=listOfCommands, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

asyncio.run(main())