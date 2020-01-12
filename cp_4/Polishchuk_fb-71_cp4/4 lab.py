import string 
import math
import re
from collections import Counter



def poryadok():
	counter = 0
	num = 1
	while num < 10:
		suma = 0
		for i in range (0, len(polinom)):
			if polinom[i] * impuls1[i] == 1:
				suma = suma + 1
		suma = suma % 2 
		meme.insert(counter, impuls1[0])
		counter = counter + 1
		for i in range (0, len(impuls1) - 1):
			impuls1[i] = impuls1[i + 1]
		impuls1[len(polinom) - 1] = suma
		#print(impuls1, '\n', impuls)
		if impuls1 == impuls:
			return;



def bigrams():
	meme1 = ''
	for i in range (0, len(meme)):
		meme1 = meme1 + str(meme[i])
	meme1 = re.findall(r'[0-1][0-1]', meme1)
	count = Counter(meme1)
	print('Bigrams: ', count)

def treegrams():
	meme1 = ''
	for i in range (0, len(meme)):
		meme1 = meme1 + str(meme[i])
	meme1 = re.findall(r'[0-1][0-1][0-1]', meme1)
	count = Counter(meme1)
	print('\nTreegrams: ', count)

def fourgrams():
	meme1 = ''
	for i in range (0, len(meme)):
		meme1 = meme1 + str(meme[i])
	meme1 = re.findall(r'[0-1][0-1][0-1][0-1]', meme1)
	count = Counter(meme1)
	print('\nFourgrams: ', count)

def fivegrams():
	meme1 = ''
	for i in range (0, len(meme)):
		meme1 = meme1 + str(meme[i])
	meme1 = re.findall(r'[0-1][0-1][0-1][0-1][0-1]', meme1)
	count = Counter(meme1)
	print('\nFivegrams: ', count)

def autocorelacia():
	for i in range (1, 10+1):
		hey = 0
		for j in range(0, len(meme)):
			hey = hey + ((meme[j] + meme[(j + i)%len(meme)])%2)
		print ('Autocorelyacia ', i, ': ', hey, '\n')



meme = []
polinom1 = [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
impuls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
impuls1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
polinom = [1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1]


print('Polinom: ', polinom, '\nImpuls: ', impuls)
poryadok()
print(len(meme))
bigrams()
treegrams()
fourgrams()
fivegrams()
autocorelacia()
#print(len(meme))
#print(meme[0], meme[7])
#print('hello', str(meme[0]), str(meme[7]))