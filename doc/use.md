# Use
# 使用

> 使用前请确保正确安装所有核心组件,并包含所使用的默认规则文件.

## Step1 使用Writer取出全部字符串并新建工程

当你运行`Reader.exe -h`时,显示如下输出表明程序完整并可运行.

```powershell
    __  __          ______
   / / / /__  __  _/_  __/________ _____  ________  _____
  / /_/ / _ \/ / / // / / ___/ __ `/ __ \/ ___/ _ \/ ___/
 / __  /  __/ /_/ // / / /  / /_/ / / / (__  )  __/ /
/_/ /_/\___/\__, //_/ /_/   \__,_/_/ /_/____/\___/_/
           /____/

HeyTranser Reader


Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -r RLANG, --rlang=RLANG
                        Language which used by project
  -a PLANG, --plang=PLANG
                        程序语言/自定义语言规则
  -f FIRST, --first=FIRST
                        是否首次
  -t ISTRS, --istrs=ISTRS
                        是否已部署trs函数
  -i ISID, --isid=ISID  trs函数是否带ID
  -d FUNCRRULE, --funcrrule=FUNCRRULE
                        自定义指定/排除函数规则
  -s STRINGRULE, --stringrule=STRINGRULE
                        自定义指定/排除字符串规则
  -p PROJECTDIR, --projectdir=PROJECTDIR
                        工程根目录
  -o HTPROJECT, --htproject=HTPROJECT
                        HT工程根目录
  -q QZFOMMAT, --qzfommat=QZFOMMAT
                        强制使用格式

Thanks for using!
```

| 简写  | 完整  | 格式  | 意义 |  备注 |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| -r  | --rlang=  | 字符串  |  Language which used by project |  遵循`IETF`标准 |
| -a  |  --plang= |  字符串 | 程序语言/自定义语言规则  |  不要填入目前不支持的语言 |
| -f  |  --first= | T/F  |  是否首次 |  意义是是否创建新工程 |
| -t  |  --istrs= | T/F  | 是否已部署trs函数  |   |
|  -i | --isid=  | T/F  |  trs函数是否带ID |  -t 参数为F的话,此选项强制为F |
|  -d |  --funcrrule= |  字符串(文件夹目录)(可选) |  自定义指定/排除函数规则 |   |
| -s  | --stringrule=  | 字符串(文件夹目录)(可选)  |  自定义指定/排除字符串规则 |   |
| -p  |  --projectdir= | 字符串(文件夹目录)  |  工程根目录 |   |
| -o  | --htproject=  |  字符串(文件夹目录)(可选) | HT工程根目录  |  若空,则默认为项目目录下`HeyTranser`文件夹 |
|  -q | --qzfommat=  |  T/F | 强制使用格式 |  <b>若不了解,强烈建议不要选T</b> |
|  -h |  --help | 无  |  帮助 |   |
| (无)  | --version  | 空  | 输出版本  | 只返回版本,其他参数无效  |
|   |   |   |   |   |
