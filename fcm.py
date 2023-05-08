import logging
from aiogram.dispatcher.filters.state import State, StatesGroup
logger = logging.getLogger(__name__)


class Orders(StatesGroup):
    waiting_id = State()
    waiting_photo = State()
    waiting_geo = State()
