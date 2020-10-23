import logging

#словарь латиницы
dic_eng = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25, ' ':111}
#словарь кириллицы
dic_rus = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4, 'е':5, 'ё':6, 'ж':7, 'з':8, 'и':9, 'й':10, 'к':11, 'л':12, 'м':13, 'н':14, 'о':15, 'п':16, 'р':17, 'с':18, 'т':19, 'у':20, 'ф':21, 'х':22, 'ц':23, 'ч':24, 'ш':25, 'щ':26, 'ъ':27, 'ы':28, 'ь':29, 'э':30, 'ю':31, 'я':32, ' ':111}

# создание логгера
logger = logging.getLogger("CaesarCipher")
logger.setLevel(logging.INFO)
# создание файла лога
fh = logging.FileHandler("caesar_log.txt")
# создание форматтера
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# привязка форматтера к обработчику
fh.setFormatter(formatter)
# добавление обработчика к логгеру
logger.addHandler(fh)

logger.info("Program started")

#функция для возврата ключа словря по значению для англ. языка
def get_key_eng(val):
	for key, value in dic_eng.items():
		if val == value:
			return key
	return " "

#функция для возврата ключа словря по значению для рус. языка
def get_key_rus(val):
	for key, value in dic_rus.items():
		if val == value:
			return key
	return " "

#функция шифровки
def caesar(lang, mode, word, step):
	if mode == 1:
		logger.info("Process of encrypting started")
	else:
		logger.info("Process of decrypting started")

	new_word = []
	if lang == 1: #работа с англ. словарем
		for i in list(word): #цикл для перевода сообщения в список из ключей
			new_word.append(dic_eng.get(i))
		new_word_word = []
		if mode == 1: #режим шифрования (сдвиг вправо)
			for j in new_word: #цикл для обновления ключей в списке с учетом шага
				if j+step > 25:
					new_word_word.append(get_key_eng(j+step-26))
				else:
					new_word_word.append(get_key_eng(j+step))
		elif mode == 2: #режим дешифровки (сдвиг влево)
			for j in new_word: #цикл для обновления ключей в списке с учетом шага и записи значения ключа в список "new_word_word"
				if j - step < 0:
					new_word_word.append(get_key_eng(j-step + 26))
				else:
					new_word_word.append(get_key_eng(j-step))

	elif lang == 2: #работа с рус. словарем
		for i in list(word):
			new_word.append(dic_rus.get(i))
		new_word_word = []
		if mode == 1:
			for j in new_word:
				if j+step > 32:
					new_word_word.append(get_key_rus(j+step-33))
				else:
					new_word_word.append(get_key_rus(j+step))
		elif mode == 2:
			for j in new_word:
				if j - step < 0:
					new_word_word.append(get_key_rus(j-step + 33))
				else:
					new_word_word.append(get_key_rus(j-step))
	final_message = ''.join(new_word_word)
	logger.info(f"Encrypted/decrypted message: '{final_message}'")
	return final_message #возврат значений нового списка "new_word_word" в виде строки (т.е. вывод зашифрованного или расшифрованного сообщения)



#меню
print('Welcome to the Caesar Cipher!')
while True: #"зацикленность" меню до тех пор, пока не будет выбран выход
	print('\nModes:\n1 - Encrypt message\n2 - Decrypt message\n0 - Exit')
	mode = input('Choose mode: ') #выбор режима
	if mode == '0': #выход
		print('Goodbye...')
		logger.info("Program closed")
		break
	if mode.isdigit(): # проверка на число
		if (int(mode) == 1) or (int(mode) == 2): #проверка режима на значение "1" или "2"
			lang = input('Choose alphabet (1 - English, 2 - Russian): ') #выбор алфавита
			if lang.isdigit(): #проверка на число
				if (int(lang) == 1) or (int(lang) == 2): #проверка языка на значение "1" или "2"
					step = input('Enter step: ')
					if step.isdigit(): #проверка шага на число
						message = str(input('Enter message: '))
						logger.info(f"Message entered: '{message}'")
						print(caesar(int(lang), int(mode), message.lower(), int(step))) #ввод самого сообщения, преобразование к нижнему регистру и последующий его вывод
					#дальше идут указания на допущенную пользователем ошибку при вводе
					else:
						logger.error("Invalid 'step' value: must be integer")
						print('Step must be an integer')
				else:
					logger.error("Invalid 'language' value: must be 1 or 2")
					print('Language value must be 1 or 2')
			else:
				logger.error("Invalid 'language' value: must be integer")
				print('Language value must be an integer')
		else:
			logger.error("Invalid 'mode' value: must be 1 or 2")
			print('Mode value must be 1 or 2')
	else:
		logger.error("Invalid 'mode' value: must be integer")
		print('Mode value must be an integer')
