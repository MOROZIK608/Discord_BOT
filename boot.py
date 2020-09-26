import discord
from discord.ext import commands
from discord.utils import get
import time
import random
import sqlite3
import pyttsx3
import re




client = commands.Bot(command_prefix = '.')



# Words
hello_word = ['hello', 'hi', 'привет', 'privet', 'ky', 'qq', 'ку']
hellp = ['help', '/help', 'помощь', 'команды']
mats = ['блядь', 'еблан', 'сука', 'ебанутый', 'заебал', 'отьебись', 'шлюха', 'хуесос', 'уебу', 'уёба', 'бля', 'у сука', 'иди нахуй', 'хуй', 'хуйня', 'блять', 'нахуй', 'блядина']
stikers = ['🖕']
osk_bots = ['бот тупой', 'бот ебанутый', 'тупой бот','ебанутый бот','ёбнутый бот','бот ёбнутый', 'бот ебанулся', 'бот еблан']
osk = ['тупой', 'дебил', 'тупарылый', 'дебилойд', 'мразь', 'еблан', 'ты тупой', 'ты дебил', 'ты тупарылый', 'ты дебилойд', 'ты мразь', 'ты еблан']
osk_rod = ['мать в канаве', 'мать жива?', 'мать жива??', 'мать жива???', 'мать жива еблан?', 'мать жива еблан??', 'мать жива еблан???', 'мать жива????', 'мать жива ?', 'мать жива ??', 'мать жива ???', 'мать жива ????', 'твоя мать шлюха', 'твая мать шлюха', 'мать шлюха', 'твоя мать в канаве', 'сын шлюхи', 'сын мрази', 'ты сын шлюхи', 'мамку ебал', 'я твою мамку ебал',
'я тваю мамку ебал', 'я твою мать ебал', 'я тваю мать ебал', 'твоя мама самя тупая', 'твая мама самая тупая']

# Connected
print('BOT connected')




# Создание БД
connection = sqlite3.connect('bot.db')
cursor = connection.cursor()

@client.event
async def on_redy():
	cursor.execute("""CREATE TABLE IF NOT EXISTS users (
			name TEXT,
			id INT,
			cash BIGINT,
			rep INT
		)""")

# Выдача роли
async def on_member_join(member):
	channel = client.get_channel( 736326838367944729 )

	role = discord.utils.get(member.guild.roles, id = 736327233261535372 )

	await member.add_roles(role)
	await channel.send(f'Ты как здесь окозался? ``{ member.name }``',
	 color = 0x0c0c0c )


# Clear message
@client.command(pass_context = True)

async def clear(ctx, amount = 100):
	await ctx.channel.purge(limit = amount)

@client.command()
async def send_a(ctx):
	await ctx.author.send('Привет!!')

@client.command()
async def send(ctx, member: discord.Member):
	while True:
		rand = random.randint(1,3)
		if rand == 1:
			time.sleep(0.900)
			await member.send(f'{member.mention}, ебать ты уёбище лысое')

		elif rand == 2:
			time.sleep(0.900)
			await member.send(f'{member.mention}, лошара ты ебаная подохни!')

		else:
			time.sleep(0.900)
			await member.send(f'{member.mention}, Мда... Ебать ты чмо.......')










####################################################
@client.event
# Команды
async def on_message(message):
	await client.process_commands( message )
	msg = message.content.lower()

# создание переменых
	global rand
	rand = random.randint(1,4)
	rand2 = random.randint(1,100)
	rand_balance = random.randint(1,2)
	rrand = 3
	number = random.randint(1,2)
	balace = 230

# Команды

	if msg in hello_word:
		await message.channel.send('И тебе привет!')


	elif msg in mats:
		await message.delete()
		author = message.author
		print(f'[log] { author }: заматерился')
		await message.author.send(f' {author.mention} 😡 Лучше такое не пиши а то будет бан !😡')

	elif msg in stikers:
		await message.channel.send('😡  Это плохой смайлик!!! 😡 ')

	elif msg in osk_rod:
		await message.delete()
		author = message.author
		print(f'[log] { author }:   Оскорбил родных')
		await message.author.send(f' {author.mention} 😡 Ебать ты такой далбаёб нахуя ты родных оскорбляешь?? еблан ты жирный блядь!!! 😡')

	elif msg in hellp:
		author = message.author
		print(f'[log] { author }:   написал команду /help ')
		await message.channel.send(f' {author.mention} СОЗДАТЕЛЬ БОТА MOROZIK\n🎉 Развлекательные: \n🕗 1) Время 🕗\n😎 2) Кубик 😎 \n👹 3) Шутка 👹\n💰 4) Баланс 💰 \n🤞 5) Удача 🤞\n🎋 6) Очистка 🎋')

	elif msg == 'время':
		author = message.author
		print(f'[log] { author }: запросил время')
		await message.channel.send(f' {author.mention} Сейчас: '+ time.strftime("%X"))

	elif msg == 'кубик':
		author = message.author
		print(f'[log] { author }:  кинул кубик')
		await message.channel.send('Выпало число: ' + str(rand2) )

	elif msg == 'кто гей?':
		await message.channel.send('Кот гей, отвечаю!!!')

	elif msg == 'шутка':
		if rand == 1:
			await message.channel.send('😑 Буратино утанул -___- 😑')

		elif rand == 2:
			await message.channel.send('😑 Калобок повесился -___- 😑')

		elif rand == 3:
			await message.channel.send('😑 У кота 100 жизней 😑')

	elif msg == 'казино':
		await message.channel.send('Временно не доступно!')


	elif 'баланс' == msg:
		await message.channel.send('Вашь баланс состваляет: ' + str(balace))

	elif msg == 'удача':
		if number == 1:
			await message.channel.send('Вам повезло!👍')
		else:
			await message.channel.send('Вам не повезло :(( 😐')

	elif msg == 'балансс':
		await message.channel.send(str(balace))

	elif msg == 'уч':
		balace += 20



	elif msg in osk_bots:
		await message.delete()
		await message.author.send(f' {author.mention} 😡 Лучше такое не пиши а то будет бан !😡')

	elif msg in osk:
		await message.delete()
		await message.author.send(f' {author.mention} 😡 Лучше такое не пиши а то будет бан !😡')


	elif msg == 'кик':
		name = await message.channel.send('Введите ".kick (имя)"')

	elif msg == 'очистка':
		author = message.author
		await message.channel.purge(limit = 1000)
		print(f'[log] { author }:   Очистил чат')




	elif msg == 'погода':
		await message.channel.send('Временно не доступно! 😢')

	elif msg == 'спам':
		await message.channel.send('Пропиши .send @name')






	else:
		author = message.author
		print(f'[log] {author}  что то написал');
		





		


# Connect
token = open( 'token.txt', 'r' ).readline()

client.run(token)