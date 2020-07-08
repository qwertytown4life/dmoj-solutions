import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from functools import lru_cache

pieces = int(input())
people = int(input())

@lru_cache(maxsize=10**9)
def pi_day(pec, pep, mi):
    if pep == 1 or pec == pep:
        return 1

    t = 0
    for i in range(mi, int(pec / pep) + 1):
        t += pi_day(pec - i, pep - 1, i)
    return t
  
print(pi_day(pieces, people, 1))
