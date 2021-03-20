#!/usr/bin/python3

# CGI处理模块
import cgi, cgitb 

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')

print ("Content-type:text/html")
print ()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>CGI</title>")
print ("</head>")
print ("<body>")
print ("<h2>%s,%s</h2>" % (site_name, site_url))
print ("</body>")
print ("</html>")