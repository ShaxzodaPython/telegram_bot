from keyboards.default.user import user_main_menu
from loader import dp, db
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup





@dp.message_handler(text='Rasm joylash')
async def user_upload_photo(message: types.Message, state: FSMContext):
    if db.get_user_photo_by_chat_id(chat_id=message.chat_id):
        text = "Rsam mavjud"
    else:
        text = "Rasm yuboring"
        await state.set_state("user_upload_photo")
    await message.answer(text=text)


@dp.message_handler(state="user_upload_photo")
async def user_upload_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].file_id, chat_id=message.chat.id)
    data = await state.get_data()
    if db.add_photo(data):
        text = "Rasm qo'shildi"
    else:
    text = "Rasm qo'shilmadi"

    text = "Rasm joylandi"
    await message.answer(text=text)
    await state.finish()