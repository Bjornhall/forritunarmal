import sys

dummyText = "This is Sparta!"
substring = dummyText[5:]
print dummyText
print substring

lst = []
lst.append(dummyText)
lst.append(substring)

for tmp in lst:
    print tmp