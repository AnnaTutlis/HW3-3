from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot
from keyboards.client_kb import cancel_marcup

class FSMAdmin(Foods):
    photo_food = State()
    name_food = State()
    description_food = State()
    price_food = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'food':
        await FSMAdmin.photo.set()
        await bot.send_message(
            message.chat.id,
            f"Добрый день! {message.from_user.full_name},Что Вам показать?",
            reply_markup=cancel_marcup
        )
    else:
        await bot.send_photo()
        question = "Выберите категорию"
        answers = [
        'Фото блюда',
        'Название блюда',
        'Описание блюда',
        'Цена блюда'

    ]

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Discription'] = message.text
    await FSMAdmin.next()
    await message.answer("Описание блюда")


async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Name Food'] = message.text
    await FSMAdmin.next()
    await message.answer("Название блюда")


async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['Price'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("Посмотреть цену")
    except:
        await message.answer("Только числа!!!")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply("Спасибо за обращение")

def register_hendler_fsmanketa(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*', commands="cancel")
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['register'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_surname, state=FSMAdmin.surname)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
