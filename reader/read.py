#!/usr/bin/python3

#read files
import os
import os.path
import pickle

def get_rule(rulefile):
    f=open(rulefile)
    str=f.read()
    rule=str.split(sep=",",maxsplit=9)
    return rule

def read(dir,lang,type):    

    """获取指定目录及其子目录下的 py 文件路径
    说明：
    l 用于存储找到的 py 文件路径 get_file 函数，递归查找并存储 py 文件路径于 l"""
    l = []
    filetype=get_rule(rulefile)[0]

    def get_file(path,l):
        
        fileList = os.listdir(path)   #获取path目录下所有文件
        for filename in fileList:
            pathTmp = os.path.join(path,filename)   #获取path与filename组合后的路径
            if os.path.isdir(pathTmp):   #如果是目录
                get_file(pathTmp,l)        #则递归查找
            elif filename.split(sep=".")[-1].upper()==filetype:   #不是目录,则比较后缀名
                l.append(pathTmp)
    path =dir.strip()
    get_py(path,l)
    print('在%s目录及其子目录下找到%d个待翻译文件\n分别为：\n'%(path,len(l)))
    for filepath in l:
        print(filepath+'\n')
    pickle_file=open("%s\\file.trf",%(HTD))
    pickle.dump(l,pickle_file)
    pickle_file.close()
    return l