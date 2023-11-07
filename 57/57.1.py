class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def get_weekday_number(self):
       
        import datetime
        weekday_number = datetime.date(self.year, self.month, self.day).weekday()
        return weekday_number

    def get_weekday_name(self):
      
        import calendar
        weekday_number = self.get_weekday_number()
        weekday_name = calendar.day_name[weekday_number]
        return weekday_name

    def get_month_name(self):
      
        import calendar
        month_name = calendar.month_name[self.month]
        return month_name


date = Zate(2023, 11, 7)
print(date.get_year())  
print(date.get_month()) 
print(date.get_day())
print(date.get_weekday_number())  
print(date.get_weekday_name()) 
print(date.get_month_name())  