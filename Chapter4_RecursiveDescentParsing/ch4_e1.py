# @filename ch4_e1.py
# @author Chantelle G. Dubois 
# @date 29 December, 2019
#
# Reuses some code from sp.py/Anthony J. Dos Reis

import sys

'''
Question 1: Write a parser based on the following grammar:
	<S> -> 'a' <S> 'b'
	<S> -> 'c'

Test with: c, acb, aacbb, lambda, ca, ab, acbb, aacb, and bca.
'''

'''
Comments: Can be expressed as {(a^i)c(b^i) | i >= 0} 
or <S> -> ('a')* 'c' ('b')*. In this case, using
a recursive function makes sense. 
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
		print('Pass')

def S():
	# there can be zero or more a's and b's'
	# but there has to be just as many of each
	if token == 'a':
		a_count = 0
		
		while token == 'a':
			consume('a')
			a_count += 1
		
		S()

		# there has to be the same num of b's
		# as a's

		while (a_count > 0):
			a_count -= 1
			consume('b')

	# there has to be at least 1 c
	elif token == 'c':
		advance()

	else:
		raise RuntimeError('Expecting a or c')

main()