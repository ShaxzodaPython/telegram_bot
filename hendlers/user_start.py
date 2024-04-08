from keyboards.default.user import user_main_menu
from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup





@dp.message_handler(commands='start')
async def user_start(message: types.Message):
    if db.get_user_by_chat_id(chat_id=message.chat.id):
        text = "Assalomu alaykum, xush kelibsiz"
        await message.answer(text=text)
    else:
        text = "Assalomu alaykum, ismingizni kiriting"
        await message.answer(text=text, reply_markup=user_main_menu)
        await FSMContext.full_name.set()

    @dp.message_handler(state=FSMContext.full_name)
    async def get_full_name(message: types.Message, state: FSMContext):
        await state.update_data(full_name=message.text, chat_id=message.chat.id)
        text = "Telefon raqamingiz"
        await message.answer(text=text)
        await FSMContext.phone_number.set()


    @dp.message_handler(state=FSMContext.phone_number)
    async def get_full_name(message: types.Message, state: FSMContext):
        await state.update_data(phone_number=message.text)
        text = "Manzil"
        await message.answer(text=text)
        await FSMContext.location.set()


    @dp.message_handler(state=FSMContext.location)
    async def get_full_name(message: types.Message, state: FSMContext):
        await state.update_data(location=message.text)

        data = await state.get_data()
        if db.add_user(data):
            text = "Muvaffaqiyatli bajarildi"

        else:
            text = "Muammo yuz berdi"


        await message.answer(text=text, reply_markup=user_main_menu)
        await state.finish()


