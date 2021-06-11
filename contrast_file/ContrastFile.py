'''
@application: 对比指定文件或文件夹内文件的异同
@author: 三千
@create time: 2021-6-10
@edit time: 
@editor:

'''

import sys
import os


def ContrastFile(path_1, path_2):
    file_1 = open(path_1, "r", encoding="UTF-8")
    file_2 = open(path_2, "r", encoding="UTF-8")
    file_1_list = []
    file_2_list = []
    for file_1_line in file_1.readlines():
        file_1_list.append(file_1_line)
    for file_2_line in file_2.readlines():
        file_2_list.append(file_2_line)
    file_1_count = 0
    file_2_count = 0
    while file_1_count < len(file_1_list) or file_2_count < len(file_2_list):
        file_1_line = file_1_list[file_1_count].replace(" ", "")
        file_2_line = file_2_list[file_2_count].replace(" ", "")
        if file_1_line != file_2_line:
            if file_1_line == "\n":
                file_1_count += 1
                continue
            elif file_2_line == "\n":
                file_2_count += 1
                continue
            else:
                break
        if file_1_count < len(file_1_list):
            file_1_count += 1
        if file_2_count < len(file_2_list):
            file_2_count += 1
    if file_1_count < len(file_1_list) or file_2_count < len(file_2_list):
        return file_1_count, file_2_count
    else:
        return -1, -1


def ContrastDir(path_1, path_2):

    result = []

    path_1_dict = {}
    path_2_dict = {}

    for root, dirs, files in os.walk(path_1):
        for file in files:
            path_1_dict[file] = root

    for root, dirs, files in os.walk(path_2):
        for file in files:
            path_2_dict[file] = root

    bigger_dict = path_1_dict if len(path_1_dict) < len(path_2_dict) else path_2_dict
    smaller_dict = path_2_dict if len(path_1_dict) < len(path_2_dict) else path_1_dict

    for key in smaller_dict:
        if key in bigger_dict.keys():
            position_1, position_2 = ContrastFile(os.path.join(bigger_dict[key], key), os.path.join(smaller_dict[key], key))
            if position_1 == -1 and position_2 == -1:
                result.append("the two file [{0}] is same".format(key))
            else:
                result.append("the two file [{0}] is different at line {1} and line {2}".format(key, position_1 + 1, position_2 + 1))
        else:
            result.append("there is only one file [{0}] at {1}".format(key,smaller_dict[key]))

    for key in bigger_dict:
        if key not in smaller_dict.keys():
            result.append("there is only one file [{0}] at {1}".format(key,bigger_dict[key]))
    return result


def DisplayDirResult(result):
    for r in result:
        print(r)


def DisplayFileResult(position_1, position_2):
    if position_1 == -1 and position_2 == -1:
        print("the two file is same")
    else:
        print("the two file is different at line {0} and line {1}".format(position_1 + 1, position_2 + 1))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        path_1 = sys.argv[1]
        path_2 = sys.argv[2]
        if os.path.isfile(path_1) and os.path.isfile(path_2):
            position_1, position_2 = ContrastFile(path_1, path_2)
            DisplayFileResult(position_1, position_2)
        elif os.path.isdir(path_1) and os.path.isdir(path_2):
            result = ContrastDir(path_1, path_2)
            DisplayDirResult(result)
        else:
            print("the type of parameter is incorrect")

    else:
        print("the number of parameter is incorrect")
