import vk_api
from random import choice, randrange
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
vars=['камень','ножницы','бумага']

for event in longpoll.listen():
  if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text.lower() in vars:
    if event.from_user:
      user = event.text.lower()
      bot  = choice(vars)
      vk.messages.send(user_id=event.user_id, message=bot, random_id=randrange(1,100000))
      out = ""
      if bot == 'ножницы':
        if user =='ножницы':
          out = 'ничья'
        elif user == 'бумага':
          out = 'Ты Проиграл!'
        else:
          out = 'Ты Выйграл!'

      elif bot =='бумага':
        if user =='бумага':
          out = 'ничья'
        elif user == 'камень':
          out = 'Ты Проиграл!'
        else:
          out = 'Ты Выйграл!'

      elif bot =='камень':
        if user =='камень':
          out = 'ничья'
        elif user == 'ножницы':
          out = 'Ты Проиграл!'
        else:
          out = 'Ты Выйграл!'
      else:
        out = 'Нет такого варинта'

      vk.messages.send(user_id=event.user_id, message=out, random_id=randrange(1,100000))
