import sys
text = input()
temp = input()

for i in range(len(temp)):
    if temp in text: print('yes'), sys.exit()
    temp = list(temp)
    frontChar = temp[0]
    temp.pop(0)
    temp.append(frontChar)
    temp = ''.join(temp)

print('no')
