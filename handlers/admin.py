import time, threading, shutil, datetime, schedule
import data, db, os

from collections import Counter
from datetime import date, timedelta


def update_data():
    data.users_whom_need_block_dict = dict(db.select_users_whom_need_block())
    print(data.users_whom_need_block_dict)
    data.users_who_have_block_dict = dict(db.select_users_who_have_block())
    print(data.users_who_have_block_dict)


def update_directory():
    data.image_names = os.listdir(data.images_path)
    data.image_names.remove('.DS_Store')
    data.storage = []


def check_reports():
    print('-------------------------------------------')
    reported_list = db.check_count_reports()
    if reported_list:
        reported_id_list = []
        reported_image_list = []

        for element in reported_list:
            reported_id_list.append(element[0])
            reported_image_list.append(element[1])

        reported_id_dict = Counter(reported_id_list)

        for num, image in enumerate(reported_image_list):
            shutil.move(data.images_path + '/' + image, data.reported_images_path + '/' + image)
            print(num + 1, ': Reported image moved')

        db.delete_reported_images()

        for key, value in reported_id_dict.items():
            db.update_count_reported_images(reported_user_id=key, count_reports=value)

        update_directory()

    else:
        print('There are no reported images on', datetime.date.today())

    who_need_block_list = db.select_count_reported_images_more_ten()
    update_data()

    if who_need_block_list:
        try:
            for num, banned_id in enumerate(who_need_block_list):
                user_id = banned_id[0]

                if user_id not in data.users_whom_need_block_dict and user_id not in data.users_who_have_block_dict:
                    unblock_date = str(date.today() + timedelta(days=7))
                    db.insert_to_blocks_first_ban(user_id=user_id, first_unblock_date=unblock_date)
                    db.update_count_reported_images_to_zero(user_id=user_id)
                    update_data()
                    print(num + 1, '-> user_id:', user_id, 'was blocked')

                else:
                    db.update_blocks_second_ban(user_id=user_id)
                    update_data()
                    print('The user:', user_id, 'received a second lock')
        except:
            print('Smth wrong')
    else:
        print('No one who need to block')


def unblock():
    print('-------------------------------------------')
    today = str(date.today())
    if today in data.users_whom_need_block_dict.values():
        db.update_first_unblock_date(unblock_date=today)
        print('Someone got unblocked on', today)
    else:
        print('No one needs to unblock, on', today)


def start_check_reports():
    while True:
        check_reports()
        # time.sleep(21600)
        time.sleep(30)


def start_unblock():
    while True:
        unblock()
        # print('unblock')
        # time.sleep(21600)
        time.sleep(35)


def start_thread_check():
    thr = threading.Thread(target=start_check_reports, args=(), name='thr-check')
    thr.start()
    print('\nLaunched -->', thr.name)


def start_thread_unblock():
    thr = threading.Thread(target=start_unblock, args=(), name='thr-unblock')
    thr.start()
    print('\nLaunched -->', thr.name)
