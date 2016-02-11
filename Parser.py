from Lexer import Lexer
from Token import Token

# Implement the class Parser, the syntax analyzer (parser). This should be a top-down recursive- descent parser for the grammar G above.
# The output of the parser is the stack-based inter- mediate code S, corresponding to the given program, written to standard output (stdout).
# If the expression is not in the language (or if an ERROR token is returned by the Lexer) then the parser should output the error message
# “Syntax error!” (at the point when the error is recognized) and immediately quit.
# The parser should have at least two (private) member variables, one of type Lexer, the other of type Token (for the current token).
# It should only have a single public method, parse(), for initiating the parse – other methods are private.

class Parser:
	
	def __init__(self, lexeme):
		self.lexeme = lexeme
		self.cToken = self.Lexer.nextToken()

	def parse(self):
		self.statements()

	def printError(self):
		print "Syntax error!"
        quit()

	# Statements → Statement ; Statements | end
	def statements(self):
		tCode = self.cToken.tCode

		# Deals with | end
		if tCode == Token.TokenCode.END:
			return

		# Deals with Statement ; Statements
		self.statement()
		if tCode == Token.TokenCode.SEMICOL:
			self.cToken = self.Lexer.nextToken()
			self.statements()
		else:
			self.printError()



		

