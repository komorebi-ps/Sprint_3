import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

#1    
    @property
    def get_name_items(self):
        return self.__name_items
    
    @property
    def get_number_items(self):
        return self.__number_items
    
#2
    def add_item_to_cheque(self, name):
        try:
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            self.__name_items.append(name)
            self.__number_items += 1
        except ValueError:
            print('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        except NameError:
            print('Позиция отсутствует в товарном справочнике')

 #3                                   
    def delete_item_from_check(self, name):
        try: 
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            self.__name_items.remove(name)
            self.__number_items -= 1
        except NameError:
            print('Позиция отсутствует в чеке')

#4
    def check_amount(self):
        total = []
        for name in self.__name_items:
            price = self.__item_price[name]
            total.append(price) 
        total_sum = sum(total)
        if len(self.__name_items) > 10:
            total_sum = total_sum - total_sum * 0.1
        return total_sum

#5
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 20:
                twenty_percent_tax.append(name)
                price = self.__item_price[name]
                total.append(price)
        tax_sum = 0
        for price in total:
            if len(self.__name_items) > 10:
                price = price * 0.9
            item_tax = price * 0.2
            tax_sum += item_tax
        return tax_sum

#6       
    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for name in self.__name_items:
            if self.__tax_rate[name] == 10:
               ten_percent_tax.append(name)  
               price = self.__item_price[name]
               total.append(price)
        tax_sum = 0
        for price in total:
            if len(self.__name_items) > 10:
                price = price * 0.9
            item_tax = price * 0.1
            tax_sum += item_tax
        return tax_sum

#7            
    def total_tax(self):
        total_tax = self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()
        return total_tax
    
#8
    @staticmethod
    def get_telephone_number(telephone_number):
        try:
            telephone_number_int = int(telephone_number)
            if telephone_number_int != telephone_number:
                raise ValueError('Необходимо ввести цифры')
            if len(str(telephone_number)) > 10:
                raise ValueError('Необходимо ввести 10 цифр после "+7"')
            return f"+7{telephone_number}"
        except ValueError as e:
            print(e)
            