from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import types

b3 = KeyboardButton('/exit')
b4 = KeyboardButton('/report')
b5 = KeyboardButton('/next')


b6 = KeyboardButton('/meme')
b7 = KeyboardButton('/score')
b8 = KeyboardButton('/choose')

kb_client_choose = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_choose.row(b3, b4, b5)

kb_client_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_main.row(b6, b7, b8)

kb_inline_choose = types.InlineKeyboardMarkup()
item_one = types.InlineKeyboardButton(text='ОДЫН', callback_data='item_one')
item_two = types.InlineKeyboardButton(text='DVA', callback_data='item_two')
kb_inline_choose.add(item_one, item_two)

kb_inline_report = types.InlineKeyboardMarkup()
first_item_for_report = types.InlineKeyboardButton(text='First', callback_data='first_item_for_report')
second_item_for_report = types.InlineKeyboardButton(text='Second', callback_data='second_item_for_report')
report_both = types.InlineKeyboardButton(text='Both', callback_data='report_both')
miss = types.InlineKeyboardButton(text='Miss', callback_data='miss')
kb_inline_report.add(first_item_for_report, second_item_for_report).add(report_both, miss)
