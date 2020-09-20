dic = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25, ' ':100}
def get_key(val):
	for key, value in dic.items():
		if val == value:
			return key
	return " "
def caesar(mode, word, step):
	new_word = []
	for i in list(word):
		new_word.append(dic.get(i))
	new_word_word = []
	if mode == 1:
		for j in new_word:
			if j+step > 25:
				new_word_word.append(get_key(j+step-26))
			else:
				new_word_word.append(get_key(j+step))
	elif mode == 2:
		for j in new_word:
			if j - step < 0:
				new_word_word.append(get_key(j-step + 26))
			else:
				new_word_word.append(get_key(j-step))

	return ''.join(new_word_word)

print('Welcome to the Caesar Cipher!\nModes:\n1 - Encrypt message\n2 - Decrypt message')
print(caesar(int(input('Choose mode: ')), str(input('Enter message: ')), int(input('Enter step: '))))