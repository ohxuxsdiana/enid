from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start'])
async def send_welcome (message):
    await bot.reply_to(message,'Привет! Я твой супермега крутой помощник по игре на гитаре!/nЯ буду оказывать тебе помощь с нахождением аккордов, уроков и табулатуры по интересующим тебя песням! Мои команды:/n1)/start/n2)/terminalogia/n3)/easy songs')

@bot.message_handler(commands=['terminalogia'])
async def send_welcome(message):
    await bot.reply_to(message, 'Табулатура (или tabulature, сокращенно табуляция) - это форма музыкальной записи, указывающая на аппликатуру инструмента или расположение исполняемых нот, а не на музыкальные высоты./nАкко́рд (фр. accord, итал. accordo, от позднелат. accordo — согласовываю) — одновременное сочетание трёх и более музыкальных звуков разной высоты (точнее, разных высотных классов), воспринимаемое слухом как целостный элемент звуковысотной вертикали./nГnитарный бой — самый известный приём игры на гитаре. Заключается в ударном звукоизвлечении (отсюда и название), резким, но скользящим ударом — по отдельным, рядом расположенным, струнам, либо по всем сразу./nКапода́стр (итал. capo — головка, верх; и tasto — лад; дословно: верхний порожек) — зажим, использующийся в струнно-щипковых инструментах (гитара, балалайка, мандолина), для высотной транспозиции путём искусственного укорачивания звучащей части струн. ')


@bot.message_handler(commands=['bloggers'])
async def send_welcome (message):
    await bot.reply_to(message,'Топ 3 лучших блогеров на youtube обущающих игрой на гитаре:/n1) Ярик Бро/n2) Гитарная Революция/n3) MusicWorker')

@bot.message_handler(commands=['Light tablature'])
async def send_welcome(message):
    await bot.reply_to(message, 'Топ 10 легких табов/n1) Гарии поттер/n2) Кузнечик/n3) Saw Theme(пила)/n4) Lumen - Гореть/n5) Жуки - Батарейка/n6) Белая ночь - В. Салтыков/n7) Seven nation army/n8) Крёстный отец/n9) Ведьмаку заплатите чеканной монетой/n10) Мальчик на девятке/n11) Звери - Районы кварталы')



@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

import asyncio
asyncio.run(bot.polling())