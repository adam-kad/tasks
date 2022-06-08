class Good:
    def __init__(self, name: str, price:int, count=1):
        
        if len(list(name)) > 20:
            raise Exception("В названии больше 20 символов")
        else:
            self.name = name
            
        if len(list(str(price))) > 7:
            raise Exception("В цене больше 7 символов")
        else:
            self.price = price
            
        if len(list(str(count))) > 3:
            raise Exception("В колличестве больше 3 символов")
        else:
            self.count = count
    
#--------------------------------------------------------#


class DiscountGood(Good):
    def __init__(self, name: str, price: int, count, disk=0):
        super().__init__(name, price, count)
        
        if disk > 99:
            raise Exception("Максимальная скидка: 99%")
        else:
            self.disk = disk
        
    
    def window(self):
        #Создание списка
        self.conc_window = []
        self.conc_window.append(self.name)
        self.conc_window.append(self.price)
        self.conc_window.append(self.count)
        return self.conc_window
    
    
    
    def conclusion(self, goods: list):
        
        #Итоговая сумма с учетом скидки
        self.disk_price = 0
        
        #Создание списка с вложенными списками
        goods.append(self.conc_window)
        
        print(f'{self.name} ', end=' '*18)
        print(f'{self.price}  *', end=' '*2)
        print(f'{self.count}  =', end=' '*3)
        
        if self.disk > 0:
            self.disk_price = self.total_price() - (self.total_price() * (self.disk/100))
            print(f'{self.disk_price}', end='  ')
        elif self.disk == 0:
            print(f'{self.total_price()}', end='  ')
            
        print(f'(-{self.disk}%) ')
              
        return goods
    
    
    #Метод для вычета цены * колличество данного товара
    def total_price(self):
        return self.price * self.count
    
    
    #Создание списка с ценами * колличество данного товара + скидка
    def global_price(self, global_price_list: list):
        if self.disk > 0:
            global_price_list.append(self.disk_price)
            return global_price_list
        elif self.disk == 0:
            global_price_list.append(self.total_price())
            return global_price_list
        
    #Итоговая сумма за товары
    def global_price_sum(self):
        self.global_sum = 0
        for gpl in global_price_list:
            self.global_sum = self.global_sum + gpl
        return self.global_sum


#--------------------------------------------------------#


Bread = Good('Bread', 17, 3)
Water = Good('Water', 19, 2)
Juice = Good('Juice', 80, 1)
Paper = Good('Paper', 19, 10)


#-------------------------------------------------------------#
#-------------------------------------------------------------#

goods = []
global_price_list = []

Bread = DiscountGood('Bread', 17, 3, 10)
Water = DiscountGood('Water', 19, 2)
Juice = DiscountGood('Juice', 80, 1, 15)
Paper = DiscountGood('Paper', 19, 10)


print('Name                    PPU   CNT     Price  Disc.\n==================================================')

Bread.window()
Water.window()
Juice.window()
Paper.window()
Bread.conclusion(goods=goods)
Water.conclusion(goods=goods)
Juice.conclusion(goods=goods)
Paper.conclusion(goods=goods)

print('================================================== \nTotal', end=' '*20)
Bread.global_price(global_price_list = global_price_list)
Water.global_price(global_price_list = global_price_list)
Juice.global_price(global_price_list = global_price_list)
Paper.global_price(global_price_list = global_price_list)

#Итоговая сумма с учетом скидок
print(f'={Paper.global_price_sum()}')


#Получение корзины клиента
#print(Paper.conclusion(goods))