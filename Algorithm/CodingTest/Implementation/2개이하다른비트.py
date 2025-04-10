import sys

# def solution(numbers):
#     result = []
#     for num in numbers:
#         if num % 2 == 0:
#             result.append(num + 1)
#         else:
#             # 홀수일 때: num에 1을 더하고, ^(XOR) 연산으로 차이 비트 구하고
#             # 거기서 >>2 해서 1만큼 왼쪽 쉬프트한 걸 더함
              # 라고 하는데 이걸 도데체 어떤 새끼가 생각해내냐;;
#             b = (num ^ (num + 1)) >> 2
#             result.append(num + 1 + b)
#     return result

def solution(numbers):
    bits = [format(num, 'b') for num in numbers]
    result = []

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            result.append(numbers[i]+1)
            continue
        count = 3
        number = numbers[i]
        while count > 2:
            count = 0
            number += 1
            bit = format(number, 'b')
            len_bit, len_biti = len(bit), len(bits[i])

            k = 0
            if len_bit > len_biti:
                while k in range(len_bit-len_biti):
                    if bit[k] != 0:
                        count += 1
                    k += 1

            for j in range(len_biti):
                if bit[j+k] != bits[i][j]:
                    count += 1
                    if count > 2:
                        break
        result.append(number)

    return result

numbers = list(map(int, sys.stdin.readline().split()))
print(solution(numbers))