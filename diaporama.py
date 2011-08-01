# -*- coding: utf-8 -*-

"""
Pour écrire la page du diaporama

Takes JPG images in a "image" directory
builds tumbnails in thumbs/
creates a gallery.xml file for simpleviewer.swf
creates a diaporama.html file to display it

"""
from FOIlib import *
import os

def main():
    try:
        c = sys.argv[1]
    except:
        raise """\
La syntaxe normale est :
python diaporama.py video_dir

le programme construit la page dans video_dir
"""
    D=diaporama(c)
    if not D.empty:
        D.images()
        D.setLang("FR")
        D.do_xml()
        D.do_html()
        D.setLang("EN")
        D.do_xml()
        D.do_html()
    else:
    #    print "pas de diaporama pour ",c
	pass

if __name__ == "__main__":
    main()
