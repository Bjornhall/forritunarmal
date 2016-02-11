import sys

# Prints error message if stack is empty, else pops the stack and returns the result
def popstack(operator):
    if not stack:
        print "Error for operator: " + operator
        sys.exit()
    else:
        return stack.pop()

stack = []
map = {}

# loops through each line and responds to the operator in it
for line in sys.stdin:
    line = line.rstrip()
    if line[0:4] == "PUSH":
        var = line[5:]
        stack.append(var)
    elif line[0:3] == "ADD":
        var1 = popstack("ADD")
        var2 = popstack("ADD")
        if isinstance(var1, str):
            if var1.isdigit():
                var1 = int(var1)
            else:
                var1 = int(map[var1])
        if isinstance(var2, str):
            if var2.isdigit():
                var2 = int(var2)
            else:
                var2 = int(map[var2])
        stack.append(var1 + var2)
    elif line[0:3] == "SUB":
        var1 = popstack("SUB")
        var2 = popstack("SUB")
        if isinstance(var1, str):
            if var1.isdigit():
                var1 = int(var1)
            else:
                var1 = int(map[var1])
        if isinstance(var2, str):
            if var2.isdigit():
                var2 = int(var2)
            else:
                var2 = int(map[var2])
        stack.append(var2 - var1)
    elif line[0:4] == "MULT":
        var1 = popstack("MULT")
        var2 = popstack("MULT")
        if isinstance(var1, str):
            if var1.isdigit():
                var1 = int(var1)
            else:
                var1 = int(map[var1])
        if isinstance(var2, str):
            if var2.isdigit():
                var2 = int(var2)
            else:
                var2 = int(map[var2])
        stack.append(var1 * var2)
    elif line[0:6] == "ASSIGN":
        val = popstack("ASSIGN")
        var = popstack("ASSIGN")
        map[var] = val
        stack.append(var)
    elif line[0:5] == "PRINT":
        var = popstack("PRINT")
        if var.isdigit():
            print var
        else:
            print map[var]
    else:
            print "Error for operator: " + line
            sys.exit()
