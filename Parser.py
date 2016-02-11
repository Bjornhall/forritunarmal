from Lexer import Lexer
from Token import Token

class Parser:
	
	def __init__(self, lexeme):
		self.lexeme = lexeme
		self.cToken = self.Lexer.nextToken()

	def parse(self):
		self.statements()

	def printError(self):
		print "Syntax error!"
        quit()

	# Statements => Statement ; Statements | end
	def statements(self):
		tCode = self.cToken.tCode

		# Deals with Statements => end
		if tCode == Token.TokenCode.END:
			return

		# Deals with Statements => Statement ; Statements
		self.statement()
		if tCode == Token.TokenCode.SEMICOL:
			self.cToken = self.Lexer.nextToken()
			self.statements()
		else:
			self.printError()

	# Statement => id = Expr | print id
	def statement(self):
		tCode = self.cToken.tCode

		# Deals with Statement => id = Expr
		if tCode == Token.TokenCode.ID:
			print "PUSH" + self.cToken.lexeme

			# Update cToken and tCode
			self.cToken = self.Lexer.nextToken()
			tCode = self.cToken.tCode

			# Check if next token is '=', then Expr sould follow
			if tCode == Token.TokenCode.ASSIGN:
				self.cToken = self.Lexer.nextToken()
				self.expr()
				print "ASSIGN"
			else:
				self.printError()

		# Deals with Statement => print id
		elif tCode == Token.TokenCode.PRINT:

			# Update cToken and tCode
			self.cToken = self.Lexer.nextToken()
			tCode = self.cToken.tCode

			# Check if next token is 'ID', then PUSH id and PRINT
			if tCode == Token.TokenCode.ID:
				print "PUSH" + self.cToken.lexeme
				print "PRINT"
			else:
				self.printError()

		else:
			self.printError()

	# Expr => Term | Term + Expr | Term - Expr
	def expr(self):

		# Expr always leads to Term
		self.term()

		# Checks if following token is '+' or '-'
		tCode = self.cToken.tCode
		if tCode == Token.TokenCode.ADD:
			self.cToken = self.Lexer.nextToken()
			self.expr()
			print "ADD"
		elif tCode == Token.TokenCode.SUB:
			self.cToken = self.Lexer.nextToken()
			self.expr()
			print "MINUS"
		# Tarf error? ef ekki ta breyta elif i else !!!!

	# Term => Factor | Factor * Term
	def term(self):
		
		# Term always leads to Factor
		self.factor()

		# Check if following token is '*'
		tCode = self.cToken.tCode
		if tCode == Token.TokenCode.MULT:
			self.cToken = self.Lexer.nextToken()
			self.term()
			print "MULT"
		# Tarf error????

	# Factor => int | id | ( Expr )
	def factor(self):
		tCode = self.cToken.tCode

		# Checks if token is 'int' or 'id'
		if tCode == Token.TokenCode.INT:
			print "PUSH" + self.cToken.lexeme
			self.cToken = self.Lexer.nextToken()
		elif tCode == Token.TokenCode.ID:
			print "PUSH" + self.cToken.lexeme
			self.cToken = self.Lexer.nextToken()

		# Checks for '(' and ')' and calls Expr inbetween
		elif tCode == Token.TokenCode.RPAREN:
			self.cToken = self.Lexer.nextToken()
			self.expr()

			# Error handles parentesis mismatch
			if tCode == Token.TokenCode.LPAREN:
				self.cToken = self.Lexer.nextToken()
				return
			else:
				self.printError()

		else:
			self.printError()