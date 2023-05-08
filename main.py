import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import BotBlocked
from os import getenv
from sys import exit
from defs import bot_block_error, cmd_top, cmd_stat, cmd_rank, other_msg
from members import member_start
from fcm import Orders


# переменные
Token = getenv("TOKEN_STAT")
if not Token:
    exit("Error: no token provided")
bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


dp.register_errors_handler(bot_block_error, exception=BotBlocked)
dp.register_message_handler(cmd_top, commands="top")
dp.register_message_handler(cmd_stat, commands="stat")
dp.register_message_handler(cmd_rank, commands="rank")
dp.register_chat_member_handler(member_start)
dp.register_message_handler(other_msg)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
