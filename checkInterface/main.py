# -*- coding: utf-8 -*-
from matching import *

#��־��������
def func():
    para_value = [None]*50    #�̶����飬���ڴ洢�������Ĳ�����
    f = open("YKAdebug_sendCache.txt")    #�򿪱���log
    l =[None]*50   #�̶����飬�洢ÿһ���¼���ÿһ������
    #losedpara=[None]*30
    line = (f.readline()).decode('utf-8')   #���ж�ȡ
    mark = -1   #�¼����Ͳ����������е�����
    n = -1   #�¼����Ʋ����������е�����
    para_i = 0
    i = 0
    extend = -1
    rc = -1
    while True:
      #print line
      if len(line) == 0:    #�ж���־�����Ƿ����
         break
      if cmp(line.strip(),'}') == 0  or cmp(line.strip(),'}, {') == 0:
         j=0
         if "A5" in l[mark]:
             identifying(l,extend,rc,n)    #�����A5�¼������в���ƥ��
         i = 0
         para_i = i
      line = (f.readline()).decode('utf-8')
      l[para_i] = line
      if cmp(line.strip(),'}') != 0 and cmp(line.strip(),'}, {') != 0 and len(line) != 0 and cmp(line.strip(),'{') != 0:
         npos = line.index(':')
         s1 = line[1:npos]   #���ա��������ַ������н�ȡ
         s2 = line[npos+1:len(line)]

         if cmp(s1.strip(),'"t1"') == 0:
            mark=i
         if cmp(s1.strip(),'"e"') == 0:
             extend=i
         if cmp(s1.strip(),'"rc1"') == 0:
             rc=i
      if "n3" in line:
        n = i
        #print n
      i = i+1
      para_i = i
    f.close()



if __name__=='__main__':
    func()
