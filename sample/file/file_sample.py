import os


def ret_path_to_file_info(path: str, returnTo: str = ''):
    base = os.path.basename(path)  # imWaybill_LP00165786832283.pdf
    file = os.path.splitext(base)  # ('imWaybill_LP00165786832283', '.pdf')

    if returnTo == 'filename':
        return file[0]

    elif returnTo == 'ext':
        return file[1]

    return file[0], file[1]


class FileExtensionError(OSError):
    pass


def is_file_ext_allowed(extension: str, allowList: list):
    if extension not in allowList:
        raise FileExtensionError('{} is not allowed'.format(extension))

    return True


def get_files_in_dir(path: str):
    files = os.listdir(path)
    return files


if __name__ == '__main__':
    path = '/home/api/media/adjustment/sample.txt'
    file_ext = ret_path_to_file_info(path, 'ext')
    file_name = ret_path_to_file_info(path, 'filename')

    print(file_name, file_ext)

    try:
        is_file_ext_allowed(file_ext, ['.xls', '.xlsx'])

    except Exception as e:
        print(e.__str__())

    path = '/home/python_test/sample/file'
    files = get_files_in_dir(path)
    print(files)
