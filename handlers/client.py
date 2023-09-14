import datetime
import os, shutil, random, emoji
import data, db
from datetime import date, timedelta

from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client_choose, kb_client_main, kb_inline_choose, kb_inline_report
from aiogram.types import ReplyKeyboardRemove
from aiogram.types.input_file import InputFile
from aiogram.types.input_media import MediaGroup

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from collections import Counter
from collections import defaultdict


class FSM(StatesGroup):
    get_photo = State()
    no_photo = State()
    after_main = State()
    answer_choose = State()
    after_choose = State()
    answer_report = State()


async def update_data():
    data.image_names = os.listdir(data.images_path)
    data.image_names.remove('.DS_Store')
    data.storage = []


async def what_cat():
    cat = random.randint(1, 500)
    if cat > 499:
        return ':black_cat:'
    else:
        return ':cat:'


# @dp.message_handler(user_id=data.users_whom_need_block_dict)
@dp.message_handler(lambda *args, **kwargs: args[0]['from']['id'] in data.users_whom_need_block_dict)
async def check_ban_list(message: types.Message):
    for key, value in data.users_whom_need_block_dict.items():
        if value == '9999-99-99':
            await bot.send_message(message.chat.id, 'Сори, но пош$л нах><уй ')
        if value != '9999-99-99':
            await bot.send_message(message.chat.id, 'На вас поступило много жалоб.. пока запишем вас карандашиком! \n'
                                                    'Поэтому одобряем вам отпуск!! на недельку! до ' + data.
                                   users_whom_need_block_dict[message.from_user.id] + ', приходите отдохнувшим !1!')
    return True


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message, state: FSMContext):
    try:
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name
        user_last_name = message.from_user.last_name
        username = message.from_user.username

        db.insert_users(user_id=user_id, user_first_name=user_first_name, user_last_name=user_last_name,
                        username=username)

        db.insert_score(user_id=user_id, username=username)

        await bot.send_message(message.chat.id,
                               'Приветик, ' + user_first_name + '! Предлагаю зачиллиться и порофлить!!!')
        await command_main(message)

    except:
        await bot.send_message(message.from_user.id, 'Велком бэк, май диар!')
        await command_main(message)


# @dp.message_handler(commands=['main'])
async def command_main(message: types.Message):
    await bot.send_message(message.chat.id, data.instruction, reply_markup=kb_client_main)
    await FSM.after_main.set()


# @bot.message_handler(commands=['choose'], state=FSM.after_main)
async def command_choose(message: types.Message, state: FSMContext):
    if len(data.image_names) == 1:
        data.image_names = data.image_names + data.storage
        data.storage.clear()

    if not data.image_names:
        data.image_names = data.image_names + data.storage
        data.storage.clear()

    random_images = random.sample(data.image_names, 2)

    await state.set_data({'random_first_img': random_images[0], 'random_second_img': random_images[1], 'user_id':
        message.from_user.id})

    index_one = data.image_names.index(random_images[0])
    del data.image_names[index_one]
    index_two = data.image_names.index(random_images[1])
    del data.image_names[index_two]

    for image in random_images:
        data.storage.append(image)

    color_cat = await what_cat()
    await bot.send_message(message.chat.id, emoji.emojize(color_cat), reply_markup=ReplyKeyboardRemove())

    media = MediaGroup()
    media.attach_photo(photo=InputFile(data.images_path + '/' + random_images[0]))
    media.attach_photo(photo=InputFile(data.images_path + '/' + random_images[1]))
    await message.answer_media_group(media=media)

    await bot.send_message(message.chat.id, 'ВЫБИРАЙ МЕМАСИК!!!', reply_markup=kb_inline_choose)
    await FSM.answer_choose.set()


# @dp.callback_query_handler(lambda call: True, state=FSM.answer_choose)
async def answer_choose(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()

    if call.data == 'item_one':
        img_for_up_score = data['random_first_img']
        img_for_down_score = data['random_second_img']
        await db.update_score(img_for_up_score=img_for_up_score, img_for_down_score=img_for_down_score)

    elif call.data == 'item_two':
        img_for_up_score = data['random_second_img']
        img_for_down_score = data['random_first_img']
        await db.update_score(img_for_up_score=img_for_up_score, img_for_down_score=img_for_down_score)

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await bot.send_message(call.message.chat.id, 'Отлично! Заряжай /next !!!', reply_markup=kb_client_choose)
    await FSM.after_choose.set()


# @bot.message_handler(commands=['exit'], state=FSM.after_choose)
async def command_exit_choose(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'бб, найс порофлили! Тапни на /main, если хочешь попасть в главное '
                                                 'меню',
                           reply_markup=ReplyKeyboardRemove())
    await state.finish()


# @dp.message_handler(commands=['report'], state=FSM.after_choose)
async def command_report(message: types.Message, state: FSMContext):
    data = await state.get_data()
    first_img = data['random_first_img']
    second_img = data['random_first_img']

    await bot.send_message(message.chat.id, 'Какой мемасик репортим?', reply_markup=kb_inline_report)
    await FSM.answer_report.set()


# dp.register_callback_query_handler(answer_report, lambda call: True, state=FSM.answer_report)
async def answer_report(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    sender_report_id = data['user_id']
    if call.data != 'miss':
        try:
            if call.data == 'first_item_for_report':
                selected_img = data['random_first_img']
                # await db.insert_reports(sender_report_id=sender_report_id, image_id=selected_img)
                await db.update_count_report(image_id=selected_img)

            elif call.data == 'second_item_for_report':
                selected_img = data['random_second_img']
                # await db.insert_reports(sender_report_id=sender_report_id, image_id=selected_img)
                await db.update_count_report(image_id=selected_img)

            elif call.data == 'report_both':
                first_image = data['random_first_img']
                second_image = data['random_second_img']
                # await db.insert_two_reports(sender_report_id=sender_report_id, first_image_id=first_image,
                #                             second_image_id=second_image)
                await db.update_both_count_report(first_image=first_image, second_image=second_image)

            await bot.send_message(call.message.chat.id, 'Репорт аксептид!')

        except:
            await bot.send_message(call.message.chat.id, 'Ты уже репортил этот мемас! Выбери другую опцию')

    else:
        await bot.send_message(call.message.chat.id, 'убрали, забыли, больше не миссай')

    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await FSM.after_choose.set()


# @bot.message_handler(commands=['next'], state=FSM.after_choose)
async def command_next(message: types.Message, state: FSMContext):
    await command_choose(message, state)


# @dp.message_handler(commands='meme', state=FSM.after_main)
async def command_meme(message: types.Message):
    await FSM.get_photo.set()
    await message.answer('Заливай мемас!')


# @dp.message_handler(content_types=['photo'], state=FSM.get_photo)
async def load_photo(message: types.Message, state: FSMContext):
    user_photo_id = message.photo[-1].file_id
    file_photo = await bot.get_file(user_photo_id)

    filename, file_extension = os.path.splitext(file_photo.file_path)  # file_extension - расширение файла
    downloaded_file_photo = await bot.download_file(file_photo.file_path)

    user_id = message.from_user.id
    image_id = user_photo_id + file_extension
    dir_name = data.images_path + '/' + str(user_id)

    def write_file():
        with open(data.images_path + '/' + image_id, 'wb') as new_file:
            downloaded_file_photo.seek(0)  # ставит указатель на начало (читает по байтово)
            new_file.write(downloaded_file_photo.read())

    write_file()

    # try:               # попытка разбить на папочки картинки
    #     write_file()
    # except:
    #     os.mkdir(dir_name)
    #     write_file()

    db.insert_images(user_id=user_id, image_id=image_id)

    await update_data()
    await bot.send_message(message.chat.id, 'мемас принят')
    await FSM.after_main.set()


# @dp.message_handler(state=FSM.get_photo)
async def no_photo(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, message.from_user.first_name + ', это не фото, ну ты чего')
    await FSM.after_main.set()


# @dp.message_handler(commands=['score'], state=FSM.after_main)
async def command_score(message: types.Message, state: FSMContext):
    user_info = await db.select_score(user_id=message.from_user.id)
    await bot.send_message(message.chat.id, message.from_user.first_name + ', твоя позиция в таблице: '
                           + str(user_info[0]) +
                           '\n            кол-во людей прооравших с твоих мемов: ' + str(user_info[1]))
    await FSM.after_main.set()


# @dp.message_handler(commands=['king', 'queen'], state=FSM.after_main)
async def command_king_or_queen(message: types.Message, state: FSMContext):
    user_info = await db.select_king_or_queen()
    await bot.send_message(message.chat.id, 'Бест приколист(ка): ' + user_info[0] + ' ' + user_info[1])
    await FSM.after_main.set()


def register_handlers_client(message: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_main, commands=['main'])
    dp.register_message_handler(command_choose, commands=['choose'], state=FSM.after_main)
    dp.register_message_handler(command_report, commands=['report'], state=FSM.after_choose)
    dp.register_message_handler(command_exit_choose, commands=['exit'], state=FSM.after_choose)
    dp.register_message_handler(command_next, commands=['next'], state=FSM.after_choose)
    dp.register_message_handler(command_meme, commands=['meme'], state=FSM.after_main)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSM.get_photo)
    dp.register_message_handler(no_photo, state=FSM.get_photo)
    dp.register_message_handler(command_score, commands=['score'], state=FSM.after_main)
    dp.register_message_handler(command_king_or_queen, commands=['king', 'queen'], state=FSM.after_main)


def register_callback_query_handler_client(message: Dispatcher):
    dp.register_callback_query_handler(answer_choose, lambda call: True, state=FSM.answer_choose)
    dp.register_callback_query_handler(answer_report, lambda call: True, state=FSM.answer_report)
