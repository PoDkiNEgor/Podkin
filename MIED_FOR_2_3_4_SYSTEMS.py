import array
import subprocess
import math 

CONST = array.array('d',[0.25, 1, 96484.56])
P = CONST[0]
QP = CONST[1]
F = CONST[2]


my_dict = {
    'AL':  array.array('d',[4.2, 1.39, 4.6, 0, 0.07]),
    'SC':  array.array('d',[3.30, 1.32, 6.10,    0.00,    0.07]) ,  
    'Y': array.array('d',[ 3.20, 1.22, 7.36,    0.00,    0.07]),
    'LA': array.array('d',[3.05, 1.09, 7.98,   0.00,   0.07]),
    'CE': array.array('d',[3.02, 1.07, 7.54,    0.00,    0.07]),
    'PR': array.array('d',[3.03, 1.08, 7.57,    0.00,    0.07]),
    'ND': array.array('d',[3.04, 1.11, 7.51,    0.00,    0.07]),
    'SM': array.array('d',[3.10, 1.10, 7.36,    0.00,    0.07]),
    'EU': array.array('d',[3.16, 0.90, 9.42,    0.00,    0.07]),
    'GD': array.array('d',[3.18, 1.19, 7.35,    0.00,    0.07]),
    'TB': array.array('d',[3.15, 1.20, 7.20,    0.00,    0.07]),
    'DY': array.array('d',[3.23, 1.23, 7.13,    0.00,    0.07]),
    'HO': array.array('d',[3.20, 1.24, 7.07,    0.00,    0.07]),
    'ER': array.array('d',[3.21, 1.26, 6.99,    0.00,    0.07]),
    'TM': array.array('d',[3.24, 1.27, 6.90,    0.00,    0.07]),
    'YB': array.array('d',[3.20, 0.95, 8.50,    0.00,    0.07]),
    'LU': array.array('d',[3.40, 1.30, 6.81,    0.00,    0.07]),
    'TH': array.array('d',[3.30, 1.28, 7.30,    0.00,    0.07]),
    'U': array.array('d',[3.33, 1.56, 5.60,    0.00,    0.07]),
    'PU': array.array('d',[3.07, 1.44, 5.20,    0.00,    0.07]),
    'GA': array.array('d',[4.10, 1.31, 5.20,    0.45,    0.07]),
    'IN': array.array('d',[4.00, 1.17, 6.30,    0.25,    0.07]),
    'TL': array.array('d',[3.90, 1.12, 6.60,    0.25,    0.07]),
    'SN': array.array('d',[4.15, 1.24, 6.40,    0.10,    0.04]),
    'PB': array.array('d',[4.10, 1.15, 6.90, 0.00,    0.04]),
    'SB': array.array('d',[4.25, 1.26, 6.60, 0.30,    0.04]),
    'BI': array.array('d',[4.15, 1.16, 7.20, 0.30,    0.04]) 


}

while True:

    print("="*15,"MIEDEMA MODEL","="*15)

    numb = int(input("Сколько компонентов в вашей системе?: "))
    if numb == 2:
        print("Вы выбрали расчет для двойных систем")
        def miedema(X1, X2):
            global element_1, r1, f1, n1, v1, RP1, a1, element_2, r2, f2, n2, v2, RP2, a2
            try:
                element_1 = X1
                r1 = my_dict[element_1]
                f1 = r1[0]
                n1 = r1[1]
                v1 = r1[2]
                RP1 = r1[3]
                a1 = r1[4]

                element_2 = X2
                r2 = my_dict[element_2]
                f2 = r2[0]
                n2 = r2[1]
                v2 = r2[2]
                RP2 = r2[3]
                a2 = r2[4]
            except KeyError as e:
                print(f"Ошибка: Элемент {e} отсутствует в словаре.")

        X1 = input('Введите первый элемент: ')
        X2 = input('Введите второй элемент: ')

         


        miedema(X1,X2)
        if X1 in my_dict.keys() and X2 in my_dict.keys():

            print('ПРОВЕРКА КОДА ПРОЙДЕНА')

            if X1 == X2:
                 print('ОШИБКА')


            else:
                ca = float(input('Введите концентрацию первого элемента А: '))
                cb = float(input('Введите концентрацию второго элемента B: '))

                if ca + cb == 1:
                    x = int(input('Нажмите 1 для СТАРТА '))
                    if x == 1:
                        e = math.e


                        print('e= ',e)

                
                        Q = 9.4 * P

                        print("Q= ", Q)

                        df =  -((f1-f2)**2)
                        print("изменение электроотрицательности df =", df)

                        

                        dn = P * (n1 - n2)**2
                        print("изменение электронной плотности dn = ", dn)


                        csa = (ca * v1)/((ca * v1) + (cb * v2))
                        csb = (cb * v2)/((ca * v1) + (cb * v2))



                        print('csa = ', csa)
                        print('csb = ', csb)

                        
                        print('постоянная Фарадея F = ',F)

                   

                        fc  = csa * csb *(1+8*(csa**2)*(csb**2))
                        print("функция поверхностных атомных концентраций fc = ", fc)
                        gc = 2*(((ca*v1))+(cb*v2))/((1/n1)+(1/n2))
                        print('функция  атомных концентраций g(c) = ', gc)

                        CON = df + dn 
             

                        dH = fc*gc*F*P*CON

                        print( "Энтальпия образования:", float(dH/1000), 'КДж')



                        C = int(input("Введите количество атомов в интерметалиде "))
                        dHsumm = - (C*dH)
                        print( "Сумммарная энтальпия образования:", dHsumm/1000 , 'КДж')
                        




                        text_file = open("results.txt", "w")
                        text_file.write("Энтальпия образования: " + str(dH/1000)+ ' КДж')
                        text_file.close()
                        file_path = 'results.txt'
                        subprocess.Popen(['notepad.exe', file_path])
                        
                    
                  
                    
                    else:
                        print('ОШИБКА')
                        
                else:
                    print('ОШИБКА')

    elif numb == 3:
        print("Вы выбрали расчет для тройных систем")

        def miedema(X1, X2, X3):
            global element_1, r1, f1, n1, v1, RP1, a1, element_2, r2, f2, n2, v2, RP2, a3, element_3, r3, f3, n3, v3, RP3, a3
            try:
                element_1 = X1
                r1 = my_dict[element_1]
                f1 = r1[0]
                n1 = r1[1]
                v1 = r1[2]
                RP1 = r1[3]
                a1 = r1[4]

                element_2 = X2
                r2 = my_dict[element_2]
                f2 = r2[0]
                n2 = r2[1]
                v2 = r2[2]
                RP2 = r2[3]
                a2 = r2[4]

                element_3 = X3
                r3 = my_dict[element_3]
                f3 = r3[0]
                n3 = r3[1]
                v3 = r3[2]
                RP3 = r3[3]
                a3 = r3[4]

            except KeyError as e:
                print(f"Ошибка: Элемент {e} отсутствует в словаре.")

        X1 = input('Введите первый элемент: ')
        X2 = input('Введите второй элемент: ')
        X3 = input('Введите третий элемент: ')
         


        miedema(X1,X2,X3)
        if X1 in my_dict.keys() and X2 in my_dict.keys() and X3 in my_dict.keys():

            print('ПРОВЕРКА КОДА ПРОЙДЕНА')

            if X1 == X2 == X3:
                 print('ОШИБКА')


            else:
                ca = float(input('Введите концентрацию первого элемента А: '))
                cb = float(input('Введите концентрацию второго элемента B: '))
                cc = float(input('Введите концентрацию третьего элемента C: '))

                if ca + cb + cc == 1:
                    x = int(input('Нажмите 1 для СТАРТА '))
                    if x == 1:
                        e = math.e


                        print('e= ',e)

                
                        Q = 9.4 * P

                        print("Q= ", Q)

                        print("f3=", f3)

                        df1 =  -((f1-f2)**2)
                        print("изменение электроотрицательности df1 = ", df1)
                        df2 =  -((f2-f3)**2)
                        print("изменение электроотрицательности df2 = ", df2)
                        df3 =  -((f1-f3)**2)
                        print("изменение электроотрицательности df3 = ", df3)

                        

                        dn1 = P * (n1 - n2)**2
                        print("изменение электронной плотности dn = ", dn1)
                        dn2 = P * (n2 - n3)**2
                        print("изменение электронной плотности dn = ", dn2)
                        dn3 = P * (n1 - n3)**2
                        print("изменение электронной плотности dn= ", dn3)


                        csa = (ca * v1)/((ca * v1) + (cb * v2)) 
                        csb = (cb * v2)/((ca * v1) + (cb * v2)) 
                 




                        print('csa для первого элемента = ', csa)
                        print('csb для второго элемента = ', csb)
                        

                        
                        print('постоянная Фарадея F = ',F)

                   

                        fc1  = csa * csb *(1+8*(csa**2)*(csb**2))
                        print("функция поверхностных атомных концентраций fc1= ", fc1)
                        gc1 = 2*(((ca*v1))+(cb*v2))/((1/n1)+(1/n2))
                        print('функция  атомных концентраций g(c)1= ', gc1)

                        CON1 = df1 + dn1 
             

                        dHab = fc1*gc1*F*P*CON1

                        

                        print( "Энтальпия образования AB:", float(dHab/1000), 'КДж')

                        csb = (cb * v1)/((cb * v1) + (cc * v2)) 
                        csc = (cb * v2)/((cb * v1) + (cc * v2))

                        print('csb для второго элемента = ', csb)
                        print('csc для третьего элемента = ', csc)




                        fc2  = csb * csc *(1+8*(csb**2)*(csc**2))
                        print("функция поверхностных атомных концентраций fc2= ", fc2)
                        gc2 = 2*(((cb*v2))+(cc*v3))/((1/n2)+(1/n3))
                        print('функция  атомных концентраций g(c)2= ', gc2)

                        CON2 = df2 + dn2 
             

                        dHbc = fc2*gc2*F*P*CON2

                        

                        print( "Энтальпия образования BC:", float(dHbc/1000), 'КДж')

                        csa = (ca * v1)/((ca * v1) + (cc * v2)) 
                        csc = (cc * v2)/((ca * v1) + (cc * v2))

                        print('csa для первого элемента = ', csa)
                        print('csc для третьего элемента = ', csc)

                        fc3  = csa * csc *(1+8*(csa**2)*(csc**2))
                        print("функция поверхностных атомных концентраций fc3= ", fc3)
                        gc3 = 2*(((ca*v1))+(cc*v3))/((1/n1)+(1/n3))
                        print('функция  атомных концентраций g(c)3= ', gc3)

                        CON3 = df3 + dn3 
             

                        dHac = fc3*gc3*F*P*CON3

                        

                        print( "Энтальпия образования AC:", float(dHac/1000), 'КДж')

                        dHabc = (dHab*((csb+csa)**2))+(dHac*((csc+csa)**2))+ (dHbc*((csc+csb)**2))

                        print( "Энтальпия образования ABC:", float(dHabc/1000), 'КДж')



##                        C = int(input("Введите количество атомов в интерметалиде "))
##                        dHsumm = - (C*dH)
##                        print( "Сумммарная энтальпия образования:", dHsumm/1000 , 'КДж')
                        




##                        text_file = open("results.txt", "w")
##                        text_file.write("Энтальпия образования: " + str(dH/1000)+ ' КДж')
##                        text_file.close()
##                        file_path = 'results.txt'
##                        subprocess.Popen(['notepad.exe', file_path])
                        
                    
                  
                    
                    else:
                        print('ОШИБКА')
                        
                else:
                    print('ОШИБКА')    
    elif numb == 4:
        print("Вы выбрали расчет для систем с четырьмя элементами")
        def miedema(X1, X2, X3, X4):
            global element_1, r1, f1, n1, v1, RP1, a1, element_2, r2, f2, n2, v2, RP2, a2, element_3, r3, f3, n3, v3, RP3, a3, element_4, r4, f4, n4, v4, RP4, a4
            try:
                element_1 = X1
                r1 = my_dict[element_1]
                f1 = r1[0]
                n1 = r1[1]
                v1 = r1[2]
                RP1 = r1[3]
                a1 = r1[4]

                element_2 = X2
                r2 = my_dict[element_2]
                f2 = r2[0]
                n2 = r2[1]
                v2 = r2[2]
                RP2 = r2[3]
                a2 = r2[4]

                element_3 = X3
                r3 = my_dict[element_3]
                f3 = r3[0]
                n3 = r3[1]
                v3 = r3[2]
                RP3 = r3[3]
                a3 = r3[4]

                element_4 = X4
                r4 = my_dict[element_4]
                f4 = r4[0]
                n4 = r4[1]
                v4 = r4[2]
                RP4 = r4[3]
                a4 = r4[4]

            except KeyError as e:
                print(f"Ошибка: Элемент {e} отсутствует в словаре.")
        X1 = input('Введите первый элемент: ')
        X2 = input('Введите второй элемент: ')
        X3 = input('Введите третий элемент: ')
        X4 = input('Введите четвертый элемент: ')


        miedema(X1,X2,X3,X4)
        if X1 in my_dict.keys() and X2 in my_dict.keys() and X3 in my_dict.keys() and X4 in my_dict.keys():

            print('ПРОВЕРКА КОДА ПРОЙДЕНА')

            if X1 == X2 == X3 == X4:
                 print('ОШИБКА')


            else:
                ca = float(input('Введите концентрацию первого элемента А: '))
                cb = float(input('Введите концентрацию второго элемента B: '))
                cc = float(input('Введите концентрацию третьего элемента C: '))
                cd = float(input('Введите концентрацию четвертого элемента D: '))

                if ca + cb + cc + cd == 1:
                    x = int(input('Нажмите 1 для СТАРТА '))
                    if x == 1:
                        e = math.e


                        print('e= ',e)

                
                        Q = 9.4 * P

                        print("Q= ", Q)

                        print("f3=", f3)

                        df1 =  -((f1-f2)**2)
                        print("изменение электроотрицательности dfAB = ", df1)
                        df2 =  -((f2-f3)**2)
                        print("изменение электроотрицательности dfBC = ", df2)
                        df3 =  -((f1-f3)**2)
                        print("изменение электроотрицательности dfAC = ", df3)
                        df4 =  -((f1-f4)**2)
                        print("изменение электроотрицательности dfAD = ", df4)
                        df5 =  -((f2-f4)**2)
                        print("изменение электроотрицательности dfBD = ", df5)
                        df6 =  -((f4-f3)**2)
                        print("изменение электроотрицательности dfDC = ", df6)

                        

                        dn1 = P * (n1 - n2)**2
                        print("изменение электронной плотности dnAB = ", dn1)
                        dn2 = P * (n2 - n3)**2
                        print("изменение электронной плотности dnBC = ", dn2)
                        dn3 = P * (n1 - n3)**2
                        print("изменение электронной плотности dnAC= ", dn3)
                        dn4 = P * (n1 - n4)**2
                        print("изменение электронной плотности dnAD = ", dn4)
                        dn5 = P * (n2 - n4)**2
                        print("изменение электронной плотности dnBD = ", dn5)
                        dn6 = P * (n4 - n3)**2
                        print("изменение электронной плотности dnDC= ", dn6)


                        csa = (ca * v1)/((ca * v1) + (cb * v2)) 
                        csb = (cb * v2)/((ca * v1) + (cb * v2)) 
                 




                        print('csa для первого элемента = ', csa)
                        print('csb для второго элемента = ', csb)
                        

                        
                        print('постоянная Фарадея F = ',F)

                   

                        fc1  = csa * csb *(1+8*(csa**2)*(csb**2))
                        print("функция поверхностных атомных концентраций fc1= ", fc1)
                        gc1 = 2*(((ca*v1))+(cb*v2))/((1/n1)+(1/n2))
                        print('функция  атомных концентраций g(c)1= ', gc1)

                        CON1 = df1 + dn1 
             

                        dHab = fc1*gc1*F*P*CON1

                        

                        print( "Энтальпия образования AB:", float(dHab/1000), 'КДж')

                        csb = (cb * v1)/((cb * v1) + (cc * v2)) 
                        csc = (cb * v2)/((cb * v1) + (cc * v2))

                        print('csb для второго элемента = ', csb)
                        print('csc для третьего элемента = ', csc)




                        fc2  = csb * csc *(1+8*(csb**2)*(csc**2))
                        print("функция поверхностных атомных концентраций fc2= ", fc2)
                        gc2 = 2*(((cb*v2))+(cc*v3))/((1/n2)+(1/n3))
                        print('функция  атомных концентраций g(c)2= ', gc2)

                        CON2 = df2 + dn2 
             

                        dHbc = fc2*gc2*F*P*CON2

                        

                        print( "Энтальпия образования BC:", float(dHbc/1000), 'КДж')

                        csa = (ca * v1)/((ca * v1) + (cc * v2)) 
                        csc = (cc * v2)/((ca * v1) + (cc * v2))

                        print('csa для первого элемента = ', csa)
                        print('csc для третьего элемента = ', csc)

                        fc3  = csa * csc *(1+8*(csa**2)*(csc**2))
                        print("функция поверхностных атомных концентраций fc3= ", fc3)
                        gc3 = 2*(((ca*v1))+(cc*v3))/((1/n1)+(1/n3))
                        print('функция  атомных концентраций g(c)3= ', gc3)

                        CON3 = df3 + dn3 
             

                        dHac = fc3*gc3*F*P*CON3

                        

                        print( "Энтальпия образования AC:", float(dHac/1000), 'КДж')

                        csa = (ca * v1)/((ca * v1) + (cd * v4)) 
                        csd = (cd * v4)/((ca * v1) + (cd * v4))

                        print('csa для первого элемента = ', csa)
                        print('csc для четвертого элемента = ', csc)

                        fc4  = csa * csd *(1+8*(csa**2)*(csd**2))
                        print("функция поверхностных атомных концентраций fc4= ", fc4)
                        gc4 = 2*(((ca*v1))+(cd*v4))/((1/n1)+(1/n4))
                        print('функция  атомных концентраций g(c)4= ', gc4)

                        CON4 = df4 + dn4 
             

                        dHad = fc4*gc4*F*P*CON4

                        

                        print( "Энтальпия образования AD:", float(dHad/1000), 'КДж')



                        csb = (cb * v2)/((ca * v2) + (cb * v4)) 
                        csd = (cd * v4)/((ca * v2) + (cd * v4))

                        print('csb для второго элемента = ', csb)
                        print('csd для четвертого элемента = ', csd)

                        fc5  = csb * csd *(1+8*(csb**2)*(csd**2))
                        print("функция поверхностных атомных концентраций fc5= ", fc5)
                        gc5 = 2*(((cb*v2))+(cd*v4))/((1/n2)+(1/n4))
                        print('функция  атомных концентраций g(c)5= ', gc5)

                        CON5 = df5 + dn5 
             

                        dHbd = fc5*gc5*F*P*CON5

                        

                        print( "Энтальпия образования BD:", float(dHbd/1000), 'КДж')


                        csd = (cd * v4)/((cd * v4) + (cc * v3)) 
                        csc = (cc * v3)/((cd * v4) + (cc * v3))

                        print('csb для четвертого элемента = ', csd)
                        print('csd для третьего элемента = ', csc)

                        fc6  = csd * csc *(1+8*(csd**2)*(csc**2))
                        print("функция поверхностных атомных концентраций fc6= ", fc6)
                        gc6 = 2*(((cd*v4))+(cc*v3))/((1/n4)+(1/n3))
                        print('функция  атомных концентраций g(c)6= ', gc6)

                        CON6 = df6 + dn6 
             

                        dHdc = fc6*gc6*F*P*CON6

                        

                        print( "Энтальпия образования DC:", float(dHdc/1000), 'КДж')



                        dHabcd = (dHab*((csb+csa)**2))+(dHac*((csc+csa)**2)) + (dHbc*((csc+csb)**2)) + (dHad*((csa+csd)**2)) + (dHbd*((csb+csd)**2)) + (dHdc*((csd+csc)**2))

                        print( "Энтальпия образования ABCD:", float(dHabcd/1000), 'КДж')

                    else:
                        print('ОШИБКА')
                        
                else:
                    print('ОШИБКА')
    
 
            
    else:
        print('NET')
        print('ОШИБКА')
        
    
