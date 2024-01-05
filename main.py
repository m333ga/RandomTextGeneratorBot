from aiogram import Bot, executor, Dispatcher, types
from config import bot_token
import random as rn

bot = Bot(bot_token)
dp = Dispatcher(bot = bot)

@dp.message_handler( commands = ['start'] )
async def start(msg: types.Message) -> None:
    await msg.answer('Hello. This is a bot for generating random text.')

@dp.message_handler( commands = ['random_word'] )
async def echo(msg: types.Message) -> None:
    with open('Text Languages/ru_list.txt', encoding='utf-8') as f:
        await msg.answer(rn.choice(f.read().splitlines()).lower())
    
if __name__ == "__main__":
    executor.start_polling(dp)