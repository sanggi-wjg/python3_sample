import base64
import hashlib


def md5_hash(data: str, encode_type = 'utf-8') -> bytes:
    m = hashlib.md5(data.encode(encode_type))
    return m.digest()


def base64_encode(data: bytes, decode_type = 'utf-8') -> str:
    b = base64.encodebytes(data)
    return b.decode(decode_type)


if __name__ == '__main__':
    # keyword = '<RequestOrder><clientID>K210306214<\/clientID><logisticProviderID>YTO<\/logisticProviderID><customerId>K210306214<\/customerId><txLogisticID>K210306214TJ157904280167CC8<\/txLogisticID><tradeNo>1<\/tradeNo><mailNo><\/mailNo><totalServiceFee>0.0<\/totalServiceFee><codSplitFee>0.0<\/codSplitFee><orderType>5<\/orderType><serviceType>0<\/serviceType><flag>0<\/flag><sender><name>Motive Street<\/name><postCode>14441<\/postCode><phone>1<\/phone><mobile>1<\/mobile><prov>上海<\/prov><city>上海市<\/city><address>경기도 부천시 오정동 774-1 (주)동방  3층.<\/address><\/sender><receiver><name>杨云龙<\/name><postCode>046011<\/postCode><phone>000000<\/phone><mobile>19981494332<\/mobile><prov>山西省<\/prov><city>长治市,城区<\/city><address>山西省长治市城区 东街街道安康小区21号楼2单元1302室<\/address><\/receiver><sendStartTime><\/sendStartTime><sendEndTime><\/sendEndTime><goodsValue>0<\/goodsValue><items><item><itemName>LINE TAPE TRACK PANTS BLKGRN<\/itemName><number>1<\/number><itemValue>32300.00<\/itemValue><\/item><\/items><insuranceValue>0.0<\/insuranceValue><special><\/special><remark><\/remark><\/RequestOrder>0u4z2yaL'
    # keyword = 'spam, spam, and eggs'
    # md = md5_hash(keyword)
    # print(md)
    # db = base64_encode(md)
    # print(db)

    id = 'TA'
    pw = 'taobao'

    a = md5_hash('{}:{}'.format(id, pw))
    b = base64_encode(a)
    print(b)
