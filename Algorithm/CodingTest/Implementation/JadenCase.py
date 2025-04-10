import sys

def solution(s):
    result = ""
    make_upper = True
    for char in s:
        if make_upper:
            result += char.upper()
        else:
            result += char.lower()
        make_upper = (char == ' ')
    return result

s = sys.stdin.readline()
print(solution(s))