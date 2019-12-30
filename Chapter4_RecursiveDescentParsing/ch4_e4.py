# @filename ch4_e4.py
# @author Chantelle G. Dubois 
# @date 29 December, 2019
#
# Reuses some code from sp.py/Anthony J. Dos Reis

import sys

'''
Question 4: Write a parser based on the following grammar after
you simplify it with the star operator:

	<S> -> 'a' <B> <S>
	<S> -> 'e'
	<B> -> 'b' 'c' 'd'

Test with: e, abcde, abcdabcde, lambda, abcdex, and abcdabcd
'''

'''
Comments: Simplifying with the star operator we have
	<S> -> 'a' ('b' 'c' 'd') (('e')* | ('a' ('b' 'c' 'd'))* 'e')
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
	<S> -> 'a' <B> <S>
	<S> -> 'e'
	'''
	if token == 'a':
		consume('a')
		B()
		S()

	elif token == 'e':

		while token == 'e':
			consume('e')

	else:
		raise RuntimeError("Expecting a or e")

def B():
	'''
	<B> -> 'b' 'c' 'd'
	'''
	consume('b')
	consume('c')
	consume('d')

main()