import base64
import hashlib


def md5_hash(text: str, encodeType = 'utf-8'):
    m = hashlib.md5(text.encode(encodeType))

    return m.digest()


def base64_encode(text: bytes, decodeType = 'utf-8'):
    b = base64.encodebytes(text)
    return b.decode(decodeType).replace('\n', '')


sample_list = [
    'TA:taobao',
    'JAMY:wpdlal',
    '100bang:qorqkd'
]

for s in sample_list:
    a = md5_hash(s)
    b = base64_encode(a)
    print(b)
