a = []
x=0
while True : 
    print ('~~~~~~~~~~\n PungyahShoesShop \n~~~~~~~~~~ ')
    print ('1)Nike ลด 20% [n]\n2)Adidas ลด 30% [a]\nสินสุดการเลือกรายการ [x]')
    brand = input ('Please select brand : ')
    brand = brand.lower()
    while brand =='n' :
        print ('\n*************Nike************\n1.Nike Air Force 1 React [1]\n2.Nike Air Max 270 React [2] \n3.Jordan Jumpman 2020 PF[3] \n4.Nike Air[4] \n5.home [0]')
        nike = (input ('Please select Nike :  '))
        nike = nike.lower()
        if nike== '1':
            n1 = ('Nike Air Force 1 React:4,500:900:3,600')
            a.append(n1)
            x+=3600      
            print ('\n-----------รายการได้ถูกเก็บไว้ในตะกร้า Shopping แล้วค่ะ----------------\n')
        elif nike== '2':
            n2 = ('Nike Air Max 270 React:5,000:1,000:4,000')  
            a.append(n2)
            x+=4000
            print ('\n-----------รายการได้ถูกเก็บไว้ในตะกร้า Shopping แล้วค่ะ----------------\n')
        elif nike== '3' :
            n3 = ('Jordan Jumpman 2020 PF:5,500:1,100:4,400')
            a.append(n3)
            x+=4400
            print ('\n-----------รายการได้ถูกเก็บไว้ในตะกร้า Shopping แล้วค่ะ----------------\n')
        elif nike== '4' :
            n4 = ('Nike Air PF:5,500:1,100:4,400')
            a.append(n4)
            x+=4400
            print ('\n-----------รายการได้ถูกเก็บไว้ในตะกร้า Shopping แล้วค่ะ----------------\n')
        elif nike== '0':
            break    
    while brand == 'a' :
        print ('***********Adidas************\n1)PUSHA T OZWEEGO [1]\n2)ADDVANTAGE BASE [2]\n3)NITE JOGGER [3]\n5.Backhome [0]')
        addie = (input ('Please select Adidas : '))
        addie = addie.lower()
        if addie == '1' :
            a01 = ('PUSHA T OZWEEGO:5,300:1,590:3,710')
            a.append(a01)
            x+=3710
            print ('\n-----------รายการได้ถูกเก็บไว้ในตะกร้า Shopping แล้วค่ะ----------------\n')
        elif addie == '2' :
            a02 = ('ADDVANTAGE BASE:2,000:600:1,400')
            a.append(a02)
            x+=1400
            print ('\n-----------รายการได้ถูกเก็บไว้ในตะกร้า Shopping แล้วค่ะ----------------\n')
        elif addie == '3' :
            a03 = ('NITE JOGGER:4,900:1,470:3,430')
            a.append(a03)
            x+=3430
            print ('\n-----------รายการได้ถูกเก็บไว้ในตะกร้า Shopping แล้วค่ะ----------------\n')
        elif addie== '0':
            break
        
    if brand == 'x' :
        print ('                                  สินค้าและจำนวนเงินที่ต้องจ่าย')
        print ('{0:-<120}'.format(""))
        print ('{0:' '<35}{1:' '<35}{2:' '<35}{3:' '<35}'.format('รุ่น','ราคา','ส่วนลด','จ่ายจริง'))
        print ('{0:-<120}'.format(""))
        count=1
        for d in a :
            e = d.split(':')
            print(count,end=". ")
            print('{0[0]:<32}{0[1]:<35}{0[2]:<36}{0[3]:<36}'.format(e))
            count+=1
        print ('{0:-<120}'.format(""))
        print('รวมเป็นเงิน                                                                                              %d'%x)
        print ('{0:-<120}'.format(""))
        
    