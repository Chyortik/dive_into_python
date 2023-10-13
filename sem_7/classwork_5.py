from classwork_4 import make_files


def new_make_file(extensions: dict):
    for extension, count in extensions.items():
        make_files(extension=extension, count=count)



if __name__ == '__main__':
    data = {
        'txt': 1,
        'zip': 2,
    }
    new_make_file(data)