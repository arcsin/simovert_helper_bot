from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


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
	if msg.text == "F001":
		name = "Сигал обратной связи главного контактора"
		cause = "Еслинастроенсигналобратнойсвязиглавногоконтактораипослесигналавключенияпитания, втечениевремени, установленноговР600, оннеприсходит. Вслучаесинхронныхдвигателейсвнешнимвозбуждением(P095 = 12), отсутствуетконтрольныйсигналдлямодулятокавозбуждения."
		counter_measure = "P591 Сообщениеконтактора. Значениепараметрадолжносоответствоватьподключениюобратнойсвязиглавногоконтактора. Проверьтецепьобратнойсвязиглавногоконтактора  (илиобратнуюсвязьмодулятокавозбуждениявслучаесинхронныхдвигателей)."
		answer = "**" + name + "**" + "\n" + cause + "\n\n" + counter_measure
	else:
		answer = "информации пока нет"
	await bot.send_message(msg.from_user.id, answer)


if __name__ == '__main__':
	executor.start_polling(dp)
