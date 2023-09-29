import os


def file_info(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    return path, name, extension


if __name__ == '__main__':
    file_p = '/Users/dima4/Documents/GeekBrains/Полезные_ссылки.docx'
    print(file_info(file_p))
