import sys
sys.stdin.readline
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_score = 0
word = sys.stdin.readline()
for i in range(26):
    alpha_score += ((word.count(alphabet[i])) * (i + 1))
print(alpha_score)
