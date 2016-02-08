from Token import Token
import sys
import re

class Lexer:
    # Implement the class Lexer, a lexical analyzer. It should contain a public method, nextToken(),
    # which scans the standard input (stdin), looking for patterns that match one of the tokens from 1).
    # Note that the lexemes corresponding to the tokens ADD, SUB, MULT, LPAREN, RPAREN, ASSIGN, SEMICOL
    # contain only a single letter. The patterns for the lexemes for the other tokens are:
    #     INT   = [0-9]+
    #     ID    = [A-Za-z]+
    #     END   = end
    #     PRINT = print
    # The lexical analyzer returns a token with TokenCode = ERROR if some illegal lexeme is found.