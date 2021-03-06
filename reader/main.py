#usr/bin/python3

import os
import sys
import pickle
from optparse import OptionParser
from optparse import IndentedHelpFormatter
#from pyfiglet import Figlet


#print(Figlet(font='slant').renderText('HeyTranser'))
"""
    __  __          ______
   / / / /__  __  _/_  __/________ _____  ________  _____
  / /_/ / _ \/ / / // / / ___/ __ `/ __ \/ ___/ _ \/ ___/
 / __  /  __/ /_/ // / / /  / /_/ / / / (__  )  __/ /
/_/ /_/\___/\__, //_/ /_/   \__,_/_/ /_/____/\___/_/
           /____/
"""
print(__doc__)
class NoWrapFormatter(IndentedHelpFormatter) :
    def _format_text(self, text) :
        "[Does not] format a text, return the text as it is."
        return text

parser = OptionParser(prog='HeyTranser Reader',
                              usage="",
                              description="HeyTranser Reader",
                              version="1.0",
                              formatter=NoWrapFormatter(),
                              epilog="""Thanks for using!
                              """)

#源语言,程序语言/自定义语言规则,是否首次,是否已部署trs函数,trs函数是否带ID,

#自定义指定/排除函数规则,自定义指定/排除字符串规则,
#工程根目录,HT工程根目录,强制使用格式

parser.add_option("-r", "--rlang",
                 dest="rlang", default="en",
                help="Language which used by project")
parser.add_option("-a", "--plang",
                 dest="plang",
                help="程序语言/自定义语言规则")
parser.add_option("-f", "--first",
                 dest="first", default='True',
                help="是否首次")
parser.add_option("-t", "--istrs",
                 dest="istrs", default='False',
                help="是否已部署trs函数")                
parser.add_option("-i", "--isid",
                 dest="isid", default='False',
                help="trs函数是否带ID")
parser.add_option("-d", "--funcrrule",
                 dest="funcrrule",
                help="自定义指定/排除函数规则")
parser.add_option("-s", "--stringrule",
                 dest="stringrule",
                help="自定义指定/排除字符串规则")
parser.add_option("-p", "--projectdir",
                 dest="projectdir",
                help="工程根目录")                
parser.add_option("-o", "--htproject",
                 dest="htproject",
                help="HT工程根目录")                
parser.add_option("-q", "--qzfommat",
                 dest="qzfommat", default='F',
                help="强制使用格式")                
                                
#(options, args) = parser.parse_args()
#opt=options
type(parser.parse_args())                       
(options, args) = parser.parse_args()



values=options.__dict__
def CheckValue(values):
    """
    values
    """
    if values['rlang']=='' :
        print("Error")
        exit()
    elif values['plang']=='':
        print("Error")
        exit()
    elif values['first']=='':
        print("Error")
        exit()
    elif values['istrs']=='':
        print("Error")
        exit()
    elif values['isid']=='':
        print("Error")
        exit()
    elif values['funcrrule']=='':
        print("Error")
        exit()
    elif values['stringrule']=='':
        print("Error")
        exit()
    elif values['projectdir']=='':
        print("Error")
        exit()
    elif values['htproject']=='':
        print("Error")
        exit()
    elif values['qzfommat']=='':
        print("Error")
        exit()
    else:
        StartStep1(values)


def StartStep1(values):
    """
    Step1
    """
    print("Step1 Starting...")




    print("Step1 Finished.")
    pass


def StartStep2(values):
    """
    Step2
    """
    print("Step2 Starting...")




    print("Step2 Finished.")    
    pass


def StartStep3(values):
    """
    Step3
    """
    print("Step3 Starting...")




    print("Step3 Finished.")
    pass


#######
#print(options['rlang'])
#rlang=options['rlang']
#plang=options["plang"]
#first=options["first"]
#istrs=options["istrs"]
#isid=options["isid"]
#funcrrule=options["funcrrule"]
#stringrule=options["stringrule"]
#projectdir=options["projectdir"]
#htproject=opt.get('htproject')
#print(opt.items())
#qzfommat=options["qzfommat"]




