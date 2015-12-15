#-*- coding:utf-8 -*-
#author:chengchiongwah
#Email:chengchiongwah@gmail.com
#With Python 2.7.3
#vsion:v1.0
# 本功能的实现方法：1）文件的列表表达方式：FileTop = [[0, 0, 0]] 子列表中的第一个数是所在目录层数（从1开始计），第二个数是所在层的文件和文件夹数，第三个数是当前已经遍历了第几个数；2）开始遍历后，第三个数会根据第二个数目每遍历一个文件或文件夹做递减1，等于0时表示已经遍历完成。第一个数也会做递减返回上一层。
import sys,os,time
print "Please input the path of the directory"
Path = raw_input("")
print "┌──" + "Path"
FileTop = [[0, 0, 0]] 
i = 1
k = -2

def PrintFor(FileTop):       #打印格式
    s = ""
    j = []
    h = 1
    Level = FileTop[-1][0]
    while 0 < FileTop[h][0] < Level:
        if FileTop[h][-1] == 1:
            s = s + "  "   
        else:
            s = s + "│ "
        h += 1
    return s

def FileSystem(Path):
    global i, FileTop
    k = -2
    listdir = os.listdir(Path)
    LevelDetail = len(listdir)

    if LevelDetail == 0:                            #所给的目录为空
        FileTop.append([i , LevelDetail, LevelDetail])
        print PrintFor(FileTop) + "└─"
#        print FileTop        
        del FileTop[-1]                             #删掉该目录在列表的信息。
        while FileTop[-1][-1] == 1:                 #删掉目录后后续的子列表信息表示也是最后一个元素
            while FileTop[k][0] == FileTop[-1][0] and FileTop[k][-1] != FileTop[-1][-2]:  #
                k -=1
            del FileTop[ (k + 1): ]                 #因为一路遍历到底了，原路返回并删掉已经遍历
	                                            # 过了的信息，直到还没有遍历的目录
        i = FileTop[-1][0]
        k = -2
#        print FileTop
    
    for lists in listdir:
        NexPth = os.path.join(Path,lists)
        
        if os.path.isdir(NexPth):
            if lists == listdir[0]:     #是该层的第一个文件夹，直接append
                FileTop.append([i, LevelDetail, LevelDetail])
            else:                                      
                i = FileTop[-1][0]         
                FileTop.append([ FileTop[-1][ 0], FileTop[ -1 ][-2], FileTop[ -1 ][ -1 ] - 1])
            if FileTop[-1][-1] == 1:              #是最后一个目录
                print PrintFor(FileTop) + "└─" + lists
#                print FileTop
            else:                                 
                print PrintFor(FileTop) + "├─" + lists
#                print FileTop
            if FileTop[-2][0] == FileTop[-1][0]:
                del FileTop[ -2]
#            print FileTop
            i +=1
            FileSystem(NexPth)
            
        else:
            if lists == listdir[0]:          #是该层的第一个文件
                FileTop.append([i, LevelDetail, LevelDetail])
            else:
                FileTop.append([ FileTop[-1][0], FileTop[-1][-2], FileTop[-1][-1]-1])
            if FileTop[-1][-1] == 1:                    #最后一个文件
                print PrintFor(FileTop) + "└─" + lists
#                print FileTop
                if FileTop[-2][0] == FileTop[-1][0]:    
                    del FileTop[-2: ]
                elif FileTop[-2][-1] > 1:
                    del FileTop[-1]
                else:
                    while FileTop[-1][-1] == 1:
                        del FileTop[-1]
                while FileTop[-1][-1] == 1:
                    del FileTop[-1]
                i = FileTop[-1][0]
#                print FileTop
            else:
                print PrintFor(FileTop) + "├─" + lists
#                print FileTop
                if FileTop[-1][0] == FileTop[-2][0]:
                    del FileTop[-2]
#                print FileTop

def main():
    FileSystem(Path)
    print FileTop

if __name__ == '__main__':
	main()
