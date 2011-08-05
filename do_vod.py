#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
pour faire les pages de VOD

Ce programme crée 2 fichiers :
page : page html dynamique, qui permet de présenter tous les films dans la même page
liste : le même contenu que ci-dessus, mais dans une liste statique

les noms des fichiers sont définit ci-dessous

"""

import os, sys
from langues import create_js
from FOIlib import VodPage

debug = 0 # mettre à 1 pour debugger, le nom des fichiers de sortie est changé et le prgm donne des info

class Config(object):
    """Config is a holder for configuration variables"""
    pass

config = Config()
config.debug = debug
#le nom des fichiers de sortie
if debug:
    config.page_name = "indexd.html"
    config.page_name_en = "indexd_en.html"
    config.liste_name = "listed.html"
    config.liste_name_en = "listed_en.html"
else:
    config.page_name = "index.html"
    config.page_name_en = "index_en.html"
    config.liste_name = "liste.html"
    config.liste_name_en = "liste_en.html"

#le program fait un cd ici avant de commencer:
try:
    config.working_dir = os.environ["VODdir"]
except KeyError:
    raise Exception("the environment variable VODdir should be set before running, see configuration.sh")
# la valeur est effacé au lancement par argv[0]
# toutes les adresses sont ensuite relatives à cette adresse

try:
    config.video_dir = os.environ["VIDEOdir"]
except KeyError:
    raise Exception("the environment variable VIDEOdir should be set before running, see configuration.sh")
# la valeur est effacé au lancement par argv[0]
# toutes les adresses sont ensuite relatives à cette adresse

#là où l'on trouve les fichiers annexes
try:
    config.PrgmDir = os.environ["MAKEdir"]
except KeyError:
    raise Exception("the environment variable MAKEdir should be set before running, see configuration.sh")
# html templates

config.TmplDir = os.path.join(config.PrgmDir, "tmpl")



###################################################################################
# Fait le travail
def main(config):
    try:
        config.working_dir = sys.argv[1]
    except:
        pass
    os.chdir(config.working_dir)
    # pages en français
    H1 = VodPage(config, "FR")
    ffr = open(os.path.join(config.working_dir, config.page_name),'w')
    ffr.writelines( H1.vod_html() )
    ffr.close()
    fgr = open(os.path.join(config.working_dir, config.liste_name),'w')
    fgr.writelines( H1.liste_html() )
    fgr.close()
    # pages en anglais
    H2 = VodPage(config, "EN")
    ffe = file(os.path.join(config.working_dir, config.page_name_en),'w')
    ffe.writelines( H2.vod_html() )
    ffe.close()
    fge = open(os.path.join(config.working_dir, config.liste_name_en),'w')
    fge.writelines( H2.liste_html() )
    fge.close()
    # langues.js remis à jour - nécessaire que quand on change langues.py, mais fait ici "pour être sûr"
    create_js()
    return 0

if __name__ == "__main__":
	sys.exit(main(config))

