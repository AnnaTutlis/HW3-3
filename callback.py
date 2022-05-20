from aiogram import types, Dispatcher
from config import bot, dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode


# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
    markup.add(button_call_2)

    question = "Выберите категорию"
    answers = [
        'Фото блюда',
        'Название блюда',
        'Описание блюда',
        'Цена блюда'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )
    photo = open("media/problem1.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")