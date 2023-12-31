import os
from pathlib import Path
import csv
import json
import pickle


def folder_getsize(path='.') -> int:
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += folder_getsize(entry.path)
    return result


def get_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return folder_getsize(path)


def folder_info(direct: Path):
    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_folder']
    rows = []
    with (open('folder_info.json', 'w') as f_json,
          open('folder_info.csv', 'w', newline='', encoding='utf-8') as f_csv,
          open('folder_info.pickle', 'wb') as f_pickle
          ):
        for dir_path, dir_name, file_name in os.walk(direct):
            json_data.setdefault(dir_path, {})
            for dir in dir_name:
                size = get_size(dir_path + '/' + dir)
                json_data[dir_path].update({dir: {'size': size, 'file_or_folder': 'folder'}})
                rows.append({'name': dir, 'path': dir_path, 'size': size, 'file_or_folder': 'folder'})
            for fi in file_name:
                size = get_size(dir_path + '/' + fi)
                json_data[dir_path].update({fi: {'size': size, 'file_or_folder': 'file'}})
                rows.append({'name': fi, 'path': dir_path, 'size': size, 'file_or_folder': 'file'})
            print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(json_data)}', f_pickle)


if __name__ == '__main__':
    folder_info(Path('../sem_8'))
