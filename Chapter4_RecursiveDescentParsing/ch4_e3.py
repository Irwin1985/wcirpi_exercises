# @filename ch4_e3.py
# @author Chantelle G. Dubois 
# @date 29 December, 2019
#
# Reuses some code from sp.py/Anthony J. Dos Reis

import sys

'''
Question 3: Write a parser based on the following grammar:
	<S> -> 'a'* <B>
	<B> -> 'b'* <C>
	<C> -> 'c'['d'|'e']'f'

Test with: cf, cdf, cef, aabbcf, acb, bcf, lambda, cdef, cff, and abc.
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
	'''
	<S> -> 'a'* <B>
	'''
	while token == 'a':
		consume('a')
	B()

def B():
	'''
	<B> -> 'b'* <C>
	'''
	while token == 'b':
		consume('b')

	C()

def C():
	'''
	<C> -> 'c'['d'|'e']'f'
	'''
	consume('c')

	if token == 'd' or token == 'e':
		while (token == 'd' or token == 'e'):
			advance()

	consume('f')

main()