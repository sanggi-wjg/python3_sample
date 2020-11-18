import pandas as pd

file = open('2020_반기보고서_02_손익계산서_연결_20201117.txt', encoding = 'utf-8')

datalist = { }

for i, line in enumerate(file.readlines()):
    if i == 0: continue
    d = line.split('\t')
    d.remove('')
    d.remove('\n')

    stock_code = d[1].replace('[', '').replace(']', '')

    if stock_code not in datalist.keys():
        datalist.setdefault(stock_code, {
            'stock_name': d[2],
        })
    else:
        if d[11] not in datalist[stock_code].keys():
            # (당기 3개월 / 당기 누적 / 전기 3개월 / 전기 누적)
            name = d[11].replace('[abstract]', '').replace(' ', '').strip()
            datalist[stock_code][name] = (d[12], d[13], d[14], d[15])

first_stock_code = list(datalist.keys())[0]
index_sample = list(datalist[first_stock_code].keys())
index_sample.remove('stock_name')

dataframe = pd.DataFrame(
    index = index_sample,
    columns = [item['stock_name'] for key, item in datalist.items()],
)

for key, item in datalist.items():
    stock_name = item['stock_name']

    for k, v in item.items():
        if k is not 'stock_name':
            dataframe[stock_name][k] = v[0]
