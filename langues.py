# -*- coding: utf-8 -*-

"""
Ce fichier contient les définitions des langues utilisées

copyright Communauté du Chemin-Neuf
ne pas utiliser sans authorisation
ATTENTION codage UTF-8 impératif !

pour rajouter une langue, rajouter une entrée dans langues, languages, lang_self et éventuellement résumé
rajouter son nom à ordrelangues 

Attention:
si vous voulez garder la compatibilité avec une version antérieur du sit, il faut obligatoirement rajouter A LA FIN de ordrelangues 
"""
__author__ = "M-A.Delsuc"
__version__ = "1.3 oct 2011"
__copy__ = "Communaute du Chemin-Neuf"
import codecs

# le nom des mois en français
mois_nom =  [u" ",u"janvier",u"février",u"mars",u"avril",u"mai",u"juin",u"juillet",u"août",u"septembre",u"octobre",u"novembre",u"décembre"]
mois_nom_court =  [" ","jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]

# le nom des mois en anglais
month_name =[" ","January","February","March","April","May","June","July","August","September","October","November","December"]

# le nom des langues en français
langues = {'FR':u'Français', 'EN':u'Anglais', 'DE':u'Allemand', 'ES':u'Espagnol', 'IT':u'Italien','PT':u'Portugais',
        'HU':u'Hongrois','NL':u'Néerlandais','CS':u'Tchèque','SK':u'Slovaque','LV':u'Letton','PL':u'Polonais','RU':u'Russe', 'LT':u'Lituanien',
        'TR':u'Turc', 'AR':u'Arabe','HY':u'Arménien','ZH':u'Chinois','JA':u'Japonais','VI':u'Vietnamien',
        'MOS':u'Mooré','LN':u'Lingala','RN':u'Kirundi','MU':u'Créole Mauricien','MG':u'Malgache'}

# le nom des langues en anglais
languages = {'FR':'French', 'EN':'English', 'DE':'German', 'ES':'Spanish','IT':'Italian','PT':'Portuguese',
        'HU':'Hungarian','NL':'Dutch','CS':'Czech','SK':'Solvak','LV':'Latvian','PL':'Polish','RU':'Russian', 'LT':'Lithuanian',
        'TR':'Turkish','AR':'Arabic','HY':'Armenian','ZH':'Chinese','JA':'Japanese','VI':'Vietnamese',
        'MOS':'Mossi','LN':'Lingala','RN':'Kirundi','MU':'Mauritian Creole','MG':'Malagasy'}

# le nom des langues dans leur propres langue
lang_self = {'FR':u'Français', 'EN':u'English', 'DE':u'Deutsch', 'ES':u'Español','IT':u'Italiano','PT':u'Português',
        'HU':u'Magyar','NL':u'Nederlands','CS':u'Česky','SK':u'Slovenčina','LV':u'Latviski','PL':u'Polski','RU':u'Pусский', 'LT':u'Lietuviškai',
        'TR':u'Türkçe','AR':u'العربية','HY':u'Հայերեն','ZH':u'漢語','JA':u'日本語','VI':u'Tiếng Việt',
        'MOS':u'Mòoré','LN':u'Lingala','RN':u'Kirundi','MU':u'Kreol moricien','MG':u'Malagasy'}

# le mot résumé dans qq langues
resume = {
    "CS" : u"Shrnutí",
    "DE" : u"Zusammenfassung",
    "EN" : u"Summary",
    "ES" : u"Resumen",
    "FR" : u"Résumé",
    "HU" : u"összefoglaló ",
    "HY" : u"Սեղմագիր",
    "IT" : u"Riassunto",
    "LT" : u"Trumpai",
    "LV" : u"Kopsavilkums",
    "NL" : u"Samenvatting",
    "PL" : u"Streszczenie",
    "PT" : u"Resumo",
    "RU" : u"Краткое содержание",
    "SK" : u"Zhrnutie"}

# l'ordre des langues
ordrelangues = 'FR EN DE ES IT PT HU NL CS SK LV LT PL RU TR HY AR ZH JA VI MOS LN RN MU MG'

def create_js(filename="langues.js"):
    """crée un fichier javascript qui sera utilisable dans les pages WEB"""
    import datetime
    F=codecs.open(filename,'w',encoding='utf-8')    # open to write in utf-8
    now = datetime.datetime.now()
    F.writelines(u"""// Javascript library for handling various foreign languages
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

def phparray(liste):
    "concatenate list entries for php"
    st = "array('%s'"%(liste[0])
    for l in liste[1:]:
        st += ", '%s'"%(l)
    st += ")"
    return st
def phpdict(dico):
    "concatenate dict entries for php"
    st = "array('%s'=>'%s'"%(dico.items()[0])
    for (k,v) in dico.items()[1:]:
        st += ", '%s'=>'%s'"%(k,v)
    st += ")"
    return st
    
def create_php(filename="langues.php"):
    """crée un fichier php qui sera utilisable dans les pages WEB"""
    import datetime
    F=codecs.open(filename,'w',encoding='utf-8')    # open to write in utf-8
    now = datetime.datetime.now()
    F.writelines(u"""<?php
// library for handling various foreign languages
// automatically created by langues.py script
// copyright - M-A Delsuc, Communauté du Chemin-Neuf, do not use without authorization
// created on %s

"""%(now))
    F.writelines(u"$ordrelangues = "+phparray(ordrelangues.split()+['MUL'])+";\n")
    F.writelines(u"\n// le nom des mois en français\n")
    F.writelines(u"$mois_nom = "+phparray(mois_nom)+";\n")
    F.writelines(u"$mois_nom_court = "+phparray(mois_nom_court)+";\n")
    F.writelines(u"\n// le nom des mois en anglais\n")
    F.writelines(u"$month_name = "+phparray(month_name)+";\n")
    F.writelines(u"\n// le nom des langues en français\n")
    langues['MUL'] = 'multiple'
    F.writelines(u"$langues = "+phpdict(langues)+";\n")
    F.writelines(u"\n// le nom des langues en anglais\n")
    F.writelines(u"$languages = "+phpdict(languages)+";\n")
    F.writelines(u"\n// le nom des langues le nom des langues dans leur propres langue\n")
    F.writelines(u"$lang_self = "+phpdict(lang_self)+";\n")
    F.writelines(u"\n// le mot resume\n")
    F.writelines(u"$resume = "+phpdict(resume)+";\n")
    F.close()
        
def report():
    """Produit la table des langues utilisées"""
    print u"Liste des langues disponibles :"
    print u"=================================================================================================="
    print u"code:   en français\t-\ten anglais\t-\tdans la langue\t-\tle mot résumé"
    print u"=================================================================================================="
    for l in ordrelangues.split():
        try:
            res = resume[l]
        except:
            res = "-"
        print "%3s : %15s\t-\t%15s\t-\t%15s\t-\t%15s"%(l, langues[l], languages[l], lang_self[l], res)
#        print (l,langues[l],languages[l],lang_self[l])

# le code suivant n'est exécuté que si on appelle directement le programme
# typiquement au moment du deploiment
if __name__ == '__main__':
    report()
    create_js()
    create_php()