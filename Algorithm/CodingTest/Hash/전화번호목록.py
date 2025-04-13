def solution(phone_book):
    # 사전순으로
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

print(solution(["123","456","789"]))