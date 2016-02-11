import sys

dummyText = "This is Sparta!"

def changeString(string):
    print "Changing NOW"
    string = "Changed this string"

# substring = dummyText[5:]

# print dummyText
# print substring

# lst = []
# lst.append(dummyText)
# lst.append(substring)

# for tmp in lst:
#     print tmp

print "About to change the string: ", dummyText
changeString(dummyText)
print dummyText

# def interpret(argument):
#     switcher = {
#         "PUSH": print "PUSHED",
#         "ADD": print "ADDED",
#         "ASSIGN": print "ASSIGNED",
#     }
#     return switcher.get(argument, "nothing")

# interpret('PUSH')

# def PUSH(input):
#     value = input

# def checkInput(input1, input2):
#     if isinstance(input1, str):
#         if input1.isdigit():
#             input1 = int(input1)
#         else:
#             input1 = int(map[input1])
#     if isinstance(input2, str):
#         if input2.isdigit():
#             input2 = int(input2)
#         else:
#             input2 = int(map[input2])



#     elif line[0:3] == "ADD":
#         var1 = popstack("ADD")
#         var2 = popstack("ADD")


#         if isinstance(var1, str):
#             if var1.isdigit():
#                 var1 = int(var1)
#             else:
#                 var1 = int(map[var1])
#         if isinstance(var2, str):
#             if var2.isdigit():
#                 var2 = int(var2)
#             else:
#                 var2 = int(map[var2])
#         stack.append(var1 + var2)