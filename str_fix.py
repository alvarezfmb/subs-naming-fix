import os
import sys

path = input('Enter path of folder to organize. In case you do not enter anything, current folder will be choosed.')

if not os.path.exists(path):
    path = os.getcwd().strip()
    ans = input('Current directory has been choosed. Do you wish to continue? [Y/N]')
    if ans.upper() != 'Y':
        sys.exit(0)

file_list = os.listdir(path)

for i, file in enumerate(file_list):
    if i % 2 == 0:
        print(os.path.splitext(file)[0])

ans = input('Folder will look like this. Is it OK? [Y/N]')

if ans.upper() != 'Y':
    sys.exit(0)

old_names = []
new_names = []

for i, filename in enumerate(file_list):
    name = os.path.join(path, filename)
    if i % 2 == 0:
        new_names.append(name)
    else:
        old_names.append(name)

for num, file in enumerate(old_names):
    filename_old, file_extension_old = os.path.splitext(file)
    filename_new, file_extension_new = os.path.splitext(new_names[num])
    os.rename(filename_old + file_extension_old, filename_new + file_extension_old)
