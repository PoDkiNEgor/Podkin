from tkinter import *
from tkinter import messagebox
import math
import tkinter as tk

root = tk.Tk()
root.title("Пример вызова функции с кнопки") 

def method1():
    window = Tk()
    window.title('Калькулятор твердости')
    window.geometry('400x200')
 
 
    frame = Frame(
        window,
       padx=10,
       pady=10
    )
    frame.pack(expand=True)


##method = input('Выберите метод определения твердости: ')







##if method == 'ВИККЕРС':
    

    def vickers():
        d1 = float(d1_tf.get()) #С помощью метода .get получаем из поля ввода с именем weight_tf значение веса, которое ввёл пользователь и конвертируем в целое число с помощью int().
        d2 = float(d2_tf.get()) #С помощью метода .get получаем из поля ввода с именем height_tf значение роста и конвертируем в целое число с помощью int(). Обязательно делим его на 100, так как пользователь вводит рост в сантиметрах, а в формуле для расчёта ИМТ используются метры.
        P = float(P_tf.get())
        HV = 1.854*(P/(d1+d2/2)**2)
        HV = round(HV, 2) 

        messagebox.showinfo('HV-pythonguides', f'Твердость по Виккерсу = {HV} ')
        
        


     
     
    d1_lb = Label(
        frame,
        text="Введите первую диагональ  "
    )
    d1_lb.grid(row=3, column=1)
         
    d2_lb = Label(
        frame,
        text="Введите вторую диагональ ",
    )
    d2_lb.grid(row=4, column=1)

    P_lb = Label(
        frame,
        text="Введите нагрузку ",
    )
    P_lb.grid(row=5, column=1)
         
    d1_tf = Entry(
        frame,
    )
    d1_tf.grid(row=3, column=2, pady=5)
         
    d2_tf = Entry(
        frame,
    )
    d2_tf.grid(row=4, column=2, pady=5)
        
    P_tf = Entry(
        frame,
    )
    P_tf.grid(row=5, column=2, pady=5)

         
    cal_btn = Button(
        frame,
        text='Рассчитать твердость',
        command=vickers
    )
    cal_btn.grid(row=7, column=2)
    
    


    
    window.mainloop()

def method2():
    window = Tk()
    window.title('Калькулятор твердости')
    window.geometry('400x200')
 
 
    frame = Frame(
        window,
       padx=10,
       pady=10
    )
    frame.pack(expand=True)

    def brinel():
        d = int(d1_tf.get()) #С помощью метода .get получаем из поля ввода с именем weight_tf значение веса, которое ввёл пользователь и конвертируем в целое число с помощью int().
        
        F = float(F_tf.get())
        D = float(D_tf.get())
        pi = math.pi
        HBW = (0.102*F)/(pi*D/2)*(D - ((D**2)-(d**2))**0.5)
        HBW = round(HBW, 2) 

        messagebox.showinfo('HBW-pythonguides', f'Твердость по Бринелю = {HBW} ')




 
 
    d1_lb = Label(
        frame,
        text="Введите диаметр отпечатка  "
    )
    d1_lb.grid(row=3, column=1)
         
    

    D_lb = Label(
        frame,
        text="Введите диаметр шарика ",
    )
    D_lb.grid(row=5, column=1)

    F_lb = Label(
        frame,
        text="Введите нагрузку ",
    )
    F_lb.grid(row=6, column=1)
         
    d1_tf = Entry(
        frame,
    )
    d1_tf.grid(row=3, column=2, pady=5)
         
    

    D_tf = Entry(
        frame,
    )
    D_tf.grid(row=5, column=2, pady=5)

    F_tf = Entry(
        frame,
    )
    F_tf.grid(row=6, column=2, pady=5)

         
    cal_btn = Button(
        frame,
        text='Рассчитать твердость',
        command=brinel
    )
    cal_btn.grid(row=7, column=2)




    window.mainloop()

# Создание кнопки с вызовом функции say_hello при нажатии
vickers_button = tk.Button(root, text="Виккерс", command=method1)
vickers_button.pack()

brinel_button = tk.Button(root, text="Бринелль", command=method2)
brinel_button.pack()

root.mainloop()
