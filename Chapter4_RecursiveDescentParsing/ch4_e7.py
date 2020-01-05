# @filename ch4_e7.py
# @author Chantelle G. Dubois
# @date 5 January, 2020
#
# Modified code from sp.py/Anthony J. Dos Reis

import sys   # needed to access command line arg

'''
Question 7: Copy sp.py to p0407.py. Then modify p0407.py so that
it parses without using recursion.
'''

'''
Comments: Recursion occurs in C()
'''

#global variables
tokenindex = -1
token = ''

def main():
   try:
      parser()      # call the parser
   except RuntimeError as emsg:
      print(emsg)

def advance():
   global tokenindex, token
   tokenindex += 1    # move tokenindex to next token
   # check for null string or end of string
   if len(sys.argv) < 2 or tokenindex >= len(sys.argv[1]):
      token = ''      # signal the end by returning ''
   else:
      token = sys.argv[1][tokenindex]

def consume(expected):
   if expected == token:
      advance()
   else:
      raise RuntimeError('Expecting ' + expected)

def parser():
   advance()   # prime token with first character
   S()         # call function for start symbol
   # test if end of input string
   if token != '': 
      print('Garbage following <S>-string')
   
def S():
   A()
   C()

def A():
   consume('a')
   consume('b')

def C():
   '''
   <C> -> 'c'<C>
   <C> -> 'd'
   '''
   if token == 'c':
      # perform actions corresponding to production 3
      while token == 'c':
         advance()

      consume('d')
      #C()
   elif token == 'd':
      # perform action corresponding to production 4
      advance()
   else:
      raise RuntimeError('Expecting c or d')

main()
