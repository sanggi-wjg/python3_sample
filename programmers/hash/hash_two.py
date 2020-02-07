def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)):
        if any(phone_book[i] in p for p in phone_book[i + 1:len(phone_book)]):
            return False

    return answer


if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
    print(solution(["123", "456", "789"]))
    print(solution(["12", "123", "1235", "567", "88"]))

    print(list(p for p in ["12", "123", "1235", "567", "88"]))
    print(p for p in ["12", "123", "1235", "567", "88"])
