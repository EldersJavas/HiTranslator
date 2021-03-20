#http://www.coolpython.net/python_senior/project/config_xml.html
import  xml.dom.minidom

dom = xml.dom.minidom.parse('db.xml')
root = dom.documentElement      # 获得根节点
print(root.nodeName)            # 节点名称 dbconfig

# 获取mysql节点
mysql_node = root.getElementsByTagName('mysql')[0]
for node in mysql_node.childNodes:
    if node.nodeType == 1:   # ELEMENT_NODE
        print(node.nodeName, node.firstChild.data)