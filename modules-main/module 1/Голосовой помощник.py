# import os
# import time
#
# from gtts import gTTS
# from pygame import mixer
# ff = open('ff.txt', 'r', encoding='utf-8')
# text = ff.read()
# ff.close()
#
# mixer.init()
# tts = gTTS(text=text, lang='ru')
# tts.save('la.mp3')
# mixer.music.load('la.mp3')
# mixer.music.play()
# while mixer.music.get_busy():
#     time.sleep(1)
# mixer.music.unload()
import pyaudio
import speech_recognition as sr
import random

recognize = sr.Recognizer()
hi = ["Приветствую!", "Доброго времени суток!", "Здравствуйте!", "Приветики!", "Рад Вас слышать :)", "Салют!", "Привет-привет!"]

while True:
    with sr.Microphone() as source:
        print('Скажи что-нибудь...')
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
    speech = recognize.recognize_google(audio, language='ru_RU').lower()
    print('Вы сказали:', speech)
    if speech == 'привет':
        print(random.choice(hi))
    if speech == 'фильм':
        print(random.choice())
    if speech == 'пока':
        print('До свидания')
        break


