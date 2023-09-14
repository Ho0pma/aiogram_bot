import os
import db


images_path = '/Users/elizavetatrusova/PycharmProjects/aiogram_bot/images/all_images'
image_names = os.listdir(images_path)
image_names.remove('.DS_Store')
storage = []

with open('/Users/elizavetatrusova/PycharmProjects/aiogram_bot/info/instructions.txt') as lines:
    instruction = lines.read()

reported_images_path = '/Users/elizavetatrusova/PycharmProjects/aiogram_bot/images/reported_images'
reported_image_names = os.listdir(reported_images_path)

users_whom_need_block_dict = dict(db.select_users_whom_need_block())
users_who_have_block_dict = dict(db.select_users_who_have_block())





