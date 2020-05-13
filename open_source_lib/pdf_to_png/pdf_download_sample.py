import os
import urllib.request

import urllib.parse
import urllib.error


def ret_url_parse(url: str):
    """
    url : 'http://importwaybillfile.oss-cn-zhangjiakou.aliyuncs.com/imWaybill_LP00165786832283.pdf?Expires=1584367242&OSSAccessKeyId=LTAI5pw3uQoCjCRE&Signature=fLMr2YH9%2BJRNXWjP0A5zTEp%2B4P0%3D'

    sheme : http
    netlot : importwaybillfile.oss-cn-zhangjiakou.aliyuncs.com
    path : /imWaybill_LP00165786832283.pdf
    params : ''
    query : Expires=1584367242&OSSAccessKeyId=LTAI5pw3uQoCjCRE&Signature=fLMr2YH9%2BJRNXWjP0A5zTEp%2B4P0%3D
    fragment : ''
    """
    return urllib.parse.urlparse(url)


def ret_path_to_file_info(path: str, returnTo: str):
    base = os.path.basename(path)  # imWaybill_LP00165786832283.pdf
    file = os.path.splitext(base)  # ('imWaybill_LP00165786832283', '.pdf')

    if returnTo == 'filename':
        return file[0]
    elif returnTo == 'ext':
        return file[1]

    return file[0], file[1]


def pdf_save(pdfUrl: str, pdfPath: str, fileName: str):
    try:
        if not os.path.isdir(pdfPath):
            raise NotADirectoryError(pdfPath + ' Is Not a Directory')

        path = pdfPath + fileName + '.pdf'
        result = urllib.request.urlretrieve(pdfUrl, path)
        print(result[1])
        # print(result[1].__doc__)

        # urlParse = ret_url_parse(pdfUrl)
        # print(urlParse)
        # path = urlParse[2]
        #
        # result = ret_path_to_file_info(path, 'filename')
        # print(result)

    except urllib.error.HTTPError as e:
        print('urllib.HTTPError Error (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)

    except urllib.error.URLError as e:
        print('urllib.URLError Error (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)

    except NotADirectoryError as e:
        print('NotADirectoryError Error (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)

    except Exception as e:
        print('Exception Error (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)
        # raise e


if __name__ == '__main__':
    SAMPLE_PDF_IMAGE_URL = 'http://www.africau.edu/images/default/sample.pdf'
    SAMPLE_PDF_IMAGE_URL_2 = 'http://importwaybillfile.oss-cn-zhangjiakou.aliyuncs.com/imWaybill_LP00165786832283.pdf?Expires=1584367242&OSSAccessKeyId=LTAI5pw3uQoCjCRE&Signature=fLMr2YH9%2BJRNXWjP0A5zTEp%2B4P0%3D'
    SAMPLE_URL = 'http://cg-trade.cainiao.com/tfscom/TB1YoZwsAKWBuNjy1zjXXcOypXa.tfsprivate.pdf'

    try:
        pdf_save(
            pdfUrl = SAMPLE_URL,
            pdfPath = '/home/python_test/open_source_lib/pdf_to_png/',
            fileName = 'sample_waybill'
        )

    except Exception as e:
        print('@@@ Exception Error (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)
