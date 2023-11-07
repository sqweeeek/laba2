class Validator:

    def __init__(self):
        pass

    def isEmail(self, str):
        return ('@' in str) and ('.' in str)

    def isPhone(self, str):
        if len(str.split("-")) == 5:
            return True


    def isDomain(self, domain):
        return ('.' in domain)




email = "example@example.com"
phone_number = "+381"
dom = "lol.ru"
validator = Validator()

if validator.isEmail(email):
    print("Email корректен")
else:
    print("Email некорректен")

if validator.isDomain(dom):
    print("домен корректен")
else:
    print("домен некорректен")
if validator.isPhone(phone_number):
    print("Номер телефона корректен")
else:
    print("Номер телефона некорректен")
