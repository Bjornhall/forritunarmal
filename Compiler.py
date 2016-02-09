from Lexer import Lexer
from Parser import Parser

lexeme = Lexer()
parser = Parser(lexeme)
parser.parse()