def solution(numbers):
    numbers = list(map(str, numbers))
    # 자릿수 제한이 3자리까지이므로 3자리까지만 비교하면 된다.
    numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(numbers)))
print(solution(['6', '10', '2']))