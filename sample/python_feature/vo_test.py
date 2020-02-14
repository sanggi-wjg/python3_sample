class StdClass:
    pass


if __name__ == '__main__':
    # _Temp = StdClass()
    # _Temp.abc = '123'
    #
    # _Temp2 = StdClass()
    # _Temp2.gdf = '456'
    #
    # print(_Temp)
    # print(_Temp.abc)
    #
    # print(_Temp2)
    # print(_Temp2.gdf)

    stockItem = StdClass()
    stockItem.productName = 'Warehouse Moving'
    stockItem.productUnitPrice = '100000'

    stock = list()
    stock.append(stockItem)

    print(stock)
    print(stock[0])
    print(stock[0].productName)
