def solution(clothes):
    answer = 1
    data = dict()

    for c, k in clothes:
        if k in data.keys():
            temp = data.get(k)
            temp.append(c)
            data.__setitem__(k, temp)
        else:
            data.__setitem__(k, [c])

    # print('data:', data, ' key len : ', len(data.keys()))
    for k, v in data.items():
        answer = answer * (len(v) + 1)

    return answer - 1


if __name__ == '__main__':
    print(solution(
        [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    ))

    print(solution(
        [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["blue_dro", "underwear"]]
    ))

    print(solution(
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    ))
