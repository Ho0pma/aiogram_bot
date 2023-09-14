import psycopg2

connection = psycopg2.connect(
    database='test',
    user='postgres',
    password='9299',
    host='localhost',
    port='5432'
)
print("Database opened successfully")

connection_two = psycopg2.connect(
    database='test',
    user='postgres',
    password='9299',
    host='localhost',
    port='5432'
)
print("Database opened successfully")


def insert_users(user_id: int, user_first_name: str, user_last_name: str, username: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" insert into users (user_id, user_first_name, user_last_name, username) "
                           "   values (%s,%s,%s,%s)                                                 ", (user_id,
                                                                                                        user_first_name,
                                                                                                        user_last_name,
                                                                                                        username))


def insert_images(user_id: int, image_id: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" insert into images (user_id, image_id) "
                           "   values (%s,%s)                       ", (user_id, image_id))


def insert_score(user_id: int, username: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" insert into score (user_id, username) "
                           "   values (%s,%s)                      ", (user_id, username,))


async def update_score(img_for_up_score: str, img_for_down_score: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id          "
                           "   from images           "
                           "   where image_id = '{}' ".format(img_for_up_score))

            user_winner = cursor.fetchone()[0]
            cursor.execute(" update score                      "
                           "   set user_score = user_score + 1 "
                           "   where user_id = {}              ".format(user_winner))

            cursor.execute(" select user_id          "
                           "   from images           "
                           "   where image_id = '{}' ".format(img_for_down_score))

            user_loser = cursor.fetchone()[0]
            cursor.execute(" update score                      "
                           "   set user_score = user_score - 1 "
                           "   where user_id = {}              ".format(user_loser))


async def select_score(user_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select num, user_score                                         "
                           "   from (select row_number() over w as num, user_id, user_score "
                           "           from score                                           "
                           "           window w as (order by user_score desc)) as f         "
                           "   where user_id = {}                                           ".format(user_id))

            row = cursor.fetchall()
            return row[0]


async def select_king_or_queen():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id                                                  "
                           "   from (select row_number() over w as num, user_id, user_score  "
                           "           from score                                            "
                           "           window w as (order by user_score desc)) as f          "
                           "   where num = 1                                                 ")

            superior_id = cursor.fetchone()[0]
            cursor.execute(" select user_first_name, user_last_name   "
                           "   from users                             "
                           "   where user_id = {}                     ".format(superior_id))

            user_info = cursor.fetchone()
            return user_info


async def update_count_report(image_id: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id          "
                           "   from images           "
                           "   where image_id = '{}' ".format(image_id))

            reported_id = cursor.fetchone()[0]  # id кого репортим
            cursor.execute(" update images                         "
                           "   set count_report = count_report + 1 "
                           "   where user_id = {} and              "
                           "         image_id = '{}'               ".format(reported_id, image_id))


async def update_both_count_report(first_image: str, second_image: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id                   "
                           "   from images                    "
                           "   where image_id in ('{}', '{}') ".format(first_image, second_image))

            both_reported_id = cursor.fetchall()
            first_reported_id = both_reported_id[0][0]
            second_reported_id = both_reported_id[1][0]

            cursor.execute(" update images                         "
                           "   set count_report = count_report + 1 "
                           "   where user_id in ({}, {}) and       "
                           "         image_id in ('{}', '{}')      ".format(first_reported_id, second_reported_id,
                                                                            first_image, second_image))


async def insert_reports(sender_report_id: int, image_id: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" insert into reports (sender_report_id, image_id) "
                           "   values(%s,%s)                                  ", (sender_report_id, image_id))


async def insert_two_reports(sender_report_id: int, first_image_id: str, second_image_id: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" insert into reports (sender_report_id, image_id) "
                           "   values(%s,%s), (%s,%s)                         ", (sender_report_id, first_image_id,
                                                                                  sender_report_id, second_image_id))


def select_users_and_images_full_list():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id, image_id "
                           "   from images            ")

            images_list = cursor.fetchall()
            return images_list


def select_images(user_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select image_id           "
                           "   from images             "
                           "   where user_id != {}     ".format(user_id))

            images_list = cursor.fetchall()
            return images_list


def check_count_reports():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id, image_id  "
                           "   from images             "
                           "   where count_report >= 3 ")

            reported_id_list = cursor.fetchall()
            return reported_id_list


def delete_reported_images():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" delete from images                              "
                           "   where image_id in (select image_id            "
                           "                        from images              "
                           "                        where count_report >= 3) ")


def update_count_reported_images(reported_user_id, count_reports):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" update users                                             "
                           "   set count_reported_images = count_reported_images + {} "
                           "   where user_id = {}                                     ".format(count_reports,
                                                                                               reported_user_id))


def select_count_reported_images_more_ten():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id                          "
                           "   from users                            "
                           "   where count_reported_images >= 10 ")

            who_need_block_list = cursor.fetchall()
            return who_need_block_list


def update_count_reported_images_to_zero(user_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" update users                     "
                           "   set count_reported_images = 0 "
                           "   where user_id = {}             ".format(user_id))


def select_users_whom_need_block():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id, first_unblock_date    "
                           "   from blocks                         "
                           "   where first_unblock_date like '%-%' ")

            ban_list = cursor.fetchall()
            return ban_list


def select_users_who_have_block():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select user_id, first_unblock_date      "
                           "   from blocks                           "
                           "   where first_unblock_date = 'True' and "
                           "         second_ban = '0'                ")

            ban_list = cursor.fetchall()
            return ban_list


def insert_to_blocks_first_ban(user_id: int, first_unblock_date: str):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" insert into blocks "
                           "   values (%s,%s)   ", (user_id, first_unblock_date))


def update_blocks_second_ban(user_id: int):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" update blocks                                                "
                           "   set first_unblock_date = '9999-99-99', second_ban = 'True' "
                           "   where user_id = {}                                         ".format(user_id))


def update_first_unblock_date(unblock_date: str):
    with connection_two:
        with connection_two.cursor() as cursor:
            cursor.execute(" update blocks                     "
                           "   set first_unblock_date = 'True' "
                           "   where first_unblock_date = '{}' ".format(unblock_date))



