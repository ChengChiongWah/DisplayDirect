#-*- coding:utf-8 -*-
#author:chengchiongwah
#Email:chengchiongwah@gmail.com
#With Python 2.7.3
#vsion:v1.0
import sys,os,time
print "Please input the path of the directory"
Path = raw_input("")
print "┌──" + "Path"
FileTop = [[ 0, 0, 0]]
i = 1
k = -2

def PrintFor(FileTop):       #打印格式
    s = ""
    j = []
    h = 1
    Level = FileTop[ -1][ 0]
    while 0 < FileTop[ h][ 0] < Level:
        if FileTop[ h][ -1] == 1:
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
        del FileTop[ -1]
        while FileTop[ -1][ -1] == 1:
            while FileTop[ k][ 0] == FileTop[ -1][ 0] and FileTop[ k][ -1] != FileTop[ -1][ -2]:
                k -=1
            del FileTop[ (k + 1): ]
        i = FileTop[ -1][ 0]
        k = -2
#        print FileTop
    
    for lists in listdir:
        NexPth = os.path.join(Path,lists)
        
        if os.path.isdir(NexPth):
            if lists == listdir[0]:     #如果第一个是目录的话，直接append
                FileTop.append([ i, LevelDetail, LevelDetail])
            else:                                      
                i = FileTop[-1][0]
                FileTop.append([ FileTop[ -1][ 0], FileTop[ -1 ][-2], FileTop[ -1 ][ -1 ] - 1])
            if FileTop[-1][-1] == 1:  
                print PrintFor(FileTop) + "└─" + lists
#                print FileTop
            else:  
                print PrintFor(FileTop) + "├─" + lists
#                print FileTop
            if FileTop[ -2][ 0] == FileTop[ -1][ 0]:
                del FileTop[ -2]
#            print FileTop
            i +=1
            FileSystem(NexPth)
            
        else:
            if lists == listdir[0]:
                FileTop.append([ i, LevelDetail, LevelDetail])
            else:
                FileTop.append([ FileTop[ -1][ 0], FileTop[ -1][ -2], FileTop[ -1][ -1] -1])
            if FileTop[ -1][ -1] == 1:
                print PrintFor(FileTop) + "└─" + lists
#                print FileTop
                if FileTop[ -2][0] == FileTop[ -1][0]:
                    del FileTop[ -2: ]
                elif FileTop[ -2][ -1] > 1:
                    del FileTop[ -1]
                else:
                    while FileTop[ -1][ -1] == 1:
                        del FileTop[ -1]
                while FileTop[ -1][ -1] == 1:
                    del FileTop[ -1]
                i = FileTop[ -1][ 0]
#                print FileTop
            else:
                print PrintFor(FileTop) + "├─" + lists
#                print FileTop
                if FileTop[ -1][ 0] == FileTop[ -2][ 0]:
                    del FileTop[ -2]
#                print FileTop

def main():
    FileSystem(Path)
    print FileTop

if __name__ == '__main__':
	main()
