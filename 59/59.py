class Month:
    def __init__(self, month_number):
        self.month_number = month_number

    def get_month_number(self):
        return self.month_number

    def get_month_name(self):
        month_names = {1 : 'Январь', 2 : 'Февраль', 3 : 'Март', 4 : 'Апрель',
                           5 : 'Май', 6 : 'Июнь', 7 : 'Июль', 8 : 'Август',
                           9 : 'Сентябрь', 10 : 'Октябрь', 11 : 'Ноябрь', 12 : 'Декабрь'}
        return month_names[self.month_number - 1]

    def get_last_day_of_month(self):
        if self.month_number in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month_number in [4, 6, 9, 11]:
            return 30
        else: 
            return 28 

    def get_first_day_of_week(self):
       
        return (self.month_number + 2) % 7 + 1

    def get_last_day_of_week(self):
        last_day = self.get_last_day_of_month()
        first_day = self.get_first_day_of_week()
        return (first_day + last_day - 1) % 7 + 1