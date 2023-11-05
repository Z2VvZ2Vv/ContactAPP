#  _____                _                 _              _____   _____
# / ____|              | |               | |      /\    |  __ \ |  __ \
#| |       ___   _ __  | |_   __ _   ___ | |_    /  \   | |__) || |__) |
#| |      / _ \ | '_ \ | __| / _` | / __|| __|  / /\ \  |  ___/ |  ___/
#| |____ | (_) || | | || |_ | (_| || (__ | |_  / ____ \ | |     | |
# \_____| \___/ |_| |_| \__| \__,_| \___| \__|/_/    \_\|_|     |_|
#
# v1 by Geoffrey


class Contact(object):
    def __init__(self, name, phoneNumber,email):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
    
    def getName(self):
        return self.name

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    def setName(self, name):
        self.name = name

    def setPhoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def setEmail(self, email):
        self.email = email

    def __str__(self):
        return "| " + self.name + " | " + self.phoneNumber + " | " + self.email + " |"