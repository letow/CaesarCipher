dic_eng = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25, ' ':111}
dic_rus = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4, 'е':5, 'ё':6, 'ж':7, 'з':8, 'и':9, 'й':10, 'к':11, 'л':12, 'м':13, 'н':14, 'о':15, 'п':16, 'р':17, 'с':18, 'т':19, 'у':20, 'ф':21, 'х':22, 'ц':23, 'ч':24, 'ш':25, 'щ':26, 'ъ':27, 'ы':28, 'ь':29, 'э':30, 'ю':31, 'я':32, ' ':111}

def get_key_eng(val):
	for key, value in dic_eng.items():
		if val == value:
			return key
	return " "
def get_key_rus(val):
	for key, value in dic_rus.items():
		if val == value:
			return key
	return " "

def caesar(lang, mode, word, step):
	new_word = []
	if lang == 1:
		for i in list(word):
			new_word.append(dic_eng.get(i))
		new_word_word = []
		if mode == 1:
			for j in new_word:
				if j+step > 25:
					new_word_word.append(get_key_eng(j+step-26))
				else:
					new_word_word.append(get_key_eng(j+step))
		elif mode == 2:
			for j in new_word:
				if j - step < 0:
					new_word_word.append(get_key_eng(j-step + 26))
				else:
					new_word_word.append(get_key_eng(j-step))
	elif lang == 2:
		for i in list(word):
			new_word.append(dic_rus.get(i))
		new_word_word = []
		if mode == 1:
			for j in new_word:
				if j+step > 25:
					new_word_word.append(get_key_rus(j+step-33))
				else:
					new_word_word.append(get_key_rus(j+step))
		elif mode == 2:
			for j in new_word:
				if j - step < 0:
					new_word_word.append(get_key_rus(j-step + 33))
				else:
					new_word_word.append(get_key_rus(j-step))
	return ''.join(new_word_word)

print('Welcome to the Caesar Cipher!')
while True:
	print('\nModes:\n1 - Encrypt message\n2 - Decrypt message\n0 - Exit')
	mode = input('Choose mode: ')
	if mode == '0':
		print('Goodbye...')
		break
	if mode.isdigit():
		if (int(mode) == 1) or (int(mode) == 2):
			lang = input('Choose alphabet (1 - English, 2 - Russian): ')
			if lang.isdigit():
				if (int(lang) == 1) or (int(lang) == 2):
					step = input('Enter step: ')
					if step.isdigit():
						print(caesar(int(lang), int(mode), str(input('Enter message: ')).lower(), int(step)))
					else: print('Step must be an integer')
				else: print('Language value must be 1 or 2')
			else: print('Language value must be an integer')
		else: print('Mode value must be 1 or 2')
	else: print('Mode value must be an integer')
