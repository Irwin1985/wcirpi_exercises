# @filename ch4_e6.py
# @author Chantelle G. Dubois
# @date 30 December, 2019
#
# Modified code from sp.py/Anthony J. Dos Reis

import sys   # needed to access command line arg

'''
Question 6: Copy sp.py to p0406.py. Then modify p0406.py so that
it obtains the input string from a file whose name is specified 
on the command line. 
'''

'''
Comments: Assuming multiple strings can be parsed from the same
file, so the parser will run in a loop until there are no more
strings to read. Also I'm assuming this feature is going to be 
needed for future chapter exercises.
'''

#global variables
tokenindex = -1
token = ''
tokenString = ''
tokenStringArray = []

def main():
   global token, tokenindex, tokenString, tokenStringArray
   
   # check if there is a candidate filename
   if len(sys.argv) < 2:
      print("Error - expecting a candidate filename")
   else:
      # read string from file then start parser
      print("Reading string from file " + repr(sys.argv[1]))
      read(sys.argv[1])

      for i in range(len(tokenStringArray)):
         # "reset" the vars for current iteration
         tokenString = tokenStringArray[i]
         token = ''
         tokenindex = -1

         print("Token string: " + tokenString)
      
         try:
            parser()      # call the parser
         except RuntimeError as emsg:
            print(emsg)

def advance():
   global tokenindex, token
   tokenindex += 1    # move tokenindex to next token
   # check for null string or end of string
   if len(tokenString) <= 0 or tokenindex >= len(tokenString):
      token = ''
   else:
      token = tokenString[tokenindex]

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
   else:
      print('Pass')

def read(filename):
   '''
   Reads strings from the specified file and 
   stores them in a string array for the parser
   '''
   global tokenStringArray

   try:
      tokenStringArray = [tokenString.rstrip('\n') for tokenString in open(filename)]

   except RuntimeError as emsg:
      print(emsg)

def S():
   A()
   C()

def A():
   consume('a')
   consume('b')

def C():
   if token == 'c':
      # perform actions corresponding to production 3
      advance()
      C()
   elif token == 'd':
      # perform action corresponding to production 4
      advance()
   else:
      raise RuntimeError('Expecting c or d')

main()