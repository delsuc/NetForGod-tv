# -*- coding: utf-8 -*-

"""
Pour écrire la page du résumé


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
    D=resume(c)
    if not D.empty:
        D.setLang("FR")
        D.do_html()
        D.setLang("EN")
        D.do_html()
    else:
    #    print "pas de resume pour ",c
	pass

if __name__ == "__main__":
    main()
