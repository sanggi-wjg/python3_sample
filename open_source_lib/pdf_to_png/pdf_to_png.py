import os

import pdf2image
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError

from open_source_lib.pdf_to_png.pdf_download_sample import ret_path_to_file_info

SAMPLE_PDF = './sample.pdf'
SAMPLE_WAYBILL_PDF = './sample_waybill.pdf'

"""
Required : 
    yum install poppler-utils
    pip install pdf2image

https://github.com/Belval/pdf2image
"""


def pdf_to_convert(pdfPath: str, savePath: str, saveFileName: str, extension = 'png'):
    try:
        if not os.path.isfile(pdfPath):
            raise FileNotFoundError('Can not find waybill pdf')

        # filename = ret_path_to_file_info(saveFileName, 'filename')
        images = pdf2image.convert_from_path(pdf_path = pdfPath)

        for img in images:
            path = savePath + saveFileName + '.' + extension

            if os.path.isfile(path):
                print('[-] ' + path + ' is exist')
                continue

            print('@@ ' + path + ' @@ save')
            img.save(path, extension)

        # for i, images in enumerate(images):
        #     images.save(filename + str(i) + '.png', 'PNG')

    except FileNotFoundError as e:
        print('FileNotFoundError (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)

    except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError) as e:
        print('pdf2image Error (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)

    except Exception as e:
        print('Exception (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)


if __name__ == '__main__':
    pdf_to_convert(SAMPLE_WAYBILL_PDF, '/home/python_test/open_source_lib/pdf_to_png/', 'sample_waybill')
