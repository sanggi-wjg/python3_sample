def solution(array, commands):
    answer = []

    for c1, c2, c3 in commands:
        temp = array[c1 - 1:c2]
        answer.append(sorted(temp)[c3 - 1])

    return answer


if __name__ == '__main__':
    ans = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    print(ans)
