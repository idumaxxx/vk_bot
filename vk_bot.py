import requests
import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(
    token='vk1.a.z_93Mi0'
          '-2QIm9JHMffUariIkw1nIbJsTjYmb2chI21T397xaFqHxW6yEeo6kLmRKUTsVpDpG8cn54kkmF7P9rJgRtyUxudfeSHZm6NhY1r9ZqYRY0ZfKXOqLA_IrZDkB3O6m6MTCa2KcNEXj9ec7-KjKKJB0G-9qgBLyzUtdYZPwkTDjjIqcB99E1M8bYPcdPAAZbpTSVxE8YkKnSDiktw')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.from_user:
        # Слушаем longpoll, если пришло сообщение то:
        print(vk.users.get(user_ids=event.user_id)[0])
        # first_name = user_get['first_name']
        vk.messages.send(user_id=event.user_id,
                         message=f"Здравствуйте, {vk.users.get(user_ids=(event.user_id))[0]['first_name']}", random_id=int(time.time() * 10000))
