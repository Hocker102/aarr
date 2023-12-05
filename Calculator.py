import tkinter as tk
from tkinter import Label, ttk
from tkinter import messagebox
import Calculation
import Datas

#Commit from  REAL airat)

#Создание окна
root = tk.Tk()
root.title("Кальулятор мебели")

#Вызов функций хранения параметров
Datas.Variables()
Datas.Sizes()
Datas.PriceList()

#Вызов функции определения суммы
Calculation.calculation()

#Создание списков

    #Тип мебели
Type_lbl = ttk.Label(root, text = "Тип мебели:")
Type_lbl.grid (row = 0, column = 0)
Type_cbox = ttk.Combobox(root, state = "readonly", textvariable=Datas.Type_var, values = ["Кресло","Диван","Кровать"])
Type_cbox.grid(row=0,column=1)
    #Ткань
Fabric_lbl = ttk.Label(root, text = "Ткань:")
Fabric_lbl.grid (row = 1, column=0)
Fabric_cbox = ttk.Combobox(root, state= "readonly", textvariable=Datas.Fabric_var,values = ["Жаккард", "Шенил","Кожа"])
Fabric_cbox.grid(row = 1,column=1)

    #Дерево
Wood_lbl = ttk.Label(root,text = "Дерево:")
Wood_lbl.grid(row=2,column=0)
Wood_cbox = ttk.Combobox(root,state="readonly",textvariable=Datas.Wood_var,values=["Массив","ЛДСП","ДСП","Фанера"])
Wood_cbox.grid(row = 2, column=1)
  
    #Металл
Metal_lbl = ttk.Label(root,text="Металл:")
Metal_lbl.grid(row=3,column=0)
Metal_cbox = ttk.Combobox(root,state= "readonly",textvariable=Datas.Metal_var, values = ["Титан","Оцинкованная сталь"])
Metal_cbox.grid(row=3,column=1)


    #Размер
Size_lbl = ttk.Label(root,text="Размер:")
Size_lbl.grid(row=4,column=0)
Size_cbox = ttk.Combobox(root,state= "readonly",textvariable=Datas.Size_var)
Size_cbox.grid(row=4,column=1)



def update_size(event):
    selected_type = Datas.Type_var.get()
    available_sizes = Datas.Sizes().get(selected_type,[])
    Size_cbox["values"] = available_sizes
    Datas.Size_var.set("")
   
    #Выбрана ли кровать?
    if selected_type == "Кровать":
        Metal_cbox.grid_remove()
    else:
        Metal_cbox.grid()

#Привязка события к функции update_size
Type_cbox.bind("<<ComboboxSelected>>",update_size)
def calculate_cost():
    selected_size = Datas.Size_var.get()

#Узнать результат
def show_result():
    if (Datas.Type_var.get() == "" or
        Datas.Fabric_var.get() == "" or
        Datas.Wood_var.get() == "" or
        Datas.Size_var.get() == ""):
        messagebox.showerror("Ошибка", "Пожалуйста, выберите все параметры перед расчетом.")
    else:    
        result_label["text"] = f"Себестоимость: {Calculation.calculation()} рублей"

#Кнопка для расчета
Result_btn = ttk.Button(root, text = "Рассчитать",command = show_result)
Result_btn.grid(row=5, columnspan=2)

#результат
global result_label
result_label = ttk.Label(root,text="Себестоимость: 0 рублей")
result_label.grid(row=6,columnspan=2)

#кнопка выхода
exit_button = ttk.Button(root,text = "Выход",command=root.quit)
exit_button.grid(row=7,columnspan=2)



root.mainloop()
