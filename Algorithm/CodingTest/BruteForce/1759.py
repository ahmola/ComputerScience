from itertools import combinations

l, c = map(int, input().split(" "))
chars = list(map(str, input().split(" ")))

v_chars = []
c_chars = []
for c in chars:
    if c in ["a", "e", "i", "o", "u"]:
        v_chars.append(c)
    else:
        c_chars.append(c)

result = []

for i in range(1, l):
    if 1 <= i <= len(v_chars) and 2 <= l-i <= len(c_chars):
        for v_comb in combinations(v_chars, i):
            for c_comb in combinations(c_chars, l-i):
                secret = []
                secret.append(list(v_comb))
                secret.append(list(c_comb))
                secret = sum(secret, [])
                secret.sort()
                secret_chars = "".join(map(str, secret))
                if secret_chars not in result:
                    result.append(secret_chars)

result.sort()
for r in result:
    print(r)                