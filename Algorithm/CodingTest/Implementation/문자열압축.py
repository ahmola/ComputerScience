import sys

def solution(s):
    result = float("inf")
    length = len(s)

    if length == 1:
        return 1

    # 문자열 길이 1부터
    for i in range(1, length):
        prev = s[:i]
        sub = ""
        j = i
        while j < length+i:
            count = 1
            while prev == s[j:j+i]:
                count += 1
                j += i

            if count > 1:
                sub += str(count)+prev
            elif count == 1:
                sub += prev

            prev = s[j:j+i]
            j += i

        # print(sub, i)
        result = min(result, len(sub))
    return result

s = sys.stdin.readline().strip()
print(solution(s))