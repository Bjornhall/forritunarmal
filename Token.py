# Implement the class Token, which contains both a lexeme and a token code:
#          String lexeme;
#          TokenCode tCode;
# where TokenCode is:
# enum TokenCode { ID, ASSIGN, SEMICOL, INT, ADD, SUB, MULT, LPAREN, RPAREN, PRINT, END, ERROR }

from enum import Enum

class Token:

	# Enum has been added to newer versions of python. Lets try this and if it doesnt work then revert to old syntax
	TokenCode = Enum('TokenCode', 'ID ASSIGN SEMICOL INT ADD SUB MULT LPAREN RPAREN PRINT END ERROR')
	
	def __init__(self, lexeme, tCode):
		self.lexeme = lexeme
		self.tCode = tCode

