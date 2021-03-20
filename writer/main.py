#usr/bin/python3
import os
import sys
from optparse import OptionParser
from optparse import IndentedHelpFormatter
from pyfiglet import Figlet
import pickle


print(Figlet(font='slant').renderText('HiTranslator'))
class NoWrapFormatter(IndentedHelpFormatter) :
    def _format_text(self, text) :
        "[Does not] format a text, return the text as it is."
        return text

parser = OptionParser(prog='HiTranslator Writer',
                              usage="",
                              description="HiTranslator Writer",
                              version="1.0",
                              formatter=NoWrapFormatter(),
                              epilog="""Thanks for using!
                              """)

#源语言,程序语言/自定义语言规则,是否首次,是否已注释方式将翻译信息保存至文件,完整/直接trs函数,

#是否手动引入SDK,是否完整回显,
#日志级别

parser.add_option("-pd", "--projectdir",
                 dest="工程根目录",
                help="工程根目录")                
parser.add_option("-htp", "--htproject",
                 dest="HT工程根目录",
                help="HT工程根目录,留空则定位于工程根目录下的HTProject文件夹.")       
parser.add_option("-f", "--first",
                 dest="是否首次", default='True',
                help="是否首次")
parser.add_option("-isa", "--issave",
                 dest="是否已注释方式将翻译信息保存至文件", default="False",
                help="是否已注释方式将翻译信息保存至文件")                
parser.add_option("-full", "--isfullfunc",
                 dest="完整/直接trs函数", default='False',
                help="完整/直接trs函数")
parser.add_option("-isd", "--isautosdk",
                 dest="是否手动引入SDK",
                help="是否手动引入SDK")
parser.add_option("-ifb", "--isfullback",
                 dest="是否完整回显",
                help="是否完整回显")
parser.add_option("-log", "--loglevel",
                 dest="日志级别",
                help="日志级别")                            
(options, args) = parser.parse_args()

