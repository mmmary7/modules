import vk_api
from modules import course

token = "vk1.a.Q0iEQkCP5ZedgRQkSrKwNI4tILjXp3QHcEioS3u-yHfLQrmaEmZcxBV7lZWX-NMsJbUhyQGNN2wRkQtIc_6Tkf4TJCMSuYhQzkPGqG7jb5OOoV3tmwywYEKEekOkpbLw9GnWpXUquvqTFCRIb0WTLY3BS4OBniS7Gw5TaesEDMpqhAKUrQjOfXMvtErCLs1cki8IkrklmoliEMcdGDEOEQ"
vk = vk_api.VkApi(token="vk1.a.Q0iEQkCP5ZedgRQkSrKwNI4tILjXp3QHcEioS3u-yHfLQrmaEmZcxBV7lZWX-NMsJbUhyQGNN2wRkQtIc_6Tkf4TJCMSuYhQzkPGqG7jb5OOoV3tmwywYEKEekOkpbLw9GnWpXUquvqTFCRIb0WTLY3BS4OBniS7Gw5TaesEDMpqhAKUrQjOfXMvtErCLs1cki8IkrklmoliEMcdGDEOEQ")
vk._auth_token()

while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    #print(messages)
    if messages['count'] >= 1:
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        messages_text = messages['items'][0]['last_message']['text']
        if messages_text.lower() == "курс":
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': course.getCourse("R01235")})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Неизвестная команда'})

        #print(user_id, message_id, messages_text)

        vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Какое-то сообщение'})