import sys

def solution(s):
    opened = 0
    i = 0
    length = len(s)
    while i < length:
        if opened <= 0 and s[i] == ")":
            return False
        elif s[i] == "(":
            opened += 1
        elif opened > 0 and s[i] == ")":
            opened -= 1
        i += 1

    if opened == 0:
        return True
    else:
        return False


s = list(sys.stdin.readline().strip())
print(solution(s))