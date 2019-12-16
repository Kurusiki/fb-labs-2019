import codecs
import string 
import math
import re
from collections import Counter


start = ord('а')
end = ord ('я')
'''rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 
	   'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']'''

def search(shag):
	b = ''
	index = 0
	for i in range (0, len(text), shag):
		b = b + text[i]
	dlina = len(b)
	count = Counter(b)
	#print(count)
	for i in range(start, end+1):
		index = index + (count[chr(i)] * (count[chr(i)] - 1))/(dlina * (dlina - 1))
	if index >= 0.0553:
		print ('index: ', index, '\nshag: ', shag, '\n')
		return shag

def find_key(i, a, O):
	b = ''
	c = 0
	new = ''

	for j in range (i, len(text), a):
		b = b + text[j]
	count = Counter(b)
	print(count)
	for i in range(start, end+1):
		if count[chr(i)] > c:
			c = count[chr(i)]
			number = i
	#print('Номер буквы: ', number-1072, 'Буква: ', chr(number))
	if number-1072 < O:
		number = number + 32
	c = number - O
	print('\nНомер буквы: ', number-1072, 'Буква: ', chr(number), 'Буква Ключа: ', chr(c), 'Разница: ', c-1072+1, '\n\n')
	'''for i in range (0, len(b)):
		for j in range (0, 31):
			if b[i] == rus[j]:
				new = new + rus[j - c]'''

	return(c, new)

def full_decode(meme, a):
	check = 0
	list_code = ''
	for i in range(0, len(text) - 1):
		for value in range(start, end + 1):
			if text[i] == chr(value):
				if check == 17:
					check = 0
				c = value - meme[check]
				if c < 1072:
					h = c + 32
				else:
					h = c
				print ('First: ', value-1072, ' Key elem: ', meme[check], ' Second: ', h-1072)
				list_code = list_code + chr(h)
				check = check + 1
	print (list_code)


def decrypt():
	key = ''
	meme = []
	a = 0
	for i in range (2, 25):			# 					Поиск длины ключа
		a = search(i)
		if a == i:
			break					#					a = длина ключа (17)

	for i in range(0, a):			#					Формирование групп
		c, b = find_key(i, a, 14)	
		key = key + chr(c)
		meme.insert(i, c-1072) 
	print('Ключ: ', key)
	print('\nМассив разниц: ', meme)

	full_decode(meme, a)



text = codecs.open("mem.txt", 'r', 'utf-8').read()   #	text = наш текст
print(text)
decrypt()
huy = ''

for i in range(start, end+1):
	huy = huy + chr(i)
