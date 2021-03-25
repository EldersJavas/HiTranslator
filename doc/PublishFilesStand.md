# Publish Files Standard 
# 发布文件的标准

> 本项目长期更新,建议使用最新稳定版本.

> 本文档标准适用于`HeyTranser 1.0`

因为绝大部分高级程序语言均有`json`支持库,所以在转换为发布文件的格式暂定为首选`json`.


保留如下:
```json
    "Resource": [
        {
            "Item": {
                "ID": 1,
                "Resource": "",
                "TransResource": {},
                "Tag": "",
                "Translator": [],
                "TransTime": "",
                "IsClock": false,
                "Checker": [],
                "CheckTime": ""
            }
        },
```

并附加如下部分:
```json
    "Contributor": [],
    "Author": [],
    "Member": [],
    "ProjectName": ""
```

基本上就这些.
