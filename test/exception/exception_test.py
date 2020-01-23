class HttpError(Exception):
    """ Http Exceptions """
    pass


class HttpRequestError(HttpError):
    """ Raised When http request is failed """
    pass


class HttpResponseError(HttpError):
    """ Raised When http response is failed """
    pass


def get_exception_msg(code: int, *args) -> str:
    if not code:
        raise TypeError('Empty Code')

    exception_msg = {
        '1000': '{} is empty.',
        '1010': 'Parameter is empty.',
        '1020': '{} is empty. So {}.'
    }

    try:
        sfCnt = exception_msg[str(code)].count('{}')

        if sfCnt >= 1:

            if sfCnt == len(args):
                return exception_msg[str(code)].format(*{ arg for arg in args })
            else:
                return exception_msg[str(code)]

            # elif sfCnt >= len(args):
            #     return '[Warning: Insufficient Arguments] ' + exception_msg[str(code)]
            #
            # else:
            #     return '[Warning: Excessive Arguments]' + exception_msg[str(code)]

        else:
            return exception_msg[str(code)]

            # if args:
        #     # if len(args) == 1:
        #     #     return exception_msg[str(code)].format(args[0])
        #     # elif len(args) == 2:
        #     #     return exception_msg[str(code)].format(args[0], args[1])
        #     # else:
        #     return exception_msg[str(code)].format(*{ arg for arg in args })
        #
        # else:
        #     return exception_msg[str(code)]

    except KeyError:
        return 'Invalid Exception Msg Code : ' + str(code)


if __name__ == '__main__':

    try:
        # raise HttpResponseError
        # raise HttpResponseError('123')
        # raise ValueError

        print('[1-lack]', get_exception_msg(1000))
        print('[2-ok]', get_exception_msg(1000, 'Hello'))
        print('[3-ex]', get_exception_msg(1000, 'Hello', 'World'))

        print('[4-ok]', get_exception_msg(1010))
        print('[5-ex]', get_exception_msg(1010, 'Hello'))
        print('[6-ex]', get_exception_msg(1010, 'Hello', 'World'))

        print('[7-lack]', get_exception_msg(1020))
        print('[8-lack]', get_exception_msg(1020, 'Hello'))
        print('[9-ok]', get_exception_msg(1020, 'Hello', 'World'))

    except HttpResponseError as hre:
        print('[Error] : ' + hre.__str__())

    except ValueError as ve:
        print('[Error] : ' + ve.__str__())

    except BaseException as be:
        print('[Error] : ' + be.__str__())
