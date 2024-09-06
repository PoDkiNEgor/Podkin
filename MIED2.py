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
    



    print("="*15,"MIEDEMA MODEL","="*15)


    X1 = input('Введите первый элемент: ')
    X2 = input('Введите второй элемент: ')

     


    miedema(X1,X2)
    if X1 in my_dict.keys() and X2 in my_dict.keys():

        print('DA')

        if X1 == X2:
             print('ОШИБКА')


        else:
            ca = float(input('Введите концентрацию первого элемента А '))
            cb = float(input('Введите концентрацию первого элемента B '))

            if ca + cb == 1:
                x = int(input('Нажмите 1 для СТАРТА '))
                if x == 1:
                    e = math.e


                    print('e= ',e)

            
                    Q = 9.4 * P

                    print("Q= ", Q)

                    df =  -((f1-f2)**2)
                    print("изменение электроотрицательности df=", df)

                    

                    dn = P * (n1 - n2)**2
                    print("изменение электронной плотности dn= ", dn)


                    csa = (ca * v1)/((ca * v1) + (cb * v2))
                    csb = (cb * v2)/((ca * v1) + (cb * v2))



                    print('csa=', csa)
                    print('csb=', csb)

                    
                    print('постоянная Фарадея F=',F)

               

                    fc  = csa * csb *(1+8*(csa**2)*(csb**2))
                    print("функция поверхностных атомных концентраций fc= ", fc)
                    gc = 2*(((ca*v1))+(cb*v2))/((1/n1)+(1/n2))
                    print('функция  атомных концентраций g(c)= ', gc)

                    CON = df + dn 
         

                    dH = fc*gc*F*P*CON

                    print( "Энтальпия образования:", float(dH/1000), 'КДж')



                    C = int(input("Введите количество атомов в интерметалиде "))
                    dHsumm = - (C*dH)
                    print( "Сумммарная энтальпия образования:", dHsumm , 'КДж')
                    




                    text_file = open("results.txt", "w")
                    text_file.write("Энтальпия образования: " + str(dH/1000)+ ' КДж')
                    text_file.close()
                    file_path = 'results.txt'
                    subprocess.Popen(['notepad.exe', file_path])
                    
                
              
                
                else:
                    print('ОШИБКА')
                    
            else:
                print('ОШИБКА')
            
    else:
        print('NET')
        print('ОШИБКА')
        
    
