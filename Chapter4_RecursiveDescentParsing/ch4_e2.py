# @filename ch4_e2.py
# @author Chantelle G. Dubois 
# @date 29 December, 2019
#
# Reuses some code from sp.py/Anthony J. Dos Reis

import sys

'''
Question 2: Write a parser based on the following grammar:
	<S> -> 'a' <B> 'c'
	<B> -> ('b''b')* ['c']

Test with: ac, acc, abbcc, abcc, lambda, a, ac, abc, and acca.
'''

# global vars
tokenindex = -1
token = ''

def main():
	'''
	Initializes parser or prints error
	'''
	try:
		parser()
	except RuntimeError as emsg:
		print(emsg)

def advance():
	'''
	Advances the token through the string until
	end is detected
	'''
	global tokenindex, token
	tokenindex +=1 # move to next token

	# check if null string or end of string
	if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
		token = ''
	# otherwise all tokens parsed	
	else:
		token = sys.argv[1][tokenindex]

def consume(expected):
	'''
	Consumes the token 
	'''
	if expected == token:
		advance()
	else:
		raise RuntimeError('Expecting ' + expected)

def parser():
	advance()	# prime token with first character
	S()			# call function for start symbol

	# test if end of input string
	if token != '':
		print('Garbage following <S>-string')
	else:
		print("Pass")

def S():
	if token == 'a':
		consume('a')
		B()
		C()
	elif token == 'b':
		advance()
	else:
		raise RuntimeError('Expecting a or b')

def B():
	'''
	b has to come in 0 or more pairs and is optionally
	followed  by c
	'''

	# the bb pairs can occur 0 or more times
	while token == 'b':
		consume('b')
		consume('b')

	if token == 'c':
		# check if this c is the last token
		if tokenindex == (len(sys.argv[1])-1):
			pass
		else:
			C()
	else:
		raise RuntimeError('Expecting b or c')

def C():
	advance()

main()