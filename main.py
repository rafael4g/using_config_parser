from asyncore import read
import configparser

config = configparser.ConfigParser()

config.read("myfile.ini")

headers = config.sections()
print(headers)
# ['Diretories', 'Environments', 'Granted', 'Others']

headers_x_values = config.options("Environments")
print(headers_x_values)
# ['mysql_user', 'mysql_pass', 'mysql_host', 'mysql_port', 'mysql_curr', 'mysql_base']

headers_get_values = config.get("Environments", "mysql_user")
print(headers_get_values)
# user01