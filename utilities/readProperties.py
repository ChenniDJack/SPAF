import configparser

config = configparser.RawConfigParser()

config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info', "baseURL")
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', "userName")
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', "password")
        return password