# -*- coding: utf-8 -*-

"""
Pour écrire la page de présentation du film

"""
from FOIlib import presentation
import sys


def main():
    try:
        c = sys.argv[1]
    except:
        raise Exception("""\
La syntaxe normale est :
python presentation.py video_dir

le programme construit la page dans video_dir
""")
    D = presentation(c)
    D.setLang("FR")
    D.do_html()
    D.setLang("EN")
    D.do_html()

if __name__ == "__main__":
    main()
