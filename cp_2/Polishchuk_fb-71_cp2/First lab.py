import re
import math
import codecs
import string 
from collections import Counter


'''textO = re.findall(r'[а-я]', codecs.open ("text.txt", 'r', 'utf-8').read())
print('textO', len(textO),'\n', textO)

textW = re.findall(r'[ а-я \n]', codecs.open ("text.txt", 'r', 'utf-8').read())
meh = ''
for i in range(0, len(textW)):
    meh = meh + textW[i]
textW = meh.replace('\n', ' ')
print('textW', len(textW), '\n', textW)'''

a = ord('а')
b = ord ('я')


def find_text():
    meh = ''
    textW = re.findall(r'[ а-я \n]', codecs.open ("text.txt", 'r', 'utf-8').read())
    for i in range(0, len(textW)):
        meh = meh + textW[i]
    textW = meh.replace('\n', ' ')
    return textW

#____________________________Monograms Without____________________________
def monograms_without(textO, a, b):
    textO = re.findall(r'[а-я]', textO)
    print(len(textO))
    #print(a, b)
    count = Counter(textO)	
    print ('____________________________Monograms Without____________________________\n')
    entropiya = 0
    for i in range(a, b+1):
        if count[chr(i)]!=0:
            chastota = count[chr(i)]/len(textO)
            entropiya = entropiya + chastota * math.log2(chastota)
            print (chr(i), count[chr(i)], 'chastota = ', chastota)
        else:
            entropiya = entropiya
    print("entroyiya: ", entropiya*-1)
#____________________________END OF FUNCTION____________________________



#____________________________Monograms With____________________________
def monograms_with(textW, a, b):
    #print(textW)
    textW = re.findall(r'[ а-я ]', textW)
    #print(textW)
    count = Counter(textW)	
    print ('____________________________Monograms With____________________________\n')
    chastota = count[chr(32)]/len(textW)
    entropiya = chastota * math.log2(chastota)
    print(chr(32), count[chr(32)], 'chastota = ', chastota)
    for i in range(a, b+1):
        if count[chr(i)] !=0:
            chastota = count[chr(i)]/len(textW)
            entropiya = entropiya + chastota * math.log2(chastota)
            print (chr(i), count[chr(i)], 'chastota = ', chastota)
    print("entroyiya: ", (entropiya*-1))
#____________________________END OF FUNCTION____________________________

#____________________________Bigrams Without____________________________
def bigrams_without(textO, a, b):
    textO = textO.replace(' ','')
    c = len(textO)
    textO = re.findall(r'[а-я][а-я]', textO)
    #print(textO)
    k = 1.731
    count = Counter(textO)
    h = list(count)
    print ('____________________________Bigrams Without____________________________\n')
    entropiya = 0
    for i in range (0, len(h)-1):
    	chastota = count[h[i]]/c
    	entropiya = entropiya + chastota * math.log2(chastota)
    	print(h[i], count[h[i]], 'chastota = ', chastota)
    print('entropiya: ', (entropiya*-1)/2)
 
#____________________________END OF FUNCTION____________________________

#____________________________Bigrams With_______________________________
def bigrams_with(textW, a, b):
    textW = re.findall(r'[ а-я ][ а-я ]', textW)
    #print(textW)
    count = Counter(textW)
    k = 1.845
    h = list(count)
    print ('____________________________Bigrams With_______________________________\m')
    entropiya = 0
    for i in range (0, len(h)-1):
    	chastota = count[h[i]]/len(text)
    	entropiya = entropiya + chastota * math.log2(chastota)
    	print (h[i], count[h[i]], 'chastota = ', chastota)
    print('entropiya: ', (entropiya*-1)/2)

#____________________________END OF FUNCTION____________________________

#___________________Bigrams(intersections) Without_______________________
def bigram_in_without(textO, a, b):
	textO = textO.replace(' ', '')
	c = len(textO)
	#print(c)
	p = ''
	for i in range(0, c - 1):
	    p = p + textO[i]+textO[i+1]
	textO = re.findall(r'[а-я][а-я]', p)
	c = len(p)
	#print(textO)
	count = Counter(textO)
	print ('___________________Bigrams(intersections) Without_______________________\n')
	entropiya = 0
	for i in range(a, b+1):
		for j in range(a, b+1):
			if count[chr(i)+chr(j)]!=0:
				chastota = count[chr(i)+chr(j)]/c
				entropiya = entropiya + chastota * math.log2(chastota)
				print(chr(i)+chr(j), count[chr(i)+chr(j)], 'chastota = ', chastota)
	print("entropiya: ", (entropiya *-1)/2)
#____________________________END OF FUNCTION____________________________

#___________________Bigrams(intersections) With_______________________
def bigram_in_with(textW, a, b):
	c = len(textW)
	p = ''
	for i in range(0, c - 1):
	    p = p + textW[i]+textW[i+1]
	c = len(p)
	#print(p)
	textW = re.findall(r'[ а-я ][ а-я ]', p)
	#print(textW)
	count = Counter(textW)
	print ('___________________Bigrams(intersections) With_______________________\n')
	entropiya = 0
	for i in range(a, b+1):
		for j in range(a, b+1):
			if count[chr(i)+chr(j)]!=0:
				chastota = count[chr(i)+chr(j)]/c
				entropiya = entropiya + chastota * math.log2(chastota)
				print(chr(i)+chr(j), count[chr(i)+chr(j)], 'chastota = ', chastota)
		if count[chr(i)+chr(32)]!=0:
			chastota = count[chr(i)+chr(32)]/c
			entropiya = entropiya + chastota * math.log2(chastota)
			print(chr(i)+chr(32), count[chr(i)+chr(32)], 'chastota = ', chastota)
		if count[chr(32)+chr(i)]!=0:
			chastota = count[chr(32)+chr(i)]/c
			entropiya = entropiya + chastota * math.log2(chastota)
			print(chr(32)+chr(i), count[chr(32)+chr(i)], 'chastota = ', chastota)
	print('entropiya: ', (entropiya * -1)/2)


text = find_text()
monograms_without(text, a, b)
monograms_with(text, a, b)
bigrams_without(text, a, b)
bigrams_with (text, a, b)
bigram_in_without(text, a, b)
bigram_in_with(text,a,b)