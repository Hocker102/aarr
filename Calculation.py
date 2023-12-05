import Datas

#Test

Datas.PriceList()

def calculation():
    selected_type = Datas.Type_var.get()
    selected_fabric = Datas.Fabric_var.get()
    selected_wood = Datas.Wood_var.get()
    selected_metal = Datas.Metal_var.get()
    selected_size = Datas.Size_var.get()
    
    #Получение цены для из словаря prices
    type_cost = Datas.PriceList().get(selected_type,0)
    fabric_cost = Datas.PriceList().get(selected_fabric,0)
    wood_cost = Datas.PriceList().get(selected_wood,0)
    metal_cost = Datas.PriceList().get(selected_metal,0)
    size_cost = Datas.PriceList().get(selected_size,0)
    
    #Рассчитать общую себестоимоисть
    if selected_type == "Кровать":
        metal_cost = 0
    total_cost = (type_cost+fabric_cost+wood_cost+metal_cost)*size_cost
    return total_cost