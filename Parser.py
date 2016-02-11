from Lexer import Lexer
from Token import Token

class Parser:
	
	def __init__(self, myLexer):
		self.lexer = myLexer
		self.cToken = self.lexer.nextToken()

	def parse(self):
		self.statements()

	# Statements => Statement ; Statements | end
	def statements(self):

		# Deals with Statements => end
		if self.cToken.tCode == Token.TokenCode.END:
			return

		# Deals with Statements => Statement ; Statements
		self.statement()
		if self.cToken.tCode == Token.TokenCode.SEMICOL:
			self.cToken = self.lexer.nextToken()
			self.statements()
		else:
			self.printError()

	# Statement => id = Expr | print id
	def statement(self):

		# Deals with Statement => id = Expr
		if self.cToken.tCode == Token.TokenCode.ID:
			print "PUSH " + self.cToken.lexeme

			# Update cToken and tCode
			self.cToken = self.lexer.nextToken()

			# Check if next token is '=', then Expr sould follow
			if self.cToken.tCode == Token.TokenCode.ASSIGN:
				self.cToken = self.lexer.nextToken()
				self.expr()
				print "ASSIGN"
			else:
				self.printError()

		# Deals with Statement => print id
		elif self.cToken.tCode == Token.TokenCode.PRINT:

			# Update cToken and tCode
			self.cToken = self.lexer.nextToken()

			# Check if next token is 'ID', then PUSH id and PRINT
			if self.cToken.tCode == Token.TokenCode.ID:
				print "PUSH " + self.cToken.lexeme
				print "PRINT"
				self.cToken = self.lexer.nextToken()
			else:
				self.printError()

		else:
			self.printError()

	# Expr => Term | Term + Expr | Term - Expr
	def expr(self):

		# Expr always leads to Term
		self.term()

		# Checks if following token is '+' or '-'
		if self.cToken.tCode == Token.TokenCode.ADD:
			self.cToken = self.lexer.nextToken()
			self.expr()
			print "ADD"
		elif self.cToken.tCode == Token.TokenCode.SUB:
			self.cToken = self.lexer.nextToken()
			self.expr()
			print "SUB"
		# Tarf error? ef ekki ta breyta elif i else !!!!

	# Term => Factor | Factor * Term
	def term(self):
		
		# Term always leads to Factor
		self.factor()

		# Check if following token is '*'
		if self.cToken.tCode == Token.TokenCode.MULT:
			self.cToken = self.lexer.nextToken()
			self.term()
			print "MULT"
		# Tarf error????

	# Factor => int | id | ( Expr )
	def factor(self):

		# Checks if token is 'int' or 'id'
		if self.cToken.tCode == Token.TokenCode.INT:
			print "PUSH " + self.cToken.lexeme
			self.cToken = self.lexer.nextToken()
		elif self.cToken.tCode == Token.TokenCode.ID:
			print "PUSH " + self.cToken.lexeme
			self.cToken = self.lexer.nextToken()

		# Checks for '(' and ')' and calls Expr inbetween
		elif self.cToken.tCode == Token.TokenCode.LPAREN:
			self.cToken = self.lexer.nextToken()
			self.expr()

			# Error handles parentesis mismatch
			if self.cToken.tCode == Token.TokenCode.RPAREN:
				self.cToken = self.lexer.nextToken()
				return
			else:
				self.printError()

		else:
			self.printError()

	def printError(self):
		print "Syntax error!"
		quit()