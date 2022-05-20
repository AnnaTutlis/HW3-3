from aiogram import types, Dispatcher
from config import bot, dp



def register_hendler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)