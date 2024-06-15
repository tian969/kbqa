import configparser

config = configparser.ConfigParser()
config.read('.\\config.ini')
print(config['guanfang_data']['pdf_path'])