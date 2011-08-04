# -*- coding: utf-8 -*-

"""
Ce fichier contient les définitions des langues utilisées

copyright Communauté du Chemin-Neuf
ne pas utiliser sans authorisation
ATTENTION codage UTF-8 impératif !

"""
__author__ = "M-A.Delsuc"
__version__ = "1.2 feb 2009"
__copy__ = "Communauté du Chemin-Neuf"

import os

# le nom des mois en français
mois_nom =  [" ","janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
mois_nom_court =  [" ","jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

# le nom des mois en anglais
month_name =[" ","January","February","March","April","May","June","July","August","September","October","November","December"]

# le nom des langues en français
langues = {'FR':'Français', 'EN':'Anglais', 'DE':'Allemand', 'ES':'Espagnol', 'IT':'Italien','PT':'Portugais',
        'HU':'Hongrois','NL':'Néerlandais','CS':'Tchèque','SK':'Slovaque','LV':'Letton','PL':'Polonais','RU':'Russe', 'LT':'Lituanien',
        'TR':'Turc', 'AR':'Arabe','HY':'Arménien','ZH':'Chinois','JA':'Japonais','VI':'Vietnamien',
        'MOS':'Mooré','LN':'Lingala','RN':'Kirundi','MU':'Créole Mauricien','MG':'Malgache'}

# le nom des langues en anglais
languages = {'FR':'French', 'EN':'English', 'DE':'German', 'ES':'Spanish','IT':'Italian','PT':'Portuguese',
        'HU':'Hungarian','NL':'Dutch','CS':'Czech','SK':'Solvak','LV':'Latvian','PL':'Polish','RU':'Russian', 'LT':'Lithuanian',
        'TR':'Turkish','AR':'Arabic','HY':'Armenian','ZH':'Chinese','JA':'Japanese','VI':'Vietnamese',
        'MOS':'Mossi','LN':'Lingala','RN':'Kirundi','MU':'Mauritian Creole','MG':'Malagasy'}

# le nom des langues dans leur propres langue
lang_self = {'FR':'Français', 'EN':'English', 'DE':'Deutsch', 'ES':'Español','IT':'Italiano','PT':'Português',
        'HU':'Magyar','NL':'Nederlands','CS':'Česky','SK':'Slovenčina','LV':'Latviski','PL':'Polski','RU':'Pусский', 'LT':'Lietuviškai',
        'TR':'Türkçe','AR':'العربية','HY':'Հայերեն','ZH':'漢語','JA':'日本語','VI':'Tiếng Việt',
        'MOS':'Mòoré','LN':'Lingala','RN':'Kirundi','MU':'Kreol moricien','MG':'Malagasy'}

# le mot résumé dans qq langues
resume = {
    "CS" : "Shrnutí",
    "DE" : "Zusammenfassung",
    "EN" : "Summary",
    "ES" : "Resumen",
    "FR" : "Résumé",
    "HU" : "összefoglaló ",
    "HY" : "Սեղմագիր",
    "IT" : "Riassunto",
    "LT" : "Trumpai",
    "LV" : "Kopsavilkums",
    "NL" : "Samenvatting",
    "PL" : "Streszczenie",
    "PT" : "Resumo",
    "RU" : "Краткое содержание",
    "SK" : "Zhrnutie"}

# l'ordre des langues
ordrelangues = 'FR EN DE ES IT PT HU NL CS SK LV LT PL RU TR HY AR ZH JA VI MOS LN RN MU MG'

def create_js(filename=None):
    """crée un fichier javascript qui sera utilisable dans les pages WEB"""
    import datetime
    if not filename:
        filename = os.environ["WEBROOT"] + "/js/langues.js"
    F=file(filename,'w')
    now = datetime.datetime.now()
    F.writelines("""// Javascript library for handling various foreign languages
// automatically created by langues.py script
// copyright - M-A Delsuc, Communauté du Chemin-Neuf, do not use without authorization
// created on %s
var FRLang = new Object();
var ENLang = new Object();
var SelfLang = new Object();
var ResLang = new Object();
"""%(now))
    for l in ordrelangues.split():
        F.writelines("FRLang['%s'] = '%s'\n"%(l,langues[l]))
        F.writelines("ENLang['%s'] = '%s'\n"%(l,languages[l]))
        F.writelines("SelfLang['%s'] = '%s'\n"%(l,lang_self[l]))
        try:
            res = resume[l]
        except:
            res = resume["FR"]
        F.writelines("ResLang['%s'] = '%s'\n"%(l,res))
    F.close()
        
def report():
    """Produit la table des langues utilisées"""
    print "Liste des langues disponibles :"
    print "=================================================================================================="
    print "code:   en français\t-\ten anglais\t-\tdans la langue\t-\tle mot résumé"
    print "=================================================================================================="
    for l in ordrelangues.split():
        try:
            res = resume[l]
        except:
            res = "-"
        print "%3s : %15s\t-\t%15s\t-\t%15s\t-\t%15s"%(l, langues[l], languages[l], lang_self[l], res)
#        print (l,langues[l],languages[l],lang_self[l])

# le code suivant n'est exécuté que si on appelle directement le programme
if __name__ == '__main__':
    report()
    create_js()
