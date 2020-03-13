"""
Required XlsxWriter

https://xlsxwriter.readthedocs.io/
https://github.com/jmcnamara/XlsxWriter

이거는 읽는것은 불가하고 쓰기만 가능하다.
성능이 좋단다.
"""
import xlsxwriter


def sample():
    workbook = xlsxwriter.Workbook('sample.xlsx')

    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 20)

    bold = workbook.add_format({ 'bold': True })

    worksheet.write('A1', 'Hello')
    worksheet.write('A2', 'World', bold)

    workbook.close()


if __name__ == '__main__':
    worksheetNames = ['A', 'B', 'C', 'D', 'E']

    workbook = xlsxwriter.Workbook('sample.xlsx')
    bold = workbook.add_format({ 'bold': True })

    for no, name in enumerate(worksheetNames):
        worksheet = workbook.add_worksheet(name = name)
        worksheet.write('A1', 'Hello')
        worksheet.write('A2', 'World', bold)
        worksheet.write('A3', no)

    workbook.close()
