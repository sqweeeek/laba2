class Validator:

    def __init__(self):
        pass

    def isEmail(self, str):
        return ('@' in str) and ('.' in str)




email = "examp@example.com"

validator = Validator()

if validator.isEmail(email):
    print("Email корректен")
else:
    print("Email некорректен")