#usr/bin/python3

import os
#import xml
import init
#import read
#import cgi
import sys
from optparse import OptionParser
from optparse import IndentedHelpFormatter

class NoWrapFormatter(IndentedHelpFormatter) :
    def _format_text(self, text) :
        "[Does not] format a text, return the text as it is."
        return text

parser = OptionParser(prog='HiTranslator Format',
                              usage="",
                              description="HiTranslator searcher",
                              version="1.0",
                              formatter=NoWrapFormatter(),
                              epilog="""\Thanks
                              """)
parser.add_option("-d", "--dir", dest="Dir",
                help="Root Dir", metavar="Dir")
parser.add_option("-l", "--lang",
                 dest="Language", default=True,
                help="Language which used by project")
(options, args) = parser.parse_args()


