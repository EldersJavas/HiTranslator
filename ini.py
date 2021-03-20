from configparser import ConfigParser


cf = ConfigParser()
cf.read('db.ini')

print(cf.sections())        # ['mysql', 'redis']
print(cf.options('mysql'))  # 输出mysql下的所有配置项
print(cf.items('mysql'))    # 输出mysql下的所有键值对

print(cf.get('mysql', 'host'))  # 输出mysql 下配置项host的值
print(cf.getint('mysql', 'port'))  # 输出port