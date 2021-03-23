import yaml

f = open(r"E:\workspace\HiTranslator\HiTranslator\reader\testfile\test.yaml",encoding='utf-8')
data = f.read()
print(yaml.load(data))