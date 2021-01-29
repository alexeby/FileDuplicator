import os


def get_file_name(file_dir: str):
    files = os.listdir(file_dir)
    if len(files) <= 0:
        raise OSError(f'No files exist in the directory {file_dir}')
    return files[0]


def iterate_file(file: str, iter: int):
    file_name, file_type = file.split('.')
    file_name = file_name + '(' + str(iter) + ')'
    return file_name + '.' + file_type


def duplicate_file(original_file_dir: str, copy_file_dir: str, num_copies: int):
    original_file_name = get_file_name(original_file_dir)
    original_file_path = original_file_dir + original_file_name

    with open(original_file_path, 'r') as original_file:
        for i in range(num_copies):
            copy_file_path = copy_file_dir + iterate_file(original_file_name, i + 1)
            with open(copy_file_path, 'w') as copy_file:
                for line in original_file:
                    copy_file.write(line)
                copy_file.close()
                original_file.seek(0)
        original_file.close()