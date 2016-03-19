#This is the font part, importing from font.py
from font import *

##------------------------------##
#This is the splitting part, to split each line of one charater into a list

alphabet = []
alphabet_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabet_picture = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

for letter in alphabet_picture:
	alphabet.append(letter.split('\n'))

alphabet = dict(zip(alphabet_list,alphabet)) #creat a dictionary to designate every charater with its splited picture

##------------------------------##
#This is the reading part, to read the inputed word from keyboard

print "Please enter a word in any length, no matter the case, but alphabet and space only."

input = raw_input("Input: ").upper()
 
LETTER = []
	
def letter_read(input):
	global alphabet, A
	print input
	for letter in input:
		verbose = False
		if letter in alphabet_list:          #assign each letter's splited picture to LETTER in order
			LETTER.append(alphabet[letter])
			verbose = True
		if verbose == False:
			if letter == ' ':                #deal with blank letter 
				LETTER.append(['           ' for i in range(len(A.split('\n')))])  
			else:
				raise TypeError("Your word has contained at least one invalid charaters: ", letter)
				
letter_read(input)

##------------------------------##
#This is the displaying part, to display the output

def display_letter():
	global LETTER, A
	display = ''
	letter_limit = 10   #decide the limit number of letters for every line
	line, rem = divmod(len(LETTER), letter_limit)
	if rem != 0:                                  #decide how many lines needed to display
		line += 1
	for i in range(line):                         #display the word in upper case
		for indx in range(len(A.split('\n'))):
			if i != line-1:
				for inx in range(letter_limit):
					display += LETTER[inx+letter_limit*i][indx]
				display += '\n'
			elif i == line-1:
				for inx in range(rem):
					display += LETTER[inx+letter_limit*i][indx]
				display += '\n'

	import time
	import sys
	def delay_print(s):                #display the word with fake refreshing action
		for c in s:
			sys.stdout.write( '%s' % c )
			sys.stdout.flush()
			time.sleep(0.001)

	delay_print(display)

display_letter()

	