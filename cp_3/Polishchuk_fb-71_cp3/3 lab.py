import re
import math
import codecs
import string 
from collections import Counter
from collections import deque

a = ord('а')
b = ord ('я')

alphab = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',' п', 'р', 'с', 'т', 'у', 'ф',' х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я']

def find_text():
    meh = ''
    nubmers = []
    k = 0
    textW = re.findall(r'[а-я\n]', codecs.open ("text.txt", 'r', 'utf-8').read())
    for i in range(0, len(textW)):
        meh = meh + textW[i]
    #print(meh)
    textW = meh.replace('\n', '')
    for i in range(1, len(textW)):
        #meh = meh + textW[i]
        if i%2 != 0 :
        	#print ('literal a :', textW[i-1], ' literal b: ', textW[i], '\nOrd a: ', ord(textW[i-1])% 1072, ' Ord b: ', ord(textW[i])% 1072 )
        	oh = ((ord(textW[i-1]) - 1072) * 31) + (ord(textW[i]) - 1072)
        	nubmers.insert(k, oh)
        	k = k + 1
    #print(nubmers)
    return textW, nubmers

def bigrams(ourtext):
	meme1 = ''
	#some = [0, 0, 0, 0, 0]
	a = 100
	mem = ['','','','','']
	innum = []
	meme1 = re.findall(r'[а-я][а-я]', ourtext)
	#сount = Counter(meme1)
	#d = deque(some, len(сount))
	#print(сount)
	for i in range(0, 5):
		if i < 5:
			a, mem[i], num = the_best(a, meme1, mem)
			innum.insert(i, num)
			print (a)
	huy = Counter(meme1)
	print(mem)
	print(huy)
	return(innum)

def the_best(best, meme1, some):
	c = 0
	bigrama = ''
	сount = Counter(meme1)
	for	i in range (a, b+1):
		for	j in range (a, b+1):
			if сount[chr(i)+chr(j)] > c and сount[chr(i)+chr(j)] <= best:
				if chr(i)+chr(j) != some[0] and chr(i)+chr(j) != some[1] and chr(i)+chr(j) != some[2] and chr(i)+chr(j) != some[3] and chr(i)+chr(j) != some[4]:
					c = сount[chr(i)+chr(j)]
					bigrama = chr(i)+chr(j)
					innum = ((i - 1072) * 31) + (j - 1072)
						#print (chr(i)+chr(j))

	return(c, bigrama, innum)

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b//a) * x, x

def inverse(a, m):
    g, x, y = egcd(a, m)
    if g > 1:
        return x % (m/g)
    else:
        return x % m

def formula():
	mema = []
	memb = []
	k = 0
	for i in range (0, 5):
		for j in range (0, 5):
			for u in range (0, 5):
				for y in range (0, 5):
					a = (-(morenum1[j] - morenum1[y]) * inverse(morenum0[i]-morenum0[u], 961))%961
					b = (morenum1[j] - (a * morenum0[i]))%961
					mema.insert(k, a)
					memb.insert(k, b)
			k = k+1
	#print(mema, '\n', memb)
	return mema, memb
			
def decrypt():
	for i in range (0, len(a)):
		check = 0
		textnew = ''
		baddd = ['аы' ,'оы', 'еы', 'уы', 'оы', 'аь', 'оь', 'еь', 'иь', 'уь', 'ъщ', 'фд', 'ъв', 'аа']
		for j in range (0, len(nubmers)):
			if check == 1:
				break
			x = ((nubmers[j] - b[i]) * inverse(a[i], 961))%961
			x1 = int(x / 31)
			x2 = x - (31*x1)
			x1 = x1 + 1072
			x2 = x2 + 1072
			textnew = textnew + chr(int(x1)) + chr(int(x2))
			for k in range(0, 14):
				if chr(int(x1)) + chr(int(x2)) == baddd[k]:
					ploho = chr(int(x1)) + chr(int(x2))
					check = 1
		if check == 0:
			print('Text ', i, ': \n', textnew, '\n\n\n\n\n\n')
		else:
			print ('Not text №', i, ' beacouse have: ', ploho, 'a: ', a[i], ' b: ', b[i]) 



text, nubmers = find_text()
#print(nubmers)
most_frequent = ['ст', 'но', 'то', 'на', 'ен']
#print((ord('е') - 1072) * 32+ (ord('н') - 1072))
morenum1 = [562, 430, 590, 416, 173]
morenum0 = bigrams(text)
print (morenum1, '\n', morenum0)
#print (morenum0)
a, b = formula()
#print (a,'\n', b)
think = ''
#print('lennn: ', len(textnew), '\n', 'text ', i, ': \n', textnew, '\n\n\n\n\n\n')	
decrypt()
