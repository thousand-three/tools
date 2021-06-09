'''
@application: 统计指定文件或文件夹下的文件行数
@author: 三千
@create time: 2021-5-7
@edit time: 
@editor:

'''

import os
import sys


def CombinPath(str_path):
    #判断不同的系统路径，windows系统为'\\'，Linux为'/'
    if '\\' in str_path or '/' in str_path:
        return str_path
    elif str_path == "":
        path = os.path.split(os.path.realpath(__file__))[0]
        return path
    else:
        path = os.path.split(os.path.realpath(__file__))[0]
        if '\\' in path:
            path = path + '\\' + str_path
            return path
        if '/' in path:
            path = path + '/' + str_path
            return path


def DirsCountLine(path):
    count = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            if '\\' in root:
                count = count + FileCountLine(root+'\\'+f)
            if '/' in root:
                count = count + FileCountLine(root+'/'+f)
    return count


def FileCountLine(path):
    f = open(path, mode='r', encoding='UTF-8')
    count = 0
    for index, line in enumerate(f):
        count = count + 1
    return count


if __name__ == "__main__":
	if len(sys.argv) == 2:
		str_path = sys.argv[1]
	else:
		str_path = input("请输入：文件或文件夹的绝对路径，若为文件名则为当前目录下指定文件，若为空则为当前目录所有文件\n")
	path = CombinPath(str_path)
	if os.path.isfile(path):
		count = FileCountLine(path)
		print(count)
	elif os.path.isdir(path):
		count = DirsCountLine(path)
		print(count)
	else:
		print("the path not exists")
