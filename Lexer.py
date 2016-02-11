from Token import Token
import sys
import re

	# Implement the class Lexer, a lexical analyzer. It should contain a public method, nextToken(),
	# which scans the standard input (stdin), looking for patterns that match one of the tokens from 1).
	# Note that the lexemes corresponding to the tokens ADD, SUB, MULT, LPAREN, RPAREN, ASSIGN, SEMICOL
	# contain only a single letter. The patterns for the lexemes for the other tokens are:
	#     INT   = [0-9]+
	#     ID    = [A-Za-z]+
	#     END   = end
	#     PRINT = print
	# The lexical analyzer returns a token with TokenCode = ERROR if some illegal lexeme is found.

class Lexer:

	def __init__(self):
		self.hasInput = False
		self.input = ""
		self.index = 0

	def nextToken(self):
		if not self.hasInput:
			self.input = sys.stdin.read()
			self.hasInput = True

		# Remove whitespace
		self.input = input.replace(" ", "")

		# List og lexemes
		lexemes = [
			("end", Token.TokenCode.END),
			("print", Token.TokenCode.PRINT),
			("\+", Token.TokenCode.ADD),
			("\-", Token.TokenCode.SUB),
			("\*", Token.TokenCode.MULT),
			("\(", Token.TokenCode.LPAREN),
			("\)", Token.TokenCode.RPAREN),
			("=", Token.TokenCode.ASSIGN),
			("\;", Token.TokenCode.SEMICOL),
			("[0-9]+", Token.TokenCode.INT),
			("[A-Za-z]+", Token.TokenCode.ID)]


		for lexeme, tCode in lexemes:

			# Match the lexeme at index to corrosponding lexeme in lexemes with the re library.
			matchedLexeme = re.match(lexeme, self.input[self.index:])

			# If a match is found make a Token with the constructor by sending in lexeme and tokenCode
			# UpDate the index
			if matchedLexeme:
				lexemLength = matchedLexeme.end()
				nToken = Token(self.input[self.index:self.index + lexemLength], tCode)
				self.index += lexemLength
				return nToken

		# If there is no lexeme that is a mactch - return error.		
		return Token("error", Token.TokenCode.ERROR)
