from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sqlite3

import re

from config import TOKEN

database_name = 'simovert_compendium.db'
home_dir = "/home/pi/simovert_helper_bot/"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
	await message.reply("Hello!\n I can explain Faults and Alarms of Simovert")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
	await message.reply("I can explain Faults and Alarms of Simovert")


@dp.message_handler()
async def message(msg: types.Message):
	request = msg.text.strip()
	request = request.upper()
	print ("request after strip and upper=" + request)	
	if request.startswith('FF'): type_message = "FF"
	elif request.startswith('F'): type_message = "F"
	elif request.startswith('A'): type_message = "A"
	else: return 
	Number = int(re.sub("\D", "", request))
	print ("Number=" + str(Number))
	SQL = "SELECT Name, Cause, Counter_measure FROM main WHERE (Type = '{0}' AND Number = {1} AND Language = '{2}')".format(type_message, Number, 'ru')
	cur.execute(SQL)
	rows = cur.fetchone()
	print (rows)
	if not rows: return
	name = rows[0]
	cause = rows[1]
	counter_measure = rows[2]
		
	answer = "*" + name + "*" + "\n" + "*Причина:*" + cause 
	if counter_measure is not None : answer = answer + "\n" +  "*Способ устранения:*" + counter_measure
	print ("answer=" + answer)	
	
	
	await bot.send_message(msg.from_user.id, answer, parse_mode= "Markdown")


if __name__ == '__main__':
	#Connect to database
	con = sqlite3.connect(home_dir + database_name)
	cur = con.cursor()
	
	executor.start_polling(dp)
	
	#Database connection close
	con.close()
	
