def convert_text_to_list(txt: list):
    resultList = []

    for t in txt:
        if t in ['(', ')', '[', ']']:
            resultList.append(t)

    return resultList


def is_balanced(txtList: list):
    stack = []

    for ch in txtList:

        if ch == '(' or ch == '[':
            stack.append(ch)

        elif ch == ')':

            if stack.__len__() != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return 'no'

        elif ch == ']':

            if stack.__len__() != 0 and stack[-1] == '[':
                stack.pop()
            else:
                return 'no'

    if stack.__len__() != 0:
        return 'no'

    return 'yes'


if __name__ == '__main__':
    result = []

    while True:
        inputStr = list(input())
        if inputStr[0] == '.':
            break

        textList = convert_text_to_list(inputStr)
        result.append(is_balanced(textList))

    for r in result:
        print(r)
