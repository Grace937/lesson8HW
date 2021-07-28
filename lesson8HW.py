for i in range(1):
    aa=int(input('目前有多少個蘋果?'))
    bb=int(input('一個賣蘋果多少錢?'))
    print('----------------------------')
se=[]
sss=0
money=0
hi=['進貨輸入1','出貨輸入2','查看營業額統計輸入3','查看庫存輸入4','離開系統輸入5']
for i in hi:
    print(i)
print('----------------------------')
i=0
while i<1: 
   w=int(input('請選擇要使用的功能'))
   if w==1:
       come=int(input('進貨幾顆蘋果?'))
       aa=aa+come
   elif w==2:
        out=int(input('出貨幾顆蘋果?'))
        if aa<out:
            print('庫存不夠，還差:',out-aa,'顆')
        else:
            print('應收: $',bb*out)
            se.append(out)
            sss=sss+1
            aa=aa-out
            money=money+bb*out
   elif w==3:
           print('今天有',sss,'筆交易')
           print('交易如下，分別為:')
           for x in se:
               print(x,'顆')
           print('共收入',money,'元')
   elif w==4:
        print('庫存',aa,' 顆')
   elif w==5:
       print('已離開系統')
       i=i+1