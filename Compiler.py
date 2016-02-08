from Lexer import Lexer
from Parser import Parser

lex = Lexer()
parser = Parser(lex)
parser.parse()