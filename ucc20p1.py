da_len = int(input())
string1 = input()
string2 = input()
counter = 0
for i in range(da_len):
    if string1[i] == string2[i] == '0':
        counter += 1

print(counter)
