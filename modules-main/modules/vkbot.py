import random
from course import *
from wiki import *
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

token = "vk1.a.Q0iEQkCP5ZedgRQkSrKwNI4tILjXp3QHcEioS3u-yHfLQrmaEmZcxBV7lZWX-NMsJbUhyQGNN2wRkQtIc_6Tkf4TJCMSuYhQzkPGqG7jb5OOoV3tmwywYEKEekOkpbLw9GnWpXUquvqTFCRIb0WTLY3BS4OBniS7Gw5TaesEDMpqhAKUrQjOfXMvtErCLs1cki8IkrklmoliEMcdGDEOEQ"
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        # print(msg, user_id)
        random_id = random.randint(1, 10000000)
        if msg == "курс":
            response = f'{getCourse("R01235")}, рублей за 1 доллар, {getCourse("R01239")}, за 1 евро, ' \
                       f'{getCourse("R01035")}, рублей за 1 фунт'
        elif msg.startswith("вики"):
            article = msg[4:]
            response=get_wiki_article(article)
        else:
            response="Неизвестная команда"
        vk.messages.send(user_id=user_id, random_id=random_id, message=response[0:4096])

