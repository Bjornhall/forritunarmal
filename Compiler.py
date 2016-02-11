from Lexer import Lexer
from Parser import Parser

myLexer = Lexer()
parser = Parser(myLexer)
parser.parse()