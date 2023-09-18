from pathlib import Path


def change_file_name(count_num: int, extension: str, old_name_limits=None, final_name_part='', dir_name=''):

    dir_path = Path.cwd()
    if dir_name:
        dir_path = dir_path / dir_name
    cnt = 1
    for obj in dir_path.iterdir():
        if obj.suffix == extension:

            old_name = obj.stem
            if old_name_limits is None:
                old_name_limits = [0, len(old_name)]
            start_name = 0 if len(old_name) <= old_name_limits[0] else old_name_limits[0]
            end_name = (len(old_name) - 1) if len(old_name) < old_name_limits[1] else old_name_limits[1]
            new_name = old_name[start_name:end_name]

            number_name = str(cnt) if len(str(cnt)) > count_num else ('0' * (count_num - len(str(cnt))) + str(cnt))
            new_name += final_name_part + number_name + extension
            obj.rename(dir_path / new_name)
            cnt += 1


if __name__ == '__main__':
    change_file_name(4, '.sos', [2, 7], 'OLOLOLO', 'some_trash')
