# d = {1: [1, 2, 3]}
# print(d)



# import db, copy
# from collections import defaultdict
# a = db.select_users_and_images_full_list()
#
# d = defaultdict(list)
# print(a)
# for element in a:
#     d[element[0]].append(element[1])
#
# print(d)

#
# print(a)
# print(dict(a))

#
# def take_images():
#     a = db.select_users_and_images_full_list()
#     return a
#
#
# b = copy.deepcopy(take_images())
#
# print(b)
# del b[0]
# del b[0]
# del b[0]
#
# print(b)
#
# b = copy.deepcopy(take_images())
# print(b)




# a = set()
# a.add(6)
# a.add(7)
# print(a)
# a.remove(6)
# print(a)

#
# from datetime import date, timedelta
#
# print(date.today())
# unblock_date = str(date.today() + timedelta(days=7))
# print(unblock_date)
# print(type(unblock_date))





# import time
# import threading
#
#
# def data():
#     while True:
#         print('+')
#         time.sleep(5)
#
#
# thr = threading.Thread(target=data, args=(), name='thr-1')
# thr.start()
#
# for i in range(100):
#     print('-')
#     time.sleep(4)


# from collections import Counter
#
# reported_list = [(1, '1.png'), (2, '2.png'), (1, '3.png'), (2, '4.png'), (3, '5.png')]
#
# reported_id_list = []
# reported_image_list = []
#
# for element in reported_list:
#     reported_id_list.append(element[0])
#     reported_image_list.append(element[1])
#
# print(reported_id_list)
# print(reported_image_list)
#
# reported_id_dict = Counter(reported_id_list)
# print(reported_id_dict)


#
# a = [1, 1, 2, 2, 3]
# b = Counter(a)
#
# for value in b.values():
#     print(value)



#
# for i in range(4):
#     print(i)


# import random
# n = 0
# while n <= 1000:
#     def what_cat():
#         cat = random.randint(1, 500)
#
#         if cat > 499:
#             return ':black_cat:'
#         else:
#             return ':cat:'
#
#     print(what_cat())
#     n += 1


# a = ([1,], [2,])
# for i in a:
#     print(i[0])
# print(a[0])
# print(a)


# # @bot.message_handler(commands=['choose'], state=FSM.after_main)
# async def command_choose(message: types.Message, state: FSMContext):
#     old_name_end = '/Users/elizavetatrusova/PycharmProjects/aiogram_bot/images/images_end'
#     new_name_end = '/Users/elizavetatrusova/PycharmProjects/aiogram_bot/images/end'
#     old_name_start = '/Users/elizavetatrusova/PycharmProjects/aiogram_bot/images/images_start'
#     new_name_start = '/Users/elizavetatrusova/PycharmProjects/aiogram_bot/images/istart'
#
#     image_names = os.listdir(old_name_start)
#     image_names.remove('.DS_Store')
#
#     if len(image_names) == 1:
#         chose_last_img = image_names[0]
#         path_last_img = old_name_start + '/' + chose_last_img
#         destination_path = old_name_end + '/'
#         shutil.move(path_last_img, destination_path)
#
#     if not image_names or len(image_names) == 1:
#         os.rename(old_name_end, new_name_end)
#         os.rename(old_name_start, new_name_start)
#         os.rename(new_name_start, old_name_end)
#         os.rename(new_name_end, old_name_start)
#
#         image_names = os.listdir(old_name_start)
#         image_names.remove('.DS_Store')
#
#     random_first_img = random.choice(image_names)
#
#     path_first_img = old_name_start + '/' + random_first_img
#     image_one = open(path_first_img, 'rb')
#
#     await bot.send_message(message.chat.id, 'Выбирай рофл!!! ОДЫН или DVA?', reply_markup=kb_client_choose)
#     await bot.send_photo(message.chat.id, image_one)
#
#     destination_path = old_name_end + '/'
#     shutil.move(path_first_img, destination_path)
#
#     # ----------------------------------------------------------------------------------------#
#
#     image_names = os.listdir(old_name_start)
#     image_names.remove('.DS_Store')
#
#     random_second_img = random.choice(image_names)
#
#     path_second_img = old_name_start + '/' + random_second_img
#     image_two = open(path_second_img, 'rb')
#
#     await bot.send_photo(message.chat.id, image_two)
#     await state.set_data({'random_first_img': random_first_img, 'random_second_img': random_second_img, 'user_id':
#         message.from_user.id})
#
#     destination_path = old_name_end + '/'
#     shutil.move(path_second_img, destination_path)
#
#     # ----------------------------------------------------------------------------------------#
#
#     markup_inline = types.InlineKeyboardMarkup()
#     item_one = types.InlineKeyboardButton(text='ОДЫН', callback_data='item_one')
#     item_two = types.InlineKeyboardButton(text='DVA', callback_data='item_two')
#
#     markup_inline.add(item_one, item_two)
#     await bot.send_message(message.chat.id, 'ВЫБИРАЙ МЕМАСИК!!!', reply_markup=markup_inline)
#     await FSM.answer_choose.set()


# msg = await bot.send_message(message.chat.id, 'Text')
# # time.sleep(1)
# # await bot.edit_message_text(chat_id=message.chat.id, message_id=msg_to_edit.message_id, text='g')
# message_id = msg['message_id']
# print(message_id)
# await state.set_data({'message_id': message_id})
# await state.finish()
# print(message.chat.id)


# data_to_edit = await state.get_data()
# print(data_to_edit)
# message_id = data_to_edit['message_id']
# print(message_id)
# await state.finish()
# await FSM.after_main.set()


# print(message.chat.id)
# await bot.edit_message_text(text='l', chat_id=message.chat.id, message_id=message_id, reply_markup=ReplyKeyboardRemove())
# , reply_markup = ReplyKeyboardRemove()


# who_need_block_list = db_select_who_need_block()
# # who_need_block_forever = db_select_who_need_block_forever()
#



# if who_need_block_list:
#     # update_data()
#     try:
#         for num, banned_id in enumerate(who_need_block_list):
#             user_id = banned_id[0]
#
#             if user_id not in data.banned_users_dict:
#                 unblock_date = str(date.today() + timedelta(days=7))
#                 db_insert_to_blocks_first_ban(user_id=user_id, first_unblock_date=unblock_date)
#                 db_update_who_no_need_block(user_id=user_id)
#                 update_data()
#                 print(num + 1, '-> user_id:', user_id, 'was blocked')
#
#             else:
#                 # update_d
#                 print(2)
#                 db_update_blocks_second_ban(user_id=user_id)
#                 db_update_who_no_need_block(user_id=user_id)
#                 update_data()
#                 print('The user:', user_id, 'received a second lock')
#     except:
#         print('Smth wrong')
# else:
#     print('No one who need to block')


# if who_need_block_list:
#     update_data()
#     try:
#         for num, banned_id in enumerate(who_need_block_list):
#             user_id = banned_id[0]
#             unblock_date = str(date.today() + timedelta(days=7))
#
#             db_insert_to_blocks_first_ban(user_id=user_id, first_unblock_date=unblock_date)
#             db_update_who_no_need_block(user_id=user_id)
#             print(num + 1, '-> user_id:', user_id, 'was blocked')
#
#     except:
#         print('Smth wrong')
# else:
#     print('No one who need to block first time')
#
#     if who_need_block_forever_list:
#         for banned_id in who_need_block_forever_list:
#             user_id = banned_id[0]
#             db_update_blocks_second_ban(user_id=user_id)
#
# print(who_need_block_forever_list)


# schedule.run_pending()
# schedule.every().day.at('19:14').do(check_reports)
# time.sleep(1)


# a = '2022-11-23'
# d = {6629: '2022-11-23'}
# print(d)
# if a in d.values():
#     print('+')

#
#
# async def command_choose(message: types.Message, state: FSMContext):
#     if len(data.image_names) == 1:
#         data.image_names = data.image_names + data.storage
#         data.storage.clear()
#
#     if not data.image_names:
#         data.image_names = data.image_names + data.storage
#         data.storage.clear()
#
#     random_images = random.sample(data.image_names, 2)
#
#     await state.set_data({'random_first_img': random_images[0], 'random_second_img': random_images[1], 'user_id':
#                          message.from_user.id})
#
#     index_one = data.image_names.index(random_images[0])
#     del data.image_names[index_one]
#     index_two = data.image_names.index(random_images[1])
#     del data.image_names[index_two]
#
#     for image in random_images:
#         data.storage.append(image)
#
#     color_cat = await what_cat()
#     await bot.send_message(message.chat.id, emoji.emojize(color_cat), reply_markup=ReplyKeyboardRemove())
#
#     media = MediaGroup()
#     media.attach_photo(photo=InputFile(data.images_path + '/' + random_images[0]))
#     media.attach_photo(photo=InputFile(data.images_path + '/' + random_images[1]))
#     await message.answer_media_group(media=media)
#
#     await bot.send_message(message.chat.id, 'ВЫБИРАЙ МЕМАСИК!!!', reply_markup=kb_inline_choose)
#     await FSM.answer_choose.set()




# -------------

#  FIRST
# users_and_images_without_one_list = []
# for value in users_and_images_without_one_dict.values():
#     users_and_images_without_one_list += value
#
# print('bez usera_list --->', users_and_images_without_one_list)
#
# if not users_and_images_without_one_list or len(users_and_images_without_one_list) == 1:
#     print(1)
#     random_images = random.sample(data.storage, 2)
#     print('storage', data.storage)
#     print('random', random_images)
#     users_and_images_full_list = data.take_users_and_images()
#     users_and_images_full_dict = defaultdict(list)
#
#     for element in users_and_images_full_list:
#         users_and_images_full_dict[element[0]].append(element[1])
#
#     print(users_and_images_without_one_list)
#     print(users_and_images_without_one_dict)
#
# else:
#     random_images = random.sample(users_and_images_without_one_list, 2)
#     print('random iz lista', random_images)
#
# for image in random_images:
#     data.storage.append(image)
#
# for value in data.users_and_images_full_dict.values():
#     for element in value:
#         if element == random_images[0] or element == random_images[1]:
#             value.remove(element)


# SECOND
# print('start --->', data.users_and_images_full_dict)
# users_and_images_without_one_dict = dict()
#
# for key, value in data.users_and_images_full_dict.items():
#     if key != message.from_user.id:
#         users_and_images_without_one_dict[key] = value
#
# print('bez usera_dict --->', users_and_images_without_one_dict)
#
# random_keys = random.sample(set(users_and_images_without_one_dict), 2)
# print(random_keys)
# random_images = []
# for random_key in random_keys:
#     for key, value in users_and_images_without_one_dict.items():
#         if key == random_key:
#             random_images.append(random.choice(value))
#
# print(random_images)
#
# for value in data.users_and_images_full_dict.values():
#     for element in value:
#         if element == random_images[0] or element == random_images[1]:
#             value.remove(element)
#
# print('konec', data.users_and_images_full_dict)




#---------
# from collections import defaultdict


# def take_users_and_images():
#     users_and_images_full = db.select_users_and_images_full_list()
#     return users_and_images_full
#
#
# users_and_images_full_list = take_users_and_images()
# users_and_images_full_dict = defaultdict(list)
#
# for element in users_and_images_full_list:
#     users_and_images_full_dict[element[0]].append(element[1])
#_------





d = {'a': 1}
print(d['a'])










