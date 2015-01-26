#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Un mini parseur SAX
usage :
python test.py infile.xml key  default_value

imprime la valeur de "key" dans le xml, si elle est de la forme
<key value="val" />
imprime default_value si 'key' est maquante
"""
import sys, string
from xml.sax import handler, make_parser

class ParamHandler(handler.ContentHandler):
    """\
    la classe qui fait tout :
    ParamHandler(cle_a_parser, val_par_def_si_absente)
    """
    def __init__(self,key,default):
        self.value=default
        self.key=key

    def startElement(self, name, attrs):
        if name==self.key:
            self.value=attrs.get("value")
            

def test(inFileName,key,default):
    handler = ParamHandler(key,default)
    parser = make_parser()
    parser.setContentHandler(handler)
    try:
        parser.parse(inFileName)
    except:
        pass
    print handler.value

def main():
    args = sys.argv[1:]
    if len(args) != 3:
        print __doc__
        sys.exit(-1)
    test(args[0],args[1],args[2])

if __name__ == '__main__':
    main()


