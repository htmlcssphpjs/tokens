#!/usr/bin/python3
# -*- coding: utf-8 -*-
# t0ken v1.0
# Author: vsecoder feet troci
import random
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

while True:
	one = "1234567890"
	two = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_-"

	x = ''
	y = ''

	for i in range(9):
		x = x + random.choice(one)

	for i in range(33):
		y = y + random.choice(two)

	token = '1' + x + ':AA' + y

	try:
		print('... ' + token)
		bot = Bot(token=token)
		dp = Dispatcher(bot)
		@dp.message_handler(commands=['start'])
		async def send_welcome(message: types.Message):
			await bot.send_message(message.chat.id, '🙋Здравствуйте')
		executor.start_polling(dp)
		f = open('text.txt', 'a')
		f.write(token + '\n')
		f.close()
	except Exception as e:
		print('- ' + token + ' ' + str(e))
