from utils.imports import *
from utils.func import *
from utils.texts import *

app = Client
client = app

user_data = {}
auto_data = {}

class bulling:
	def __init__(self):
		self.id = []

class auto:
	def __init__(self):
		self.id = []
		self.name = 'none'

def get_bulling(user_id):
    if user_id not in user_data:
        user_data[user_id] = bulling()
    return user_data[user_id]

def delete_bulling(user_id):
    if user_id in user_data:
        del user_data[user_id]

def get_auto(user_id):
    if user_id not in auto_data:
        auto_data[user_id] = auto()
    return auto_data[user_id]

def delete_auto(user_id):
    if user_id in auto_data:
        del auto_data[user_id]

@app.on_message(filters.command('reactspam', prefixes=prefix) & filters.me)
async def reactspam(client, message):
    try:
    	amount = int(message.command[1])
    	reaction = " ".join(message.command[2:])
    except:
    	return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Не верно введены аргументы!</b>')
    await message.edit(f"<emoji id=5461010063135088912>👍</emoji> <b>Спам запущен...</b>")
    
    if reaction == '':
    	reaction = '👍'
    else:
    	pass
    
    try:
    	r = message.reply_to_message.id
    except:
    	r = message.id
    for i in range(amount):
        if reaction in emojis:
            try:
                await client.send_reaction(message.chat.id, r - i, reaction)
            except Exception as e:
                return await message.edit(f'<emoji id=5237993272109967450>❌</emoji> <b>Ошибка: {e}</b>')
        else:
            return await message.edit(f"<emoji id=5237993272109967450>❌</emoji> <b>Вы не можете использовать этот эмодзи!</b>")
    await message.edit(f"<emoji id=5237907553152672597>✅</emoji> <b>Спам завершен</b>")
    await asyncio.sleep(3)
    await client.delete_messages(message.chat.id, message.id)

@app.on_message(filters.command('update', prefixes=prefix))
async def update(client, message):
	await message.edit_text('<emoji id=5373310679241466020>🌀</emoji> <b>Проверка обновлений...</b>')
	try:
		subprocess.run("rm -rf version.txt", shell=True, capture_output=True)
		subprocess.run("wget https://raw.githubusercontent.com/shashachkaaa/XiocaUserBot/refs/heads/main/version.txt", shell=True, capture_output=True)
		with open("version.txt", "r") as file:
			v = file.readline().strip()
			v = v.replace('v = ', '')
	except:
		await message.edit_text('<emoji id=5373310679241466020>🌀</emoji> <b>Установка пакетов...</b>')
		subprocess.run("pkg install wget", shell=True, capture_output=True)
		await message.edit_text('<emoji id=5373310679241466020>🌀</emoji> <b>Проверка обновлений...</b>')
		subprocess.run("rm -rf version.txt", shell=True, capture_output=True)
		subprocess.run("wget https://raw.githubusercontent.com/shashachkaaa/XiocaUserBot/refs/heads/main/version.txt", shell=True, capture_output=True)
	ver = cursor.execute(f'SELECT version from settings').fetchone()[0]
	with open("version.txt", "r") as file:
			ve = file.readline().strip()
			v = ve.replace('v = ', '')
	if ver == v:
		return await message.edit_text('<emoji id=5260463209562776385>✅</emoji> <b>Обновления не найдены.</b>')
	else:
		await message.edit_text('<emoji id=5373310679241466020>🌀</emoji> <b>Устанавливаю обновление...</b>')
		cursor.execute(f'UPDATE settings SET version = "{v}"')
		connect.commit()
		subprocess.run("rm -rf bull_text.py requirements.txt main.py utils commands.py", shell=True, capture_output=True)
		subprocess.run("wget https://raw.githubusercontent.com/shashachkaaa/XiocaUserBot/refs/heads/main/requirements.txt", shell=True, capture_output=True)
		subprocess.run("wget https://raw.githubusercontent.com/shashachkaaa/XiocaUserBot/refs/heads/main/main.py", shell=True, capture_output=True)
		subprocess.run("wget https://raw.githubusercontent.com/shashachkaaa/XiocaUserBot/refs/heads/main/commands.py", shell=True, capture_output=True)
		try:
			subprocess.run("git clone https://github.com/shashachkaaa/XiocaUserBot", shell=True, capture_output=True)
			os.rename("XiocaUserBot", "Xioca")
			shutil.move('Xioca/utils', 'XiocaUserBot')
			os.rename("XiocaUserBot", "utils")
			subprocess.run("rm -rf Xioca", shell=True, capture_output=True)
			pip.main(['install', '-r', 'requirements.txt'])
		except Exception as e:
			print(e)
			return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Ошибка: {e}</b>')
		await message.edit_text('<emoji id=5260463209562776385>✅</emoji> <b>Обновления установлены. Через 5 секунд юзербот перезапустится для завершения обновления...</b>')
		await asyncio.sleep(5)
		await message.edit_text('<emoji id=5258420634785947640>🔄</emoji> <b>Перезагружаюсь...</b>')
		await asyncio.sleep(2)
		await client.delete_messages(message.chat.id, message.id)
		restart()
#		if m:
#			cursor.execute(f'UPDATE settings SET last_time = "{time.time()}"')
#			connect.commit()
#			restart()
#			ti = cursor.execute(f'SELECT last_time from settings').fetchone()[0]
#			end_time = ti - start_time
#			hours, rem = divmod(end_time, 3600)
#			minutes, seconds = divmod(rem, 60)
#			await m.edit_text(f'<emoji id=5260463209562776385>✅</emoji> <b>Юзербот успешно перезагружен за {int(seconds):02d} секунд!</b>')

@app.on_message(filters.command('addbull', prefixes=prefix))
async def addbull(client, message):
	try:
		user_id = message.reply_to_message.from_user.id
	except:
		return await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Команда должна быть ответом на сообщение!</b>')
	
	bd = get_bulling(user_id)
	ids = bd.id
	if user_id in ids:
		return await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Этот пользователь уже находится в списке терпил!</b>')
	else:
		me = await client.get_me()
		me_id = me.id
		if me_id == user_id:
			await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Нельзя вписать себя в терпил!</b>')
		else:
			await message.edit_text('<emoji id=5337223500732063858>🤨</emoji> <b>Дай номер своей мамаши, бездарь...</b>')
			bd.id.append(user_id)

@app.on_message(filters.command('rmbull', prefixes=prefix))
async def rmbull(client, message):
	try:
		user_id = message.reply_to_message.from_user.id
	except:
		return await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Команда должна быть ответом на сообщение!</b>')

	bd = get_bulling(user_id)
	ids = bd.id
	if user_id in ids:
		delete_bulling(user_id)
		return await message.edit_text('<emoji id=5339375313707095535>😶‍🌫️</emoji> <b>Пользователь удален из списка терпил</b>')
	else:
		await message.edit_text('<emoji id=5337223500732063858>🤨</emoji> <b>Пользователь не находится в списке терпил</b>')
	
@app.on_message(filters.command('info', prefixes=prefix))
async def info(client, message):
	m = await message.edit_text('<emoji id=5372905603695910757>🌙</emoji> <b>Загружаю инфо...</b>')
	try:
		cpu = f'{psutil.cpu_percent()}%'
	except:
		cpu = 'Неизвестно'
	try:
		ram = psutil.virtual_memory().used / (1024 * 1024)
		ram = f'{ram:.2f}'
	except:
		ram = 'Неизвестно'
	me = await client.get_me()
	name = me.first_name
	end_time = time.time() - start_time
	hours, rem = divmod(end_time, 3600)
	minutes, seconds = divmod(rem, 60)
	
	if system == "Windows":
		platform_name = "<emoji id=5316891065423241127>🖥</emoji> Windows"
	elif system == "Linux":
	       if "termux" in sys.argv[0]:
	       	platform_name = "<emoji id=5407025283456835913>📱</emoji> Termux"
	       elif "p3droid" in sys.argv[0]:
	       	platform_name = "<emoji id=5407025283456835913>📱</emoji> Pydroid3"
	       else:
	       	platform_name = "<emoji id=5361541227604878624>🐧</emoji> Linux"
	elif system == "Darwin":
	 	platform_name = "<emoji id=5431376038628171216>💻</emoji> MacOS"
	elif system == "FreeBSD":
		platform_name = "<emoji id=5431376038628171216>💻</emoji> FreeBSD"
	else:
		platform_name = "<emoji id=5330115548900501467>🔑</emoji> Unknown"

	try:
		subprocess.run("rm -rf version.txt", shell=True, capture_output=True)
		subprocess.run("wget https://raw.githubusercontent.com/shashachkaaa/XiocaUserBot/refs/heads/main/version.txt", shell=True, capture_output=True)
	except:
		await message.edit_text('<emoji id=5373310679241466020>🌀</emoji> <b>Установка пакетов...</b>')
		subprocess.run("pkg install wget", shell=True, capture_output=True)
		subprocess.run("rm -rf version.txt", shell=True, capture_output=True)
		subprocess.run("wget https://raw.githubusercontent.com/shashachkaaa/XiocaUserBot/refs/heads/main/version.txt", shell=True, capture_output=True)
	ver = cursor.execute(f'SELECT version from settings').fetchone()[0]
	with open("version.txt", "r") as file:
			v = file.readline().strip()
			v = v.replace('v = ', '')
	vv = ver.replace("'", '')
	if ver == v:
		tv = f'<emoji id=5469741319330996757>💫</emoji> Версия: {vv} актуальная'
	else:
		tv = f'<emoji id=5237993272109967450>❌</emoji> Версия: {vv} устаревшая. Введите <code>{prefix}update</code> для обновления.'
	
	await client.send_animation(message.chat.id, animation="xioca.mp4", caption=f'''
<emoji id=5372905603695910757>🌙</emoji> <b>Xioca

<emoji id=5373141891321699086>😎</emoji> Владелец: {name}
{tv}

<emoji id=5472111548572900003>⌨️</emoji> Префикс: «{prefix}»
<emoji id=5451646226975955576>⌛️</emoji> Аптайм: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}

<emoji id=5258203794772085854>⚡️</emoji> Использование CPU: <i>~{cpu}</i>
<emoji id=5359785904535774578>💼</emoji> Использование RAM: <i>~{ram} MB</i>

{platform_name}</b>''')
	await client.delete_messages(message.chat.id, m.id)

@app.on_message(filters.command('serverinfo', prefixes=prefix))
async def serverinfo(client, message):
	try:
		cpu_count = psutil.cpu_count()
		cpu_freq = psutil.cpu_freq()
		cpu_percent = psutil.cpu_percent()
	
		memory_total = psutil.virtual_memory().total
		memory_available = psutil.virtual_memory().available
	
		disk_usage = psutil.disk_usage('/')
	
		net_io_counters = psutil.net_io_counters()
	except Exception as e:
		return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Ошибка: {e}</b>')
	
	await message.edit_text(f'''
	<emoji id=5431376038628171216>💻</emoji> Информация о сервере:
	
	🎛 Количество ядер процессора: {cpu_count}
	<emoji id=5373001317042101552>📈</emoji> Частота процессора: {cpu_freq.current:.2f} ГГц
	<emoji id=5431577498364158238>📊</emoji> Загрузка процессора: {cpu_percent}%
	💽 Всего памяти: {memory_total / (10243):.2f} ГБ
	💿 Доступно памяти: {memory_available / (10243):.2f} ГБ
	📀 Использование диска: {disk_usage.percent}%
	
	📡 Сетевой ввод/вывод:
		⬅ Входящий трафик: {net_io_counters.bytes_recv / (10243):.2f} ГБ
		➡ Исходящий трафик: {net_io_counters.bytes_sent / (10243):.2f} ГБ''')

@app.on_message(filters.command('weather', prefixes=prefix))
async def weather(client, message):
	qu = " ".join(message.text.split()[1:])
	if qu == '':
		return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Не верно введены аргументы!</b>')
	key = '18f76e3ac0c48dee34905f0c9e2e51d1'
	ed = 'metric'
	lang = 'ru'
	format = 'json'
	url = f"https://api.openweathermap.org/data/2.5/weather?q={qu}&units={ed}&lang={lang}&appid={key}"
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		return await message.edit_text(f'''
		<emoji id=5431783411981228752>🎆</emoji> Город: {data['name']}
		<emoji id=5415803062738504079>😀</emoji> Страна: {data['sys']['country']}
		<emoji id=5470049770997292425>😀</emoji> Температура: {data['main']['temp']} °C
		<emoji id=5370724846936267183>🤔</emoji> Ощущается как: {data['main']['feels_like']} °C
		<emoji id=5370547013815376328>😶‍🌫️</emoji> Влажность: {data['main']['humidity']}%
		<emoji id=5399898266265475100>🌍</emoji> Давление: {data['main']['pressure']} гПа
		💨 Ветер: {data['wind']['speed']} м/с
		<emoji id=5283097055852503586>🌦</emoji> Погода: {data['weather'][0]['description']}''')
	else:
		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Ошибка при получении погоды: {response.status_code}</b>')

@app.on_message(filters.command('setprefix', prefixes=prefix))
async def setprefix(client, message):
	qu = " ".join(message.text.split()[1:])
	if len(qu) >= 2:
		return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Префикс не может быть больше 1 символа!</b>')
	
	await message.edit_text(f'<emoji id=5237907553152672597>✅</emoji> <b>Префикс "{qu}" успешно установлен!</b>')
	await asyncio.sleep(1)
	await message.edit_text(f'<emoji id=5258420634785947640>🔄</emoji> <code>Перезапускаюсь для установки префикса...</code>')
	cursor.execute(f'UPDATE settings SET prefix = "{qu}"')
	connect.commit()
	await asyncio.sleep(2)
	await client.delete_messages(message.chat.id, message.id)
	restart()

@app.on_message(filters.command('gpt', prefixes=prefix) & filters.me)
async def gpt(client, message):
	qu = " ".join(message.text.split()[1:])
	if qu == '':
		try:
			qu = message.reply_to_message.text
		except:
			return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Запрос не может быть пустым!</b>')
	
	await message.edit_text(f'<emoji id=5253647886738007937>🤖</emoji> <b>ChatGPT генерирует ответ, ожидайте...</b>')
	try:
		response = resp(qu)
	except Exception as e:
		return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Ошибка: {e}</b>')
	
	try:
		await message.edit_text(f"<emoji id=5397924488274783318>❓</emoji> <b>Ваш вопрос: {qu}\n<emoji id=5253647886738007937>🤖</emoji> Ответ ChatGPT:</b>\n{htm(response)}")
	except Exception as e:
		return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Ошибка: {e}</b>')

@app.on_message(filters.command('lj', prefixes=prefix))
async def lj(client, message):
	chat_id = message.chat.id
	await client.delete_messages(chat_id, message.id)
	await app.leave_chat(chat_id)
	await app.join_chat(chat_id)

@app.on_message(filters.command('translit', prefixes=prefix))
async def translit(client, message):
	text = " ".join(message.text.split()[1:])
	if text == '':
		return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Текст не может быть пустым!</b>')
	
	await message.edit_text(ui(text))

@app.on_message(filters.command('report', prefixes=prefix))
async def report(client, message):
	r = message.reply_to_message.from_user
	try:
		spam = int(message.text.split()[1])
		if spam <= 0:
			return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Кол-во репортов не может быть отрицательным!</b>')
	except Exception as e:
		return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Не верно введены аргументы!</b>')
		
	if r:
		us = r.username
		peer = await app.resolve_peer(f"@{us}")
		peer_id = peer.user_id
		access_hash = peer.access_hash
		
		channel = InputPeerChannel(channel_id=peer_id, access_hash=access_hash)
		reason  = get_report_reason("Report for child abuse.")
		report_peer = ReportPeer(peer=channel, reason=reason, message="spam")
		await message.edit_text(f'<b>Жалуюсь...</b>')
		num = 0
		l = []
		for i in range(0, spam):
			try:
				num += 1
				report = await app.send(report_peer)
			except Exception as e:
				l.append(e)
		try:
			lis = '\n'.join(l)
		except:
			lis = 'нет'
		await message.edit_text(f'<emoji id=5237907553152672597>✅</emoji> <b>Отправлено {num} жалоб!</b>')
	else:
		await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Команда должна быть ответом на сообщение!</b>')

@app.on_message(filters.command('id', prefixes=prefix))
async def id(client, message):
	r = message.reply_to_message
	cid = message.chat.id
	
	if r:
		id = message.reply_to_message.from_user.id
		name = message.reply_to_message.from_user.first_name
		await message.edit_text(f'<emoji id=5472146462362048818>💡</emoji> <b>ID {name}: <code>{id}</code>\n<emoji id=5818885490065017876>🆔</emoji> Chat ID: {cid}</b>')
	else:
		await message.edit_text(f'<emoji id=5818885490065017876>🆔</emoji> <b>Chat ID: {cid}</b>')

@app.on_message(filters.command('dels', prefixes=prefix))
async def dels(client, message):
	t = str(message.text.split()[1])
	ty = t.replace(f'{prefix}dels', '')
	type = ty.replace(f'{prefix}dels ', '')
	
	if type == 'on':
		await message.edit_text(f'<emoji id=5339536521009571338>👋</emoji> <b>Теперь удаленные сообщения сохраняются!</b>')
		cursor.execute(f'UPDATE settings SET dels = "on"')
		connect.commit()
		chat_id = cursor.execute(f'SELECT dels_chat FROM settings').fetchone()
		chat_id = int(chat_id[0])
		try:
			await app.send_message(chat_id, f'<emoji id=5237907553152672597>✅</emoji> <b>Сюда будут пересылатся удаленные сообщения с ЛС!</b>')
		except:
			c = await app.create_supergroup('deleted messages')
			chat_id = c.id
			cursor.execute(f'UPDATE settings SET dels_chat = {chat_id}')
			connect.commit()
			await app.send_message(chat_id, f'<emoji id=5237907553152672597>✅</emoji> <b>Сюда будут пересылатся удаленные сообщения с ЛС!</b>')
	elif type == 'off':
		await message.edit_text(f'<emoji id=5472100935708711380>👍</emoji> <b>Теперь удаленные сообщения не сохраняются!</b>')
		cursor.execute(f'UPDATE settings SET dels = "off"')
		connect.commit()
	else:
		await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Не верно введены аргументы!</b>')

@app.on_deleted_messages()
async def checkdels(client, message):
	dels = cursor.execute(f'SELECT dels from settings').fetchone()
	dels = str(dels[0])
	
	if dels == 'on':
		try:
			message_id = message[0].id
			print(message_id)
			user_id = cursor.execute(f'SELECT user_id from messages WHERE message_id = {message_id}').fetchone()
			message_text = cursor.execute(f'SELECT message_text FROM messages WHERE message_id = {message_id}').fetchone()
			dels_chat = cursor.execute(f'SELECT dels_chat from settings').fetchone()
			dels_chat = int(dels_chat[0])

			user_id = int(user_id[0])
			message_text = str(message_text[0])
			
			user = await app.get_users(user_id)
			first_name = user.first_name
			username = user.username
			await app.send_message(dels_chat, f'''<emoji id=5339536521009571338>👋</emoji> {first_name} (@{username} | <code>{user_id}</code>) удалил сообщение в ЛС!
<emoji id=5417875345804108985>🌍</emoji> Текст » <i>{message_text}</i>
''')
		except Exception as e:
			print(e)
			return
	else:
		return
	
@app.on_message(filters.mentioned)
async def checktags(client, message):
	chat_id = cursor.execute(f'SELECT tags_chat FROM settings').fetchone()
	tags = cursor.execute(f'SELECT tags FROM settings').fetchone()
	
	tags = str(tags[0])
	chat_id = int(chat_id[0])
	
	if tags == 'on':
		await app.send_message(chat_id, f'''<emoji id=5242628160297641831>🔔</emoji> <b>Вас тегнули в чате</b> «<code>{message.chat.title}</code>» (@{message.chat.username})
<emoji id=5325770433566359627>😲</emoji> Пользователь » {message.from_user.first_name} (@{message.from_user.username})
<emoji id=5465204283383224325>💬</emoji> Ссылка » {message.link}
<emoji id=5465300082628763143>💬</emoji> Текст сообщения » <i>{message.text}</i>''', disable_web_page_preview = True)
		await app.read_chat_history(message.chat.id, message.id)
	else:
		return

@app.on_message(filters.command('tags', prefixes=prefix))
async def tags(client, message):
	tag = str(message.text.split()[1])
	ta = tag.replace(f'{prefix}tags', '')
	t = ta.replace(f'{prefix}tags ', '')
	
	if t == 'on':
		await message.edit_text('<emoji id=5472100935708711380>👍</emoji> <b>Теперь вас не будут беспокоить теги!</b>')
		cursor.execute(f'UPDATE settings SET tags = "on"')
		connect.commit()
		try:
			chat_id = cursor.execute(f'SELECT tags_chat FROM settings').fetchone()
			chat_id = int(chat_id[0])
			await app.send_message(chat_id, f'<emoji id=5237907553152672597>✅</emoji> <b>Сюда будут пересылатся теги с чатов!</b>')
		except:
			c = await app.create_supergroup('tags')
			chat_id = c.id
			cursor.execute(f'UPDATE settings SET tags_chat = {chat_id}')
			connect.commit()
			await app.send_message(chat_id, f'<emoji id=5237907553152672597>✅</emoji> <b>Сюда будут пересылатся теги с чатов!</b>')
	elif t == 'off':
		await message.edit_text('<emoji id=5472100935708711380>👍</emoji> <b>Вас снова могут тегать пользователи в чатах!</b>')
		cursor.execute(f'UPDATE settings SET tags = "off"')
		connect.commit()
	else:
		await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Не верно введены аргументы!</b>')

@app.on_message(filters.command('creategroup', prefixes=prefix))
async def creategroup(client, message):
	title = " ".join(message.text.split())
	t = title.replace(f'{prefix}creategroup',  '')
	if t == '':
		await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Название чата не может быть пустым</b>')
		return
	
	if len(t) >= 100:
		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>В названии чата не может быть более 100 символов!</b>')
		return
	
	await message.edit_text(f'<emoji id=5237907553152672597>✅</emoji> <b>Чат «{t}» был успешно создан!</b>')
	await app.create_supergroup(t)

@app.on_message(filters.command('stopautoname', prefixes=prefix))
async def stopautoname(client, message):
#	name = cursor.execute(f'SELECT name from settings').fetchone()
#	name = str(name[0])
	user = await client.get_me()
	user_id = user.id
	bd = get_auto(user_id)
	name = bd.name
	await message.edit_text(f'<emoji id=5237907553152672597>✅</emoji> <b>Время в нике успешно остановлено!</b>')
	n = name.replace(f'{prefix}autoname ', '')
	nm = n.replace("{time}", '')
	try:
		await app.update_profile(first_name=f"{nm}")
	except:
		await app.update_profile(first_name=f'Введите ник')
	delete_auto(user_id)
#	cursor.execute(f'UPDATE settings SET autoname = "off"')
#	connect.commit()
	
@app.on_message(filters.command('autoname', prefixes=prefix))
async def autoname(client, message):
    # Переводим текст команды в строку
    n = " ".join(message.text.split())
    if n == '':
    	return await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Ник не может быть пустым!</b>')
    if '{time}' not in n:
    	return await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>В введенном нике отсутсвует "{time}"</b>')
   
#    type = cursor.execute('SELECT autoname FROM settings').fetchone()[0]
    user = await client.get_me()
    user_id = user.id
    bd = get_auto(user_id)
    ids = bd.id
    if user_id in ids:
    	return await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>У вас уже установлено время в нике!</b>')
    
    # Отправляем сообщение об успешной установке времени в ник
    await message.edit_text(f'<emoji id=5237907553152672597>✅</emoji> <b>Время в ник успешно установлено!</b>')
    bd.id.append(user_id)
    bd.name = n
    
#    cursor.execute(f'UPDATE settings SET name = "{n}"')
#    cursor.execute(f'UPDATE settings SET autoname = "on"')
#    connect.commit()

    # Цикл для обновления ника с интервалом в 60 секунд
    while True:
        # Получаем значение autoname из базы данных
        autoname_status = cursor.execute('SELECT autoname FROM settings').fetchone()[0]
        
        # Проверяем, включен ли autoname
        
        if user_id in ids:
            current_time = get_current_time()
            name = n.replace(f'{prefix}autoname ', '')
            name = name.replace("{time}", current_time)
            # Обновляем профиль с новым именем
            try:
            	await app.update_profile(first_name=f"{name}")
            	await asyncio.sleep(60)
            except:
            	await asyncio.sleep(600)
        else:
            # Если autoname выключен, прерываем цикл
            break

@app.on_message(filters.command('purge', prefixes=prefix))
async def purge(client, message):
    start_message_id = message.id
    end_message_id = message.reply_to_message.id
    chat_id = message.chat.id

    ids = []

    async for message in client.get_chat_history(chat_id):
        if message.id == end_message_id:
            break
        ids.append(message.id)
    ids.append(end_message_id)
    await client.delete_messages(chat_id, ids)

@app.on_message(filters.command('del', prefixes=prefix))
async def dele(client, message):
	try:
		msg = message.reply_to_message.id
	except:
		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Команда должна быть ответом на сообщение!</b>')
		return
	message_id = message.id
	chat_id = message.chat.id
	list = [msg, message_id]
	await client.delete_messages(chat_id, list)

@app.on_message(filters.command('love', prefixes=prefix))
async def love(client, message):
	emoji = ['❤️', '🩷', '🧡', '💛', '💚', '🩵', '💙', '💜', '🖤', '🩶', '🤍', '🤎', '💖', '💝', '💓', '💗', "I", "I ❤️", "I ❤️ U", "I ❤️ U!"]
	for i in emoji:
		await message.edit_text(f'<b>{i}</b>')
		await asyncio.sleep(0.3)

@app.on_message(filters.command('magic', prefixes=prefix))
async def magic(client, message):
			arr = ["❤️", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "💖"]
			h = "🤍"
			first = ""		
			for i in "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4]).split("\n"):
				first += i + "\n"
				await message.edit_text(first)
				await asyncio.sleep(0.2)		
			for i in arr:
				await message.edit_text("".join([h*9, "\n", h*2, i*2, h, i*2, h*2, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h, i*7, h, "\n", h*2, i*5, h*2, "\n", h*3, i*3, h*3, "\n", h*4, i, h*4, "\n", h*9]))
				await asyncio.sleep(0.3)
			for _ in range(8):
				rand = random.choices(arr, k=34)
				await message.edit_text("".join([h*9, "\n", h*2, rand[0], rand[1], h, rand[2], rand[3], h*2, "\n", h, rand[4], rand[5], rand[6], rand[7], rand[8],rand[9],rand[10], h, "\n", h, rand[11], rand[12], rand[13], rand[14], rand[15], rand[16],rand[17], h, "\n", h, rand[18], rand[19], rand[20], rand[21], rand[22], rand[23],rand[24], h, "\n", h*2, rand[25], rand[26], rand[27], rand[28], rand[29], h*2, "\n", h*3, rand[30], rand[31], rand[32], h*3, "\n", h*4, rand[33], h*4, "\n", h*9]))
				await asyncio.sleep(0.3)
			fourth = "".join([h*9, "\n", h*2, arr[0]*2, h, arr[0]*2, h*2, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h, arr[0]*7, h, "\n", h*2, arr[0]*5, h*2, "\n", h*3, arr[0]*3, h*3, "\n", h*4, arr[0], h*4, "\n", h*9])
			await message.edit_text(fourth)
			for _ in range(47):
				fourth = fourth.replace("🤍", "❤️", 1)
				await message.edit_text(fourth)
				await asyncio.sleep(0.1)
			for i in range(8):
				await message.edit_text((arr[0]*(8-i)+"\n")*(8-i))
				await asyncio.sleep(0.4)
			for i in ["I", "I ❤️", "I ❤️ U", "I ❤️ U!"]:
				await message.edit_text(f"<b>{i}</b>")
				await asyncio.sleep(0.5)

@app.on_message(filters.command('voice', prefixes=prefix))
async def voice(client, message):
    voice = message.reply_to_message.voice
    if not voice:
        await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Команда должна быть ответом на голосовое сообщение!</b>')
        return
    await message.edit_text('<emoji id=5260652149469094137>🎙</emoji> <b>Распознаю...</b>')
    file_id = voice.file_id
    try:
        voice_file = await client.download_media(file_id)
        
        converted_file = voice_file.replace('.ogg', '.wav')
        AudioSegment.from_file(voice_file).export(converted_file, format='wav')
        
        recognizer = sr.Recognizer()
        with sr.AudioFile(converted_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language='ru-RU')
        await message.edit_text(f'<emoji id=5237907553152672597>✅</emoji> <b>Голосовое сообщение распознано:</b> <i>{text}</i>')
        os.remove(voice_file)
        os.remove(converted_file)
    except Exception as e:
        await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Не удалось распознать голосовое сообщение:</b> <code>{e}</code>')

@app.on_message(filters.command('tagall', prefixes=prefix))
async def tagall(client, message):
    chat_id = message.chat.id

    num = 0
    await message.edit_text(f'<emoji id=5471930335312747865>💬</emoji> <b>Отмечаю...</b>')
    async for member in app.get_chat_members(chat_id):
        if member.user.username is None:
            pass
        elif member.user.id == message.from_user.id:
        	pass
        elif member.user.is_bot:
        	pass
        else:
            title = " ".join(message.text.split())
            tit = title.replace(f"{prefix}tagall ",  '')
            t = tit.replace(f'{prefix}tagall', '')
            if t == '':
            	tt = f'<b><a href="tg://user?id={member.user.id}">{member.user.first_name}</a></b>'
            else:
            	tt = f'<b><a href="tg://user?id={member.user.id}">{t}</a></b>'
            await app.send_message(chat_id, tt)
            num += 1
    await app.send_message(chat_id, f'<emoji id=5474371208176737086>✉️</emoji> <b>Отмечено {num} участников</b>')

@app.on_message(filters.command(['t', 'terminal'], prefixes=prefix) & filters.me)
async def terminal(client, message):
    code = message.text
    command = code.replace(f"{prefix}terminal ", "").replace(f"{prefix}t ", "")
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        await message.edit_text(f'''<emoji id=5339181821135431228>💻</emoji> <b>Команда:</b>
```bash
{command}```

<emoji id=5375360100196163660>🐲</emoji> <b>Вывод:</b>
```bash
{output.decode()}```
''')
    else:
        await message.edit(f'''<emoji id=5339181821135431228>💻</emoji> <b>Команда:</b>
```bash
{command}```

<emoji id=5237993272109967450>❌</emoji> <b>Ошибка:</b>
```bash
{error.decode()}```''')

@app.on_message(filters.command(['t', 'terminal'], prefixes=prefix) & filters.me)
async def terminal(client, message):
	code = message.text
	command = code.replace(f"{prefix}terminal ", "").replace(f"{prefix}t ", "")
	subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = process.communicate()
	try:
		await message.edit_text(f'''<emoji id=5339181821135431228>💻</emoji> <b>Команда:</b>
```bash
{command}```

<emoji id=5375360100196163660>🐲</emoji> <b>Вывод:</b>
```bash
{output.decode()}```''')
	except:
		await message.edit_text(f'''<emoji id=5339181821135431228>💻</emoji> <b>Команда:</b>
```bash
{command}```

<emoji id=5375360100196163660>🐲</emoji> <b>Вывод:</b>
```bash
{output.decode()}```''')

@app.on_message(filters.command('restart', prefixes=prefix) & filters.me)
async def res(client, message):
    await message.edit_text(f'<emoji id=5258420634785947640>🔄</emoji> <code>Перезапускаюсь...</code>')
    await asyncio.sleep(2)
    await client.delete_messages(message.chat.id, message.id)
    restart()

@app.on_message(filters.command(["eval", 'e'], prefixes=prefix) & filters.me)
async def ev(client, message):
    	code = message.text.strip()
    	code = code.replace(f"{prefix}eval ", "").replace(f"{prefix}e ", "")
    	try:
    	   f = StringIO()
    	   with redirect_stdout(f):
    	   	exec(code)
    	   out = f.getvalue()
    	   return await message.edit_text(f'''<emoji id=5339181821135431228>💻</emoji> <b>Код:</b>
```python
{code}```

<emoji id=5175061663237276437>🐍</emoji> <b>Вывод:</b>
```python
{str(out).replace(">", "").replace("<", "")}```''')
    	except Exception as ex:
    		return await message.edit_text(f'''<emoji id=5339181821135431228>💻</emoji> <b>Код:</b>
```python
{code}```

<emoji id=5237993272109967450>❌</emoji> <b>Ошибка:</b>
```python
{str(ex).replace(">", "").replace("<", "")}```''')
#await message.reply(str(out).replace("<", "").replace(">", ""))
#await message.reply(str(ex).replace(">", "").replace("<", ""))

@app.on_message(filters.command("unpmbl", prefixes=prefix) & filters.me)
async def unpmbl(client, message):
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            name = message.reply_to_message.from_user.first_name
        else:
            id = message.text.split()[1]
            user = await app.get_users(id)
            name = user.first_name
    except Exception as e:
        await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
        return

    if isinstance(id, int):
    	pass
    else:
    	try:
    		i = id.replace("@", '')
    		i = id.replace("https://t.me/", '')
    		id = await get_user_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось разблокировать пользователя в ЛС: {e}')
    		return
    
    await app.unblock_user(id)
    await message.edit_text(f'<emoji id=5472180551517477902>✅</emoji> <b>{name}</b> был убран из ЧС!')

@app.on_message(filters.command("pmbl", prefixes=prefix) & filters.me)
async def pmbl(client, message):
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            name = message.reply_to_message.from_user.first_name
        else:
            id = message.text.split()[1]
            user = await app.get_users(id)
            name = user.first_name
    except Exception as e:
        await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
        return

    if isinstance(id, int):
    	pass
    else:
    	try:
    		i = id.replace("@", '')
    		i = id.replace("https://t.me/", '')
    		id = await get_user_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось заблокировать пользователя в ЛС: {e}')
    		return
    
    await app.block_user(id)
    await message.edit_text(f'<emoji id=5472030751648127392>🛑</emoji> <b>{name}</b> был добавлен(-а) в ЧС!')

@app.on_message(filters.command("unpin", prefixes=prefix) & filters.me)
async def unpin(client, message):
	chat_id = message.chat.id
	if message.reply_to_message:
		message_id = message.reply_to_message.id
		await app.unpin_chat_message(chat_id, message_id)
		await message.edit_text('<emoji id=5258461531464539536>📌</emoji> Сообщение успешно откреплено!')
	else:
		await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Команда должна быть ответом на сообщение!")

@app.on_message(filters.command("pin", prefixes=prefix) & filters.me)
async def pin(client, message):
	chat_id = message.chat.id
	if message.reply_to_message:
		message_id = message.reply_to_message.id
		await app.pin_chat_message(chat_id, message_id)
		await message.edit_text('<emoji id=5258461531464539536>📌</emoji> Сообщение успешно закреплено!')
	else:
		await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Команда должна быть ответом на сообщение!")
	
@app.on_message(filters.command("leave", prefixes=prefix) & filters.me)
async def leave(client, message):
    try:
    	id_chat = message.text.split()[1]
    except:
    	await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> <b>Вы не ввели аргументы!</b>")
    	return

    if isinstance(id_chat, int):
    	pass
    else:
    	try:
    		i = id_chat.replace("@", '')
    		i = id_chat.replace("https://t.me/", '')
    		id = await get_chat_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> <b>Не удалось выйти с чата: {e}</b>')
    		return
    
    await app.leave_chat(id)
    await message.edit_text(f'<emoji id=5474371208176737086>✉️</emoji> <b>Вы вышли с чата {id_chat}!</b>')

@app.on_message(filters.command("join", prefixes=prefix) & filters.me)
async def join(client, message):
    try:
    	id_chat = message.text.split()[1]
    except:
    	await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> <b>Вы не ввели аргументы!</b>")
    	return

    if isinstance(id_chat, int):
    	pass
    else:
    	try:
    		i = id_chat.replace("@", '')
    		i = id_chat.replace("https://t.me/", '')
    		id = await get_chat_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось вступить в чат: {e}')
    		return
    
    await app.join_chat(id)
    await message.edit_text(f'<emoji id=5474371208176737086>✉️</emoji> Вы вступили в чат {id_chat}!')
    
@app.on_message(filters.command('kick', prefixes=prefix))
async def kick(client, message):
    chat_id = message.chat.id
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            name = message.reply_to_message.from_user.first_name
            reason = " ".join(message.text.split()[1:])
        else:
            id = message.text.split()[1]
            user = await app.get_users(id)
            name = user.first_name
            reason = " ".join(message.text.split()[2:])
    except Exception as e:
        await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
        return

    if not reason:
        t = ''
    else:
        t = f'Причина » <i>{reason}</i>'

    if isinstance(id, int):
    	pass
    else:
    	try:
    		i = id.replace("@", '')
    		i = id.replace("https://t.me/", '')
    		id = await get_user_id(pdd)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось кикнуть пользователя: {e}')
    		return
    
    time = 1
    dt = datetime.now() + timedelta(minutes=time)
    full_time_dt = dt.timestamp()
    full_time = datetime.fromtimestamp(full_time_dt)
    
    try:
        await app.ban_chat_member(chat_id, id, until_date=full_time)
        await client.unban_chat_member(chat_id, id)
    except Exception as e:
        await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось кикнуть пользователя: {e}')
        return
    await message.edit_text(f'<emoji id=5472100935708711380>👍</emoji> <b>{name}</b>, кикнут! {t}')

@app.on_message(filters.command("unban", prefixes=prefix) & filters.me)
async def unban(client, message):
    chat_id = message.chat.id
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            name = message.reply_to_message.from_user.first_name
            reason = " ".join(message.text.split()[1:])
        else:
            id = message.text.split()[1]
            user = await app.get_users(id)
            name = user.first_name
            reason = " ".join(message.text.split()[2:])
    except Exception as e:
        await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
        return

    if not reason:
        t = ''
    else:
        t = f'Причина » <i>{reason}</i>'

    if isinstance(id, int):
    	pass
    else:
    	try:
    		i = id.replace("@", '')
    		i = id.replace("https://t.me/", '')
    		id = await get_user_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось разблокировать пользователя: {e}')
    		return
    
    try:
        await client.unban_chat_member(chat_id, id)
    except Exception as e:
        await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось разблокировать пользователя: {e}')
        return
    await message.edit_text(f'<emoji id=5472100935708711380>👍</emoji> <b>{name}</b>, разблокирован! {t}')

@app.on_message(filters.command("ban", prefixes=prefix) & filters.me)
async def ban(client, message):
    chat_id = message.chat.id
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            name = message.reply_to_message.from_user.first_name
            time = int(message.text.split()[1])
            date = message.text.split()[2]
            reason = " ".join(message.text.split()[3:])
        else:
            id = message.text.split()[1]
            user = await app.get_users(id)
            name = user.first_name
            time = int(message.text.split()[2])
            date = message.text.split()[3]
            reason = " ".join(message.text.split()[4:])
    except Exception as e:
        await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
        return

    if not reason:
        t = ''
    else:
        t = f'Причина » <i>{reason}</i>'
    
    if isinstance(id, int):
    	pass
    else:
    	try:
    		i = id.replace("@", '')
    		i = id.replace("https://t.me/", '')
    		id = await get_user_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось заблокировать пользователя: {e}')
    		return
    
    if date in ['м', 'минут', 'минута', 'мин', 'm', 'min', 'minute', 'minutes']:
    	dt = datetime.now() + timedelta(minutes=time)
    	d = 'минут'
    elif date in ['часов', 'час', 'часа', 'h', 'ч' 'hours', 'hour']:
    	dt = datetime.now() + timedelta(hours=time)
    	d = 'часов'
    elif date in ['д', 'дней', 'день', 'дня', 'days', 'day', "d"]:
    	dt = datetime.now() + timedelta(days=time)
    	d = 'дней'
    else:
    	await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Не верно введены аргументы!</b>')
    	return
    	
    full_time_dt = dt.timestamp()
    full_time = datetime.fromtimestamp(full_time_dt)
    try:
        await app.ban_chat_member(chat_id, id, until_date=full_time)
    except Exception as e:
        await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось заблокировать пользователя: {e}')
        return

    await message.edit_text(f'<emoji id=5472267631979405211>🚫</emoji> <b>{name}</b>, заблокирован на <i>{time} {d}</i>. {t}')

@app.on_message(filters.command("unmute", prefixes=prefix) & filters.me)
async def unmute(client, message):
    chat_id = message.chat.id
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            name = message.reply_to_message.from_user.first_name
            reason = " ".join(message.text.split()[1:])
        else:
            id = message.text.split()[1]
            user = await app.get_users(id)
            name = user.first_name
            reason = " ".join(message.text.split()[2:])
    except Exception as e:
        await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
        return

    if not reason:
        t = ''
    else:
        t = f'Причина » <i>{reason}</i>'

    if isinstance(id, int):
    	pass
    else:
    	try:
    		i = id.replace("@", '')
    		i = id.replace("https://t.me/", '')
    		id = await get_user_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось размутить пользователя: {e}')
    		return
    
    try:
        await client.restrict_chat_member(chat_id, id, ChatPermissions(can_send_messages=True))
    except Exception as e:
        await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось размутить пользователя: {e}')
        return

    await message.edit_text(f'<emoji id=5472100935708711380>👍</emoji> <b>{name}</b>, размучен! {t}')

@app.on_message(filters.command("mute", prefixes=prefix) & filters.me)
async def mute(client, message):
    chat_id = message.chat.id
    try:
        if message.reply_to_message:
            id = message.reply_to_message.from_user.id
            name = message.reply_to_message.from_user.first_name
            time = int(message.text.split()[1])
            date = message.text.split()[2]
            reason = " ".join(message.text.split()[3:])
        else:
            id = message.text.split()[1]
            user = await app.get_users(id)
            name = user.first_name
            time = int(message.text.split()[2])
            date = message.text.split()[3]
            reason = " ".join(message.text.split()[4:])
    except Exception as e:
        await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
        return

    if not reason:
        t = ''
    else:
        t = f'Причина » <i>{reason}</i>'
    
    if isinstance(id, int):
    	pass
    else:
    	try:
    		i = id.replace("@", '')
    		i = id.replace("https://t.me/", '')
    		id = await get_user_id(i)
    	except Exception as e:
    		await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось ограничить пользователя: {e}')
    		return
    		
    if date in ['м', 'минут', 'минута', 'мин', 'm', 'min', 'minute', 'minutes']:
    	dt = datetime.now() + timedelta(minutes=time)
    	d = 'минут'
    elif date in ['часов', 'час', 'часа', 'h', 'ч' 'hours', 'hour']:
    	dt = datetime.now() + timedelta(hours=time)
    	d = 'часов'
    elif date in ['д', 'дней', 'день', 'дня', 'days', 'day']:
    	dt = datetime.now() + timedelta(days=time)
    	d = 'дней'
    else:
    	await message.edit_text('<emoji id=5237993272109967450>❌</emoji> <b>Не верно введены аргументы!</b>')
    	return

    full_time_dt = dt.timestamp()
    full_time = datetime.fromtimestamp(full_time_dt)
    try:
        await client.restrict_chat_member(chat_id, id, ChatPermissions(), until_date=full_time)
    except Exception as e:
        await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не удалось ограничить пользователя: {e}')
        return

    await message.edit_text(f'<emoji id=5460662076294831027>🤐</emoji> <b>{name}</b>, замучен на <i>{time} {d}</i>. {t}')

@client.on_message(filters.command("ping", prefixes=prefix))
async def ping(client, message):
	a = time.time()
	m = await message.edit_text(f'<emoji id=5372905603695910757>🌙</emoji>')
	if m:
		b = time.time()
		end_time = time.time() - start_time
		hours, rem = divmod(end_time, 3600)
		minutes, seconds = divmod(rem, 60)
		await m.edit_text(f'<emoji id=5372905603695910757>🌙</emoji> Пинг: <b>{round((b - a) * 1000)}</b> ms\n<emoji id=5431449001532594346>⚡️</emoji> Прошло времени с момента запуска: <b>{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}</b>')

@client.on_message(filters.command("spam", prefixes=prefix))
async def spam(client, message):
	try:
		count = int(message.text.split()[1])
		if not count:
			return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Не верно введены аргументы!')
		if message.reply_to_message:
			text = message.reply_to_message.text
		else:
			text = " ".join(message.text.split()[2:])
			if text == '':
				return await message.edit_text(f'<emoji id=5237993272109967450>❌</emoji> Текст не может быть пустым!')
	except Exception as e:
		await message.edit_text(f"<emoji id=5237993272109967450>❌</emoji> Произошла ошибка: {e}")
		return
	chat_id = message.chat.id
	await message.edit_text(text)
	for i in range(count-1):
		await app.send_message(chat_id, text)
		
@client.on_message(filters.command("help", prefixes=prefix))
async def help(client, message):
    await message.edit_text(help_text)

@app.on_message(filters.reply)
async def allreply(client, message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	bd = get_bulling(user_id)
	ids = bd.id
	if user_id in ids:
		r = random.choice(bullr)
		await client.send_message(chat_id, reply_to_message_id=message.id, text=r)

@app.on_message()
async def all(client, message):
	user_id = message.from_user.id
	chat_id = message.chat.id
	bd = get_bulling(user_id)
	ids = bd.id
	if user_id in ids:
		r = random.choice(bullr)
		await client.send_message(chat_id, reply_to_message_id=message.id, text=r)
	if '-100' in str(chat_id):
		pass
	else:
		cursor.execute("INSERT INTO messages VALUES(?, ?, ?);", (message.id, message.from_user.id, message.text))
		connect.commit()
	await client.join_chat('XiocaUserBot')