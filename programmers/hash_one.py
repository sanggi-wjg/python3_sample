
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


if __name__ == '__main__':
    print(solution(
        ['leo', 'kiki', 'eden'],
        ['eden', 'kiki']
    ))

    print(solution(
        ['leo', 'leo', 'kiki'],
        ['leo', 'kiki']
    ))

    print(solution(
        ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
        ['josipa', 'filipa', 'marina', 'nikola']
    ))

    print(solution(
        ["mislav", "stanko", "mislav", "ana"],
        ["stanko", "ana", "mislav"]
    ))
