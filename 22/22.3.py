class Validator:

    def __init__(self):
        pass

    def isEmail(self, str):
        return ('@' in str) and ('.' in str)

    def isDomain(self, domain):
        return ('.' in domain)




email = "examp@example.com"
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