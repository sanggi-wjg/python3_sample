import os

import pdf2image
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError

from open_source_lib.pdf_to_png.pdf_download_sample import ret_path_to_file_info

SAMPLE_WAYBILL_PDF = './sample_waybill.pdf'

"""
Required : 
    yum install poppler-utils
    pip install pdf2image

https://github.com/Belval/pdf2image
"""

if __name__ == '__main__':

    try:
        if not os.path.isfile(SAMPLE_WAYBILL_PDF):
            raise FileNotFoundError('Can not find waybill pdf')

        filename = ret_path_to_file_info(SAMPLE_WAYBILL_PDF, 'filename')
        images = pdf2image.convert_from_path(pdf_path = SAMPLE_WAYBILL_PDF)
        print(images)

        for i, images in enumerate(images):
            images.save(filename + str(i) + '.png', 'PNG')

    except FileNotFoundError as e:
        print('FileNotFoundError (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)

    except (PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError) as e:
        print('pdf2image Error (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)

    except Exception as e:
        print('Exception (LINE) :', e.__traceback__.tb_lineno, ' (MSG) : ', e)
