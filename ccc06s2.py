word = input()
key = input()
translation = {}
for i in range(len(word)):
    translation[key[i]] = word[i]

end = list(input())

for i in range(len(end)):
    if end[i] in translation:
        end[i] = translation[end[i]]
    else:
        end[i] = '.'

print(''.join(end))
