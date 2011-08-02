#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
pour faire les pages de VOD

Ce programme crée 2 fichiers :
page : page html dynamique, qui permet de présenter tous les films dans la même page
liste : le même contenu que ci-dessus, mais dans une liste statique

les noms des fichiers sont définit ci-dessous

"""

import glob
import re
import os, sys
import langues

debug = 0 # mettre à 1 pour debugger, le nom des fichiers de sortie est changé et le prgm donne des info

#le nom des fichiers de sortie
if debug:
    page_name = "indexd.html"
    page_name_en = "indexd_en.html"
    liste_name = "listed.html"
    liste_name_en = "listed_en.html"
else:
    page_name = "index.html"
    page_name_en = "index_en.html"
    liste_name = "liste.html"
    liste_name_en = "liste_en.html"

#le program fait un cd ici avant de commencer:
try:
    working_dir = os.environ["VODdir"]
except KeyError:
    raise Exception("the environment variable VODdir should be set before running, see configuration.sh")
# la valeur est effacé au lancement par argv[0]
# toutes les adresses sont ensuite relatives à cette adresse

#le dossier où sont les videos
# les video sont cherchée dans les sous dossier de dir_video
try:
    dir_video = os.environ["VIDEOdir"]
except KeyError:
    raise Exception("the environment variable VIDEOdir should be set before running, see configuration.sh")

#là où l'on trouve les fichiers annexes
PrgmDir=os.path.realpath(os.curdir)


def clean(st):
   """nettoie les characteres interdit"""
   return st.replace("&","&amp;").replace("'","&#x27;").replace('"',"&quot;").replace("\n","<br/>").replace("\r","")
###################################################################################

class VodPage:
    """ Cette classe fait tout le travail  """
    import os, sys
    global PrgmDir
    
    def __init__(self,langue="FR"):
        self.langue=langue
        self.dir=dir_video
        self.flv_list = self.do_flv_list()
        self.titre_list=self.do_titre_list()
        self.langues_list=self.do_lang_list()
        self.resum_list=self.do_resum_list()
        self.diapo_list=self.do_diapo_list()

    def html_base_liste(self):
        """charge la base de la page html pour le VOD en mode liste"""
        import os.path as op
        if (self.langue == "FR"):
            VOD=file(op.join(PrgmDir,"vod_list_fr.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        else:
            VOD=file(op.join(PrgmDir,"vod_list_en.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        return r

    def html_base_vod(self):
        """charge la base de la page html pour le VOD."""
        import os.path as op
# base html de la page -  2 versions _fr et _en - les champs %s sont remplacés au moment de l'utilisation
        if (self.langue == "FR"):
            VOD=file(op.join(PrgmDir,"vod_fr.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        else:
            VOD=file(op.join(PrgmDir,"vod_en.html"))
            r = "".join(VOD.readlines())
            VOD.close()
        return r
    ###################################################################################
    def vod_html(self):
        """ cree la page html VOD dans la langue cible"""
        import os.path as op
        # calcule toutes les parties variables
        flv = str(self.flv_list).replace('[','').replace(']','')
        titre = ""
        for i in self.titre_list:
                if titre == "":
                        titre = "'" + i + "'"
                else:
                        titre = titre + ", '" + i + "'"
        langs = repr(self.langues_list).replace('[','').replace(']','')
        if self.langue == "FR":
            autrepage = page_name_en
        else:
            autrepage = page_name
        video_du_mois = self.do_mois()
        table_video = self.do_emisions()
        Ares = repr(self.resum_list).replace('[','').replace(']','') 
        Adia = repr(self.diapo_list).replace('[','').replace(']','')
        Adur = []
        debit = 1100
        for i in self.flv_list:
            dur = op.getsize(op.join(self.dir,i,"FR_divx.avi"))
            dur = round(dur*8/debit/60/1024)
            if debug: print i,dur," min"
            Adur.append(dur)
        
        # et colle le dans le html grace à vars qui retourne un dico des var locales
        return (self.html_base_vod() % vars())

    ###################################################################################
    def liste_html(self):
        """ cree la page html VOD mode liste dans la langue cible"""
        # calcul toutes les parties variables
        flv = str(self.flv_list).replace('[','').replace(']','')
        titre = ""
        for i in self.titre_list:
                if titre == "":
                        titre = "'" + i + "'"
                else:
                        titre = titre + ", '" + i + "'"
        langs = repr(self.langues_list).replace('[','').replace(']','')
        if self.langue == "FR":
            autrepage = liste_name_en
        else:
            autrepage = liste_name
        liste_video = self.do_liste_emmission()
        # et colle le dans le html grace à vars qui retourne un dico des var locales
        return (self.html_base_liste() % vars())

    ###################################################################################
    def do_flv_list(self):
        """ fabrique la liste des flv dans la langue cible
        cherche dans tous les sous-dossiers de self.dir, un fichier XX_divx.flv
        si le dossier contient un fichier au nom de public, alors l'entrée est rajoutée
        au passage, crée tous les liens entre self.dir (là où sont vraiment les video) et working_dir (là où sont les pages de visu)
        retourne la liste des dossiers rajoutés dans working_dir
        l'ordre de Cette liste determine l'ordre des videos - par defaut c'est l'ordre anti alphabetique
        si un dossier contient un fichier (vide) "premier" alors il est mis en tete
        """
        import os.path as op
        try:
            motif = self.langue+"_divx.flv"
        except:
            motif = "FR_divx.flv"
        l1=[]
        prem = ""
        for dir in glob.glob(op.join(self.dir,"*")): # pour tout les directory
            if op.isdir(dir):  
                if op.isfile(op.join(dir,"public")) and op.isfile(op.join(dir,motif)):   # qui contiennent le fichier "public" et contient au moins une video
                    if debug : print dir
                    new_dir = self.makelink(dir,working_dir)
                    l1.append(op.basename(new_dir))
                    if op.isfile(op.join(dir,"premier")):
                        prem = op.basename(new_dir)
        l1.sort()
        l1.reverse()
        if prem:
            l1.remove(prem)
            l1.insert(0,prem)
        # lien permanent vers le film du mois
        actuel = op.join(working_dir,"actuel")
        try:
            os.remove(actuel)
        except:
            pass
        os.symlink ( op.join(working_dir,l1[0]), actuel)
        if debug: print "flv_list", l1
        return (l1)
    
    ###################################################################################
    def makelink(self,source,cible):
        """s'asure que tout les liens entres les dossiers source (video) et cible (VOD) sont là"""
        import os.path as op
        import glob
        # source : self.dir/MyMovie   -  cible : VOD   -  dir : VOD/MyMovie
        dir = op.join(cible,op.basename(source))
        # create dir
        if not op.isdir(dir):
            os.mkdir(dir)
        # link flvs
        for flv in glob.glob(source+"/*.flv"):
            new_flv=op.join(dir,op.basename(flv))
            if not op.islink(new_flv):
                print "LINK", flv, new_flv
                try: 
                  os.symlink(flv, new_flv)
                except:
                  raise "Probleme avec ln -s %s %s"%(flv, new_flv)
        # affiche, textes, images
        for F in ("affiche.jpg", "textes", "images", "thumbs", "presentation.html","presentation_EN.html","diaporama.html","diaporama_FR.html","diaporama_EN.html","resume.html","resume_FR.html","resume_EN.html","gallery_EN.xml","gallery_FR.xml"):
            old_F=op.join(source,F)
            new_F=op.join(working_dir,dir,F)
            if not op.islink(new_F) and op.exists(old_F):
               print "LINK", old_F, new_F
               try:
                   os.symlink(old_F, new_F)
               except:
                   print "probleme avec ln -s %s %s"%(old_F, new_F)
        return dir

    ###################################################################################
    def strip_flv(self,l):
        import os.path as op
        """ reformate un flv, pour ne garder que la base des noms
        i.e. FOI_06_07/FR_divx.flv => FOI_06_07
        plus utilisé
        """
#        motif = "_"+self.langue+"_"
        motif = "_FR_"
        l2 = l.replace(motif + "divx.flv","")
        return( op.basename(l2) )
    
    ###################################################################################
    def do_titre_list(self):
        import os.path as op
        """ fabrique la liste des titre dans la langue cible"""
        t = []
        for i in self.flv_list:
            try:
                f=file ( op.join( i, "textes", "titre_" + self.langue + ".txt"))
                tx = clean(f.read())
                t.append(tx)
                f.close()
            except:
                t.append("--")
        return (t)
    
    ###################################################################################
    def do_lang_list(self):
        """ fabrique la liste des langues pour chaque video trouvée"""
        import os.path as op
        l = []  # pour chaque entrée
        for base in self.flv_list:
            f = glob.glob( op.join(base,"*divx.flv"))
            ll = ""     # liste des langues pour chaque entrée
            for j in langues.ordrelangues.split():    # sur toutes les langues
                for k in f:     # sur tous les fichiers
                    try:
                       [ll1] = re.findall("([A-Z][A-Z]+)_divx",  k)
                       if j == ll1:
                           if ll=="":
                               ll=ll1
                           else:
                               ll = ll+" "+ll1
                    except:
                       if debug: print "langue inconnue: ",k
            l.append(ll)
        return(l)
    ###################################################################################
    def do_resum_list(self):
        """fabrique un tableau de test (0/1) pour la présence d'un résumé """
        import os.path as op
        l = []  # pour chaque entrée
        for base in self.flv_list:
            if op.exists(op.join(base,"textes/resume_FR.txt")):
                l.append(1)
            else:
                l.append(0)
        return(l)
    ###################################################################################
    def do_diapo_list(self):
        """fabrique un tableau de test (0/1) pour la présence d'un diaporama """
        import os.path as op
        l = []  # pour chaque entrée
        for base in self.flv_list:
            if op.exists(op.join(base,"diaporama.html")):
                l.append(1)
            else:
                l.append(0)
        return(l)
    
    ###################################################################################
    def do_emisions(self):
        import os.path as op
        """ fabrique la table des emissions précédentes pour la page VOD"""
        tabl = ""
        cote="g"    # cote alterne g / d pour faire le tableau
        if len(self.flv_list)>1:        # tout sauf la dernière qui est à part
            liste = self.flv_list[1:]
            index=1
        else:
            liste=self.flv_list
            index=0
        for i in liste:
            index_em=index
            index +=1
            (titre,affiche,date) = self.do_ti_aff_date(i)
    # base html de la case pour une emission
            if index<6:
                emision_fr = """<span class="tdemission%s"><a href="#" onclick="javascript:PresMois(%d)"><img border="0" class="affiche-2" alt="affiche" src="%s"/><br clear="all"/><span class="titre"> %s </span></a></span>\n""" % (cote,index_em, affiche,titre)
            else:
                emision_fr = """<span class="tdemission%s_sm"><a href="#" onclick="javascript:PresMois(%d)"><span class="titre"> %s </span></a></span>\n""" % (cote,index_em,titre)
            if (cote == "g"):
                cote = "d"
            else:
                cote = "g"
            tabl = tabl + emision_fr
        if (cote == "d"):
            tabl = tabl+"""<span class="tdemissiond_sm">&nbsp;</span>\n"""
        return (tabl)
    ###################################################################################
    def do_liste_emmission(self):
        import os.path as op
        """ fabrique la table des emissions précédentes pour la page liste """
        texte=""
        # base html de la case pour une emission
        base="""
        <div class="ltfilm">
        <a href="%(perm)s?dt=%(dt)s&lg=%(langue)s"><img border="0" class="affiche-2" alt="affiche" src="%(affiche)s"/></a>
        <p class="date-lt">%(date)s</p>
        <p class="lttitre">%(titre)s</p>
        </div>
        """
        texte=""
        for dir in self.flv_list:
            (titre,affiche,date) = self.do_ti_aff_date(dir)
            [(dt)] = re.findall("FOI_(\d\d_\d\d)",dir)
            langue = self.langue
            if self.langue == "FR":
                perm = "perm.php"
            else:
                perm = "permn.php"
            texte=texte+base % vars()
        return (texte)
    
    ###################################################################################
    def do_mois(self):
        """ fabrique la presentation du mois courant """
        import os.path as op
        i=self.flv_list[0]
        (titre,affiche,date) = self.do_ti_aff_date(i)
        mois = """<p class="titre-mois"> %s </p><div class="aff-mois"><a href="#" onclick="javascript:PresMois(0)">
                 <img border="0" class="affiche-1" alt="affiche" src="%s"/></a></div>
                 <div class="texte-mois"> </div>""" % (titre, affiche)
        return(mois)
    
    ###################################################################################
    def do_ti_aff_date(self,dirb):
        """utilitaire pour calculer le nom et le titre"""
        import os.path as op
        try:
            f = file(  op.join(dirb, "textes", "titre_" + self.langue + ".txt"))
            titre = clean(f.read())
            f.close()
        except:
            titre="<br/>"
        affiche = op.join(dirb, "affiche.jpg")
        if not op.isfile(affiche):
            affiche = "/images/affiche.gif"
        try:
            [(annee,mois)] = re.findall("FOI_(\d\d)_(\d\d)",dirb)
            if (self.langue == "FR"):
                # if mois in ("04","08","10"):    # avril aout octobre
                #     date = "La vidéo du mois d'%s %i"%(langues.mois_nom[int(mois)],int(annee)+2000)
                # else:
                #     date = "La vidéo du mois de %s %i"%(langues.mois_nom[int(mois)],int(annee)+2000)
                date = "%s %i"%(langues.mois_nom[int(mois)],int(annee)+2000)
            if (self.langue == "EN"):
            #     date = "%s %i video"%(langues.month_name[int(mois)],int(annee)+2000)
                date = "%s %i"%(langues.month_name[int(mois)],int(annee)+2000)
        except:
            date = " "
        return ((titre,affiche,date))


###################################################################################
# Fait le travail
def main():
    global working_dir
    try:
        working_dir = sys.argv[1]
    except:
        pass
    os.chdir(working_dir)
    # pages en français
    H1 = VodPage("FR")
    ffr = open(os.path.join(working_dir,page_name),'w')
    ffr.writelines( H1.vod_html() )
    ffr.close()
    fgr = open(os.path.join(working_dir,liste_name),'w')
    fgr.writelines( H1.liste_html() )
    fgr.close()
    # pages en anglais
    H2 = VodPage("EN")
    ffe = file(os.path.join(working_dir,page_name_en),'w')
    ffe.writelines( H2.vod_html() )
    ffe.close()
    fge = open(os.path.join(working_dir,liste_name_en),'w')
    fge.writelines( H2.liste_html() )
    fge.close()
    # langues.js remis à jour - nécessaire que quand on change langues.py
    langues.create_js()

if __name__ == "__main__":
	sys.exit(main())

