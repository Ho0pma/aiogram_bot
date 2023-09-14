from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from handlers.client import FSM, command_main


# @dp.message_handler()
async def echo(message: types.Message):
    if message.text == '/main':
        await command_main(message)
    else:
        await bot.send_message(message.chat.id, 'Все тру приколы через /main')


# dp.register_message_handler(main_echo, state=FSM.after_help)
async def main_echo(message: types.Message):
    if message.text == '/main':
        await command_main(message)
    else:
        await bot.send_message(message.chat.id, 'Тоталитарный контроль: выбери команду из списка /main')


# @dp.callback_query_handler(lambda call: True, state=FSM.answer_choose)
async def answer_choose_echo(message: types.Message):
    if message.text == '/exit':
        await bot.send_message(message.chat.id, 'Никаких экзитов, сначала выбери мемассс')

    elif message.text == '/next':
        await bot.send_message(message.chat.id, 'Не пущу, сначала выбери meme')

    elif message.text == '/report':
        await bot.send_message(message.chat.id, 'Cначала выбери меньшее из двух зол')

    else:
        await bot.send_message(message.chat.id, 'Не знаю такого мемаса, знаю кнопочки одын или dva ла ла ла я бот')


async def answer_report_echo(message: types.Message):
    await bot.send_message(message.chat.id, 'Заверши опрос, плизз')


def register_handlers_other(message: Dispatcher):
    dp.register_message_handler(echo)
    dp.register_message_handler(answer_choose_echo, state=FSM.answer_choose)
    dp.register_message_handler(main_echo, state=FSM.after_main)
    dp.register_message_handler(answer_report_echo, state=FSM.answer_report)

