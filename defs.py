import logging
from aiogram import types
import re
from variables import thanks
from database import user_rate


my_log = logging.getLogger(__name__)
all_id = []
ph = []
lat = []
lon = []


async def cmd_stat(message: types.Message):
    #await message.reply("У Вас %s баллов" % ('x'))
    rate = user_rate(message.from_user.id)
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=message.from_user.id, text="У Вас {} баллов".format(rate))


async def cmd_rank(message: types.Message):
    #await message.reply("Вы на %s месте" % ('x'))
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=message.from_user.id, text="Вы на {} месте".format('x'))


async def cmd_top(message: types.Message):
    #await message.reply("Первый %s" % ('Не вы'))
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=message.from_user.id, text="Первый {}".format('Не вы'))


async def bot_block_error(message: types.Message):
    await message.reply("Что то не так. Давай снова /start")
    await message.bot.send_message(chat_id=message.from_user.id, text="Что то не так. Давай снова /start")


async def other_msg(message: types.Message):
    if message.reply_to_message:
        print('Пользователь {} ответил '
              'пользователю {}: "{}" на сообщение: "{}"'.format(message.from_user.username,
                                                                message.reply_to_message.from_user.username,
                                                                message.text,
                                                                message.reply_to_message.text))
        karma = 0
        for word in thanks:
            res = re.search(r'\b' + word + r'\b', message.text.lower())
            if res:
                karma = 1
        if karma == 1:
            print('{} Вам благодарность от {}. +1 в карму )'.format(message.reply_to_message.from_user.username,
                                                                    message.from_user.username))
        else:
            print('other msg')
