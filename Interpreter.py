import sys

# A stack reprisenting the language S
S = []
# A map variable to store the values of the identifiers
map = {}

# A method for handling the exception of the language S being incorrect.
# If correct it pops the stack and returns the result
def stackpop(op):
    if S:
        return S.pop()
    else:
        print "Error for operator: " + op
        sys.exit()

# A method for parsing the input correctly before performing a operation
def checkInput(input1, input2):
    variables = [];
    if isinstance(input1, str):
        if input1.isdigit():
            variables.append(int(input1))
        else:
            variables.append(int(map[input1]))
    if isinstance(input2, str):
        if input2.isdigit():
            variables.append(int(input2))
        else:
            variables.append(int(map[input2]))
    return variables

# A loop that goes through each input line and handles the operator in it accordingly
for inputLine in sys.stdin:
    inputLine = InputLine.rstrip()
    if inputLine[0:4] == "PUSH":
        value = inputLine[5:]
        S.append(value)
    elif inputLine[0:3] == "ADD":
        input1 = stackpop("ADD")
        input2 = stackpop("ADD")
        variables = checkInput(input1, input2)
        S.append(variables.pop() + variables.pop())
    elif inputLine[0:3] == "SUB":
        input1 = stackpop("SUB")
        input2 = stackpop("SUB")
        variables = checkInput(input1, input2)
        S.append(variables.pop() - variables.pop())
    elif inputLine[0:4] == "MULT":
        input1 = stackpop("MULT")
        input2 = stackpop("MULT")
        variables = checkInput(input1, input2)
        S.append(variables.pop() * variables.pop())
    elif inputLine[0:6] == "ASSIGN":
        val = stackpop("ASSIGN")
        var = stackpop("ASSIGN")
        map[var] = val
        S.append(var)
    elif inputLine[0:5] == "PRINT":
        var = stackpop("PRINT")
        if var.isdigit():
            print var
        else:
            print map[var]
    else:
        print "Error for operator: " + inputLine
        sys.exit()