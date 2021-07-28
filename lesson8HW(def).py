def a():
    come=int(input('進貨幾顆蘋果?'))
    return come
def b():
    out=int(input('出貨幾顆蘋果?'))
    return out
def c():
    hi=['進貨輸入1','出貨輸入2','查看營業額統計輸入3','查看庫存輸入4','離開系統輸入5']
    for i in hi:
        print(i)
for i in range(1):
    aa=int(input('目前有多少個蘋果?'))
    bb=int(input('一個蘋果賣多少錢?'))
    print('----------------------------')
ccc=c()
print('----------------------------')
se=[]
sss=0
money=0
i=0
while i<1: 
   w=int(input('請選擇要使用的功能'))
   if w==1:
       c1=a()
       aa=aa+c1
   elif w==2:
       o1=b()
       if aa>=o1:
           print('應收: $',bb*o1)
           se.append(o1)
           sss=sss+1
           aa=aa-o1
           money=money+bb*o1
       else:
           print('庫存不夠，還差:',o1-aa,'顆')
   elif w==3:
           print('今天有',sss,'筆交易')
           print('交易如下，分別為:')
           for x in se:
               print(x)
           print('共收入',money,'元')
   elif w==4:
        print('庫存',aa)
   elif w==5:
       print('已離開系統')
       i=i+1