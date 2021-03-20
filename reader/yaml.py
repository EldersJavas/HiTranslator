#http://www.coolpython.net/python_senior/project/config_yaml.html
#pip install PyYaml
import yaml

def read():
    f = open('db.yaml')
    data = f.read()
    yaml_reader = yaml.load(data)

    print(yaml_reader['mysql'])    # 以字典的形式输出mysql下的所有配置
    print(yaml_reader['redis']['port'])     # 输出某一项
    print(yaml_reader['db_ip'])     # db_ip配置是一个数组
def write():
    inputdata={
    "url":'https://www.baidu.com/',
    "driver":['ie','chrome','firfox']
}