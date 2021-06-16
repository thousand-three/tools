'''
@application: 清空指定文件或文件夹下文件的内容
@author: 三千
@create time: 2021-6-16
@edit time: 
@editor:

'''
import sys
import os

def ClearFile(path):
    if os.stat(path).st_size != 0:
        with open(path, "w", encoding="utf-8") as file:
            file.truncate(0)

def ClearDir(path):
    for root,dirs,files in os.walk(path):
        for f in files:
            ClearFile(os.path.join(root,f))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        if os.path.isdir(path):
            ClearDir(path)
        elif os.path.isfile(path):
            ClearFile(path)
        else:
            print("parameter is incorrect")
    else:
        print("the number of parameter is incorrect")
