import tkinter as tk

#Переменные для хранения параметров
Type_var = None
Fabric_var = None
Wood_var = None
Metal_var = None
Size_var = None


def Variables():
    global Type_var
    global Size_var
    global Fabric_var
    global Wood_var
    global Metal_var
    Type_var = tk.StringVar()
    Fabric_var = tk.StringVar()
    Wood_var = tk.StringVar()
    Metal_var = tk.StringVar()
    Size_var = tk.StringVar()
    
def PriceList():
    prices = {
        "Кресло": 800,
        "Диван":2000,
        "Кровать":1500,
        "Жаккард":200,
        "Шенилл":250,
        "Кожа":340,
        "Массив":500,
        "ЛДСП":300,
        "ДСП":250,
        "Фанера":200,
        "Титан":1000,
        "Оцинкованная сталь":800,
        "80x100":1.5,
        "140x70":2,
        "180x90":2.1,
        "60x120":1.5,
        "120x190":2.5,
        "180x200":3
        }
    return prices
    
def Sizes():
    Type_sizes= {
    "Кресло": ["80x100"],
    "Диван": ["180x90","140x70"],
    "Кровать":["60x120","120x190","180x200"]
    }
    return Type_sizes
