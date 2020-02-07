import collections


def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    if answer == '':
        return participant[-1]

    return answer


"""
solution_2 는 중복값도 지우기 때문 쓰면 안됨
"""


# def solution_2(participant, completion):
#     participant.sort()
#     completion.sort()
#     result = (set(participant) - set(completion))
#     print(result, type(result))
#     return list(result)[0]


def solution_3(participant, completion):
    result = collections.Counter(participant) - collections.Counter(completion)
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    print(result, type(result))
    return list(result)[0]


if __name__ == '__main__':
    print(solution_3(
        ['leo', 'kiki', 'eden'],
        ['eden', 'kiki']
    ))

    print(solution_3(
        ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
        ['josipa', 'filipa', 'marina', 'nikola']
    ))

    print(solution_3(
        ["mislav", "stanko", "mislav", "ana"],
        ["stanko", "ana", "mislav"]
    ))

    # c = collections.Counter(['leo', 'kiki', 'eden'])
    # print(c)
    # c2 = collections.Counter(['eden', 'kiki'])
    # print(c2)
    # res = c - c2
    # print(res)
    #
    # target = ['leo', 'kiki', 'eden']
    # target2 = ['eden', 'kiki']
    # result = set(target) - set(target2)
    # print(result)
    # print(result.pop())
