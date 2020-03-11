import hashlib


def ret_hash(text: str, hashType = 'sha-256', encodeType = 'utf-8'):
    salt = 'thisissalt'

    if hashType == 'sha-256':
        result = hashlib.sha256((salt + text).encode(encodeType)).hexdigest()

    else:
        raise TypeError('Hash Type not defined')

    return result


if __name__ == '__main__':
    print(ret_hash('qlalfqjsgh'))

