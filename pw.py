from collections import defaultdict
cons = defaultdict(set)

with open('password.txt', 'r') as _f:
    for line in _f:
        pw = []
        line.rstrip('\n')
        pw[:0] = line

        cons[pw[0]].add(pw[1])
        cons[pw[0]].add(pw[2])
        cons[pw[1]].add(pw[2])
        cons[pw[2]].add(None)

result = dict()

for letter, after_letters in cons.items():
    result[letter] = len(after_letters)

for i, j in sorted(result.items(), key = lambda x:(x[1],x[0]), reverse = True):
    print(i, j, end="")
print('\n')