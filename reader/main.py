#usr/bin/python3

import os
import init
import sys
from optparse import OptionParser
from optparse import IndentedHelpFormatter
from pyfiglet import Figlet


print(Figlet(font='slant').renderText('HiTranslator'))

class NoWrapFormatter(IndentedHelpFormatter) :
    def _format_text(self, text) :
        "[Does not] format a text, return the text as it is."
        return text

parser = OptionParser(prog='HiTranslator Reader',
                              usage="",
                              description="HiTranslator Reader",
                              version="1.0",
                              formatter=NoWrapFormatter(),
                              epilog="""Thanks for using!
                              """)

#源语言,程序语言/自定义语言规则,是否首次,是否已部署trs函数,trs函数是否带ID,

#自定义指定/排除函数规则,自定义指定/排除字符串规则,
#工程根目录,HT工程根目录,强制使用格式

parser.add_option("-rl", "--rlang",
                 dest="源语言", default="en",
                help="Language which used by project")

parser.add_option("-pl", "--plang",
                 dest="程序语言/自定义语言规则",
                help="程序语言/自定义语言规则")
parser.add_option("-f", "--first",
                 dest="是否首次", default='True',
                help="是否首次")
parser.add_option("-trs", "--istrs",
                 dest="是否已部署trs函数", default='False',
                help="是否已部署trs函数")                
parser.add_option("-id", "--isid",
                 dest="trs函数是否带ID", default='False',
                help="trs函数是否带ID")
parser.add_option("-fun", "--funcrrule",
                 dest="自定义指定/排除函数规则",
                help="自定义指定/排除函数规则")
parser.add_option("-str", "--stringrule",
                 dest="自定义指定/排除字符串规则",
                help="自定义指定/排除字符串规则")
parser.add_option("-pd", "--projectdir",
                 dest="工程根目录",
                help="工程根目录")                
parser.add_option("-htp", "--htproject",
                 dest="HT工程根目录",
                help="HT工程根目录")                
parser.add_option("-qz", "--qzfommat",
                 dest="强制使用格式", default='False',
                help="强制使用格式")                
                                
(options, args) = parser.parse_args()





