import os


current_dir = os.getcwd()
print(current_dir)
# tmp_path = os.path.join(current_dir, "Homeworks", "tmp", "test_2")
# print(tmp_path)

def get_files_from_dir(base_dir, full_path=True):
    list_dir = os.listdir(base_dir)
    files = []
    for file_object in list_dir:
        path_object = os.path.join(base_dir, file_object)
        if os.path.isfile(path_object):
            files.append(path_object if full_path else file_object)
    return files


# alphabet_files = get_files_from_dir("alphabet")
# print(alphabet_files)
# homeworks_files = get_files_from_dir("Homeworks", full_path=False)
# print(homeworks_files)

# def create_dir(path):
#     try:
#         os.mkdir(path)
#     except FileExistsError:
#         pass


# os.makedirs("test_3_dir/test_4_dir", exist_ok=True)