'''
@application: 将文件内大写字母转为小写
@author: 三千
@create time: 2021-8-4
@edit time: 
@editor:

'''

import sys
import os

def ConvertFile(path):
    new_content = ""
    if os.stat(path).st_size != 0:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.lower()
                new_content += line
        with open(path,'w',encoding="utf-8") as file:
            file.write(new_content)
            

def ConvertDir(path):
    for root,dirs,files in os.walk(path):
        for f in files:
            ConvertFile(os.path.join(root,f))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        if os.path.isdir(path):
            ConvertDir(path)
        elif os.path.isfile(path):
            ConvertFile(path)
        else:
            print("parameter is incorrect")
    else:
        print("the number of parameter is incorrect")