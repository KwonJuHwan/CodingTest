from collections import Counter
from itertools import combinations, permutations

a = ["a", "b", "c", "d", "e"]

join_a = "".join(a)
print(join_a)
print(Counter(a)["b"])

for i in combinations(a, 2):
    print(i)

print("****************")
k = 0
for i in permutations(a, 2):
    print(k, i)
    k += 1
