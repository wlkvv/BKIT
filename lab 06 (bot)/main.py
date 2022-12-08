from random import choice
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text


msg_set = open('meow.txt', 'r', encoding='utf-8').read().splitlines()
bot = Bot(token="Secret")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Получить приятное сообщение", "Получить список сообщений"]
    keyboard.add(*buttons)
    await message.answer("Чего желаете?", reply_markup=keyboard)


@dp.message_handler(Text(equals="Получить приятное сообщение"))
async def first(message: types.Message):
    await message.reply(choice(msg_set))

@dp.message_handler(Text(equals="Получить список сообщений"))
async def second(message: types.Message):
    a = str(""+msg_set[i]+" " for i in range(len(msg_set)))
    for i in msg_set:
        await message.answer(i)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
