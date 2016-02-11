from Token import Token
import sys
import re

class Lexer:

	def __init__(self):
		self.hasInput = False
		self.myInput = ""
		self.index = 0

	def nextToken(self):
		if not self.hasInput:
			self.myInput = sys.stdin.read()
			self.hasInput = True

		# Remove whitespace
		self.myInput = "".join(self.myInput.split())
		# self.myInput = myInput.replace(" ", "")

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
			matchedLexeme = re.match(lexeme, self.myInput[self.index:])

			# If a match is found make a Token with the constructor by sending in lexeme and tokenCode
			# UpDate the index
			if matchedLexeme:
				lexemLength = matchedLexeme.end()
				nToken = Token(self.myInput[self.index:self.index + lexemLength], tCode)
				self.index += lexemLength
				return nToken

		# If there is no lexeme that is a mactch - return error.		
		return Token("error", Token.TokenCode.ERROR)
