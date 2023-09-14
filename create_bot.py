from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot('5659583355:AAHCDo_OzhPkGutSllyJB27eKKIN8hdY3D8')
dp = Dispatcher(bot, storage=storage)
