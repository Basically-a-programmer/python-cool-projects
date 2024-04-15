import os
import shutil
print(os.getcwd())
file_path = input('Give the directory: ')

try:
    os.chdir(file_path)
except FileNotFoundError:
    file_path = input('Give the correct directory: ')

    if os.path.exists(file_path):
        os.chdir(file_path)
    else:
        print(" Warning: The incorrect directory path")

all_file = []

for (root,dirs,files) in os.walk('.', topdown=True):
    each_file = (root,dirs,files)
    all_file.append(each_file)

# print(all_file[0][2])

Vid_img_file = []
pdf_file = []
app_file = []
code_file = []
other_file = []

for files in all_file:
    for each in files[2]:
        file_add = os.path.splitext(each)
        if file_add[1] == '.py':
            code_file.append(file_add)
        elif file_add[1]== '.pdf':
            pdf_file.append(file_add)
        elif file_add[1]=='.exe':
            app_file.append(file_add)
        elif file_add[1]=='.jpeg' or file_add[1]=='.mp4':
            Vid_img_file.append(file_add)
        else:
            other_file.append(file_add)


curr_dirr = os.getcwd()
# print(code_file)
code_path = fr"{curr_dirr}\code_files"
if not os.path.exists(code_path):
    os.mkdir(code_path)
for move_each in code_file:
    try:
        shutil.move(fr"{curr_dirr}\{move_each[0]}{move_each[1]}",fr"{code_path}\{move_each[0]}{move_each[1]}")
    except FileNotFoundError:
        continue
    # print(other_file)
other_path = fr"{curr_dirr}\other_files"
if not os.path.exists(other_path):
    os.mkdir(other_path)
for move_each in other_file:
    try:
        shutil.move(fr"{curr_dirr}\{move_each[0]}{move_each[1]}",fr"{other_path}\{move_each[0]}{move_each[1]}")
    except FileNotFoundError:
        continue
# print(Vid_img_file)
Vid_img_path = fr"{curr_dirr}\Vid_img_files"
if not os.path.exists(Vid_img_path):
    os.mkdir(Vid_img_path)
for move_each in Vid_img_file:
    try:
        shutil.move(fr"{curr_dirr}\{move_each[0]}{move_each[1]}",fr"{Vid_img_path}\{move_each[0]}{move_each[1]}")
    except FileNotFoundError:
        continue
# print(app_file)
app_path = fr"{curr_dirr}\app_file"
if not os.path.exists(app_path):
    os.mkdir(app_path)
for move_each in app_file:
    try:
        shutil.move(fr"{curr_dirr}\{move_each[0]}{move_each[1]}",fr"{app_path}\{move_each[0]}{move_each[1]}")
    except FileNotFoundError:
        continue
# print(pdf_file)
pdf_path = fr"{curr_dirr}\pdf_files"
if not os.path.exists(pdf_path):
    os.mkdir(pdf_path)
for move_each in pdf_file:
    try:
        shutil.move(fr"{curr_dirr}\{move_each[0]}{move_each[1]}",fr"{pdf_path}\{move_each[0]}{move_each[1]}")
    except FileNotFoundError:
        continue