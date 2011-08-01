# -*- coding: utf-8 -*-
"""
library for the FOI project 

Le différentes classes permettent de fabriquer pour chaque film les pages spécifiques :
diaporama : pour les visuels du film
presentation : affiche, liens vers les résumés et diaporama
index : page de base avec video, et lien vers les autres pages
"""

import langues
import os, sys

footer="""
<BR CLEAR=ALL>
<div id="pied">
<ul>
<li><a href="copyright.html">&copy; C.C.N.</a></li>
<li>| <a href="http://chemin-neuf.org">La communaut&eacute; du Chemin-Neuf </a> | </li>
<li><a href="/mentions.html">mentions l&eacute;gales</a> | </li>
<li><a href="mailto:netforgod@chemin-neuf.org?cc=nfg.webmaster@gmail.com&subject=depuis le site netforgod.tv" >contactez-nous</a> | </li>
<li>Ce site est optimis&eacute; pour Firefox</li>
</ul></div></div></div></body></html>
"""

def chop_nl(list_of_strings):
    """removes \n at the end of all lines"""
    for i in range(len(list_of_strings)):
            list_of_strings[i] = list_of_strings[i].rstrip("\n")

def clean(st):
   """nettoie les characteres interdit en HTML"""
   return st.replace("&","&amp;").replace("'","&#x27;").replace('"',"&quot;").replace("\n","<br/>").replace("\r","")

def current_title(dir):
    from os.path import join
    """ lit les fichiers titre_EN.txt et titre_FR.txt """
    import glob
    tis = glob.glob(join(dir,"textes","titre_*.txt"))
    (ti_FR,ti_EN) = (("pas de titre",),("no title",))
    for f in tis:
        if f.endswith('_FR.txt'):
            ti_FR = file(f).readlines()
            chop_nl(ti_FR)
        if f.endswith('_EN.txt'):
            ti_EN = file(f).readlines()
            chop_nl(ti_EN)
    return((ti_FR,ti_EN))

def current_resume(dir):
    from os.path import join
    """ lit les fichiers resume_EN.txt et resume_FR.txt """
    import glob
    tis = glob.glob(join(dir,"textes","resume_*.txt"))
    (ti_FR,ti_EN) = ("pas de resume","no synopsis")
    for f in tis:
        if f.endswith('_FR.txt'):
#            ti_FR = "<BR>".join(file(f).readlines())
            ti_FR = file(f).readlines()
            chop_nl(ti_FR)
        if f.endswith('_EN.txt'):
            ti_EN = file(f).readlines()
            chop_nl(ti_EN)
    return((ti_FR,ti_EN))

def current_date_2():
    import datetime
    mois = datetime.datetime.today().month
    an = datetime.datetime.today().year
    return(an,mois)

def current_date(dir):
    import re
    import time
    import os
    ici = os.path.basename(os.path.abspath(dir))
    try:
        [(annee,mois)] = re.findall("FOI_(\d\d)_(\d\d)",ici)
        annee = 2000+int(annee)
    except:
        lt = time.localtime()
        annee = lt[0]
        mois = lt[1]
    return(int(annee),int(mois))

def read_dir(dir,template="*"):
    from os.path import join
    import glob
    divx = glob.glob(join(dir,template))
    return divx



class diaporama:
    """permet de créer des diaporama"""

    def __init__(self, dir,lang="FR"):
        import glob,os
        try:
            import Image    # Python Image Library is required - see 
        except:
            raise "Python Image Library is required - see  http://www.pythonware.com/products/pil/ "
        self.dir = dir
        (self.annee,self.mois)=current_date(self.dir)
        self.setLang(lang)
        imlist = glob.glob(os.path.join(self.dir,"images","photo*.jpg"))
        self.empty = len(imlist)==0 # tells that there is no diaporama to do
        self.texte="""\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="content-type" >
<meta content="NetForGod page " name="description" >
<title>%(flat_title)s</title>
<!-- This page uses SimpleViewer 
    Download SimpleViewer at www.airtightinteractive.com/simpleviewer -->
<script type="text/javascript" src="/js/swfobject.js"></script>
<STYLE TYPE="text/css">
a { text-decoration: none;}
.bd-droit {float: right; width: 148px; text-align: center;}
</STYLE>
<script type="text/javascript">
function diapo() {
               var fo = new SWFObject("/viewer.swf", "viewer", "100%%", "700", "7", "#181818");
               fo.addVariable("preloaderColor", "0xffffff");
               fo.addVariable("xmlDataPath", "gallery_%(lang)s.xml");
               fo.write("flashcontent");
               var x=document.getElementById("flashcontent").style.height=700;
               }
</script>
</head>
<body onload="diapo()" bgcolor="#000000" text="#FFFFCC"  link="#FF0033" style="font-size:12pt; font-family: verdana,sans-serif; color=#FFFFCC">
<div style="margin-left:auto; margin-right:auto; text-align:center;">
<div class="bd-droit">
%(link)s
</div>
<div style="width:1000px; margin-left:auto; margin-right:auto; text-align:center;">
<p> %(mois)s %(annee)d - <b>%(br_titre)s</b></p>
       <div id="flashcontent">
SimpleViewer requires Macromedia Flash. <a href="http://www.macromedia.com/go/getflashplayer/">Get Macromedia Flash.</a> If you have Flash
installed, <a href="diaporama_%(lang)s.html?detectflash=false">click to view gallery</a>.</div>
</div>
<p style="text-align:center"> FRATERNITÉ ŒCUMÉNIQUE INTERNATIONALE - - NET FOR GOD - - INTERNATIONAL ECUMENICAL FRATERNITY </p>
</div>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%%3E%%3C/script%%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-4576934-2");
pageTracker._initData();
pageTracker._trackPageview();
</script>
</body>
</html>
"""

    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (titre_fr,titre_en)=current_title(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.resume="Résumé du film"
            self.titre=titre_fr
            self.nomMois=langues.mois_nom[self.mois]
            self.link="""Français<a href="diaporama_EN.html"> / English</a>"""  # attention, non généralisable
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.resume="Movie synopsis"
            self.titre=titre_en
            self.nomMois=langues.month_name[self.mois]
            self.link="""English <a href="diaporama.html">/ Français</a>"""

    def images(self,maxsiz=(720,576),thumbsiz=(80,72)):
        """
        goes through all jpg files in self.dir/images/* 
        scale them to maxsiz
        creates thumbnails and save them in self.dir/thumbs/*
        """
        import glob,os,Image
        import os.path as op
        if not os.path.exists(os.path.join(self.dir,"thumbs")):
            os.mkdir(os.path.join(self.dir,"thumbs"))
        for ii in glob.glob(os.path.join(self.dir,"images","photo*.jpg")) :
            im=Image.open(ii)
            if 1.1*max(maxsiz)<max(im.size):    # needs to undersample
                print "je reduis %s  taille : %s"%(ii, str(im.size))
                HQ = op.join(op.dirname(ii),"HQ_"+op.basename(ii))    # images/photo*.jpg => images/HQ_photo*.jpg
                im.save(HQ)  # makes a backup
                im.resize(maxsiz,Image.ANTIALIAS)
                im.save(ii)
            ith=ii.replace("images/","thumbs/")
            if not os.path.exists(ith):     # makes thumbnail
                im.thumbnail(thumbsiz,Image.ANTIALIAS)
                im.save(ith)

    def do_xml(self):
        """
        takes photos in images/photoxx.jpg and captions in textes/photoxx_LL.jpg
        and create gallery_LL.xml where LL is the language code
        """
        import glob, os
        import os.path as op

        XML=file(op.join(self.dir,"gallery_"+self.lang+".xml"),"w")
        (titre_fr,titre_en)=current_title(self.dir)
        if self.lang=="EN":
            titre=titre_en
        else:
            titre=titre_fr
        XML.writelines( """\
    <?xml version="1.0" encoding="UTF-8"?>
    <simpleviewerGallery maxImageWidth="720" maxImageHeight="576" textColor="0xFFFFFF" frameColor="0xffffff" frameWidth="20" stagePadding="40" thumbnailColumns="3" thumbnailRows="4" navPosition="left" title="%s" enableRightClickOpen="false" backgroundImagePath="" imagePath="images/" thumbPath="thumbs/">
    """%" - ".join(titre))

        for ii in glob.glob(op.join(self.dir,"images","photo*.jpg")):
            i=ii
            XML.writelines("<image>\n")
            XML.writelines("   <filename>%s</filename>\n"%(op.basename(i)))
            text = self.legende(i)
            XML.writelines("  <caption>%s</caption>\n"%(text))
            XML.writelines("</image>\n")
        XML.writelines("</simpleviewerGallery>")
        XML.close()
    def legende(self,image):
        """search and return the legend for image in image dir and in current language
        search either in photoXX_LL.txt
        or in legendes_LL.txt"""
        import os.path as op
        f1 =  image.replace(".jpg","_"+self.lang+".txt")
        f2 =  op.join(op.dirname(image),"legendes_"+self.lang+".txt")
        try:
                f=file(f1)
                text=" ".join(f.readlines()).strip(" \n")
                f.close()
        except:
                text = ""
        if text == "":
                prefix = op.basename(image).replace(".jpg"," : ")   # photoxx : 
                try:
                    f=file(f2)
                    for l in f:
                      if l.startswith(prefix):
                         text = l.replace(prefix,"")
                         break
                    f.close()
                except:
                    text = ""
        if text == "":
                print "pas de légende en %s pour %s dans %s "%(self.lang,image,op.abspath(self.dir))
        return text

    def do_html(self,lang="FR"):
        """docstring for do_html"""
        import os
        formvar={}
        formvar["link"]=self.link
        formvar["mois"]=self.nomMois
        formvar["annee"]=self.annee
        formvar["lang"]=self.lang
        formvar["flat_title"]=" - ".join(self.titre)
        formvar["br_titre"]="<br>".join(self.titre)
        HTML=file(os.path.join(self.dir,self.diaponame),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()

class presentation:
    """permet de créer des page de presentation"""
    def __init__(self, dir,lang="FR"):
        import glob,os
        self.dir = dir
        (self.annee,self.mois)=current_date(self.dir)
        self.setLang(lang)
        self.texte="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>%(flat_title)s</title>
<link href="/nfg.css" type="text/css" media="screen" rel="stylesheet">
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico">
<script language="JavaScript">
<!--
function openWindow(url,name)
{ popupWin = window.open(url,name,'resizable, scrollbars, width=850,height=300')
}
// -->
</script>
</head>
<body>
<a href="/"><img id="logo" border="0" src="/images/logo_FOI.gif" alt="Logo" border="0" title="Réseau NetForGod"></a>
<img id="header" src="/images/bande-800-s.jpg" alt="header">
<div id="bandeau">
<div class="bd-gauche">
 <a id="ccn" href="http://www.chemin-neuf.org"><img src="/images/logo_k4.gif" height="35" border="0" alt="Logo Communaute du Chemin-neuf" title="Communauté du Chemin-Neuf"></a>
        %(slogan)s 
    </div>
    <div class="bd-droit">    %(link)s    </div>
</div>
<div id="page-centree" style="font-size: 16px">
<IMG alt="affiche" src="affiche.jpg" border="0" width="640" height="480">
%(resume)s
%(diapo)s
<hr width="30%%">
<a style="font-size: 16px" href="/frat.html">%(discover)s</A> <br>
<hr width="30%%">
"""+footer

    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (titre_fr,titre_en)=current_title(self.dir)
        (annee,mois)=current_date(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.resume="Résumé du film"
            self.titre=titre_fr
            self.nomMois=langues.mois_nom[self.mois]
            self.link="""Français<a href="presentation_EN.html"> / English</a>"""
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.resume="Movie synopsis"
            self.titre=titre_en
            self.nomMois=langues.month_name[self.mois]
            self.link="""English <a href="presentation.html">/ Français</a>"""
    
    def do_html(self,lang="FR"):
        """docstring for do_html"""
        import os.path as op
        formvar={}
        formvar["link"]=self.link
        formvar["mois"]=self.nomMois
        formvar["annee"]=self.annee
        formvar["slogan"]=self.slogan
        formvar["discover"]=self.discover
        formvar["lang"]=self.lang
        formvar["flat_title"]=" - ".join(self.titre)
        hr=0
        if op.exists(op.join(self.dir,self.resname)):
            formvar["resume"]="""<hr width="30%%"><a style="font-size: 16px" href="javascript:openWindow('%s','%s')">%s</A> <br>"""%(self.resname,self.resume,self.resume)
            hr=1
        else:
            formvar["resume"]=''
        if op.exists(op.join(self.dir,self.diaponame)):
            if hr==0:
                hr='<hr width="30%%">'
            else:
                hr=''
            formvar["diapo"]='%s<a style="font-size: 16px" href="%s">%s</A> <br>'%(hr,self.diaponame,"Diaporama")
        else:
            formvar["diapo"]=''
        HTML=file(os.path.join(self.dir,self.presname),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()


class resume:
    """permet de créer des pages de resume"""
    def __init__(self, dir,lang="FR"):
        import glob,os
        self.dir = dir
        imlist = glob.glob(os.path.join(self.dir,"textes","resume_*.txt"))
        self.empty = len(imlist)==0 # tells that there is no resume available
        self.setLang(lang)
        self.texte="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
	<meta http-equiv="Content-type" content="text/html; charset=utf-8">
	<link rel="stylesheet" href="/nfg.css" type="text/css" media="screen" title="no title" charset="utf-8">
</head>
<body>
<div id="page-centree">
<H1>%(resume)s</H1>
<p>%(resume_text)s</p>
</div>
<input type=button value="Fermer cette fenêtre" onClick="javascript:window.close();">
</body></html>
"""
    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (resume_fr,resume_en)=current_resume(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.resume="Résumé du film"
            self.resume_text=resume_fr
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.resume="Movie synopsis"
            self.resume_text=resume_en
    
    def do_html(self,lang="FR"):
        """docstring for do_html"""
        import os.path as op
        formvar={}
        formvar["resume"]=self.resume
        formvar["resume_text"]="<br>".join(self.resume_text)
        HTML=file(os.path.join(self.dir,self.resname),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()


class video:
    """
    permet de créer des pages video pour chaque film (celle qui présente le film en flash)
    Cette page minimise l'utilisation du javascript, et donne accès à l'achat de la video.
    """
    def __init__(self, dir,lang="FR"):
        import glob,os
        self.dir = dir
        imlist = glob.glob(os.path.join(self.dir,"textes","resume_*.txt"))
        self.empty = len(imlist)==0 # tells that there is no resume available
        (self.annee,self.mois)=current_date(self.dir)
        self.setLang(lang)
        self.texte="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>%(flat_title)s</title>
<link href="/nfg.css" type="text/css" media="screen" rel="stylesheet">
<link rel="shortcut icon" type="image/x-icon" href="/images/favicon.ico">
<script language="JavaScript">
<!--
function openWindow(url,name)
{ popupWin = window.open(url,name,'resizable, scrollbars, width=850,height=300')
}
// -->
</script>
</head>
<body>
<a href="/"><img id="logo" border="0" src="/images/logo_FOI.gif" alt="Logo" border="0" title="Réseau NetForGod"></a>
<img id="header" src="/images/bande-800-s.jpg" alt="header">
<div id="bandeau">
<div class="bd-gauche">
 <a id="ccn" href="http://www.chemin-neuf.org"><img src="/images/logo_k4.gif" height="35" border="0" alt="Logo Communaute du Chemin-neuf" title="Communauté du Chemin-Neuf"></a>
%(slogan)s 
</div>
<div class="bd-droit">    %(link)s    </div>
</div>
<div id="page-centree" style="font-size: 16px">
<object type="application/x-shockwave-flash" width="352" height="288" wmode="transparent" data="flvplayer.swf?file=%(file)s&showdigits=true">
<param name="movie" value="flvplayer.swf?file=%(file)s&showdigits=true" />
<param name="wmode" value="transparent"/>
</object>
%(resume)s
%(diapo)s
<hr width="30%%">
<a style="font-size: 16px" href="/frat.html">%(discover)s</A> <br>
<hr width="30%%">
<BR CLEAR=ALL>
<div id="pied">
<ul>
"""+footer
    def setLang(self,lang):
        """docstring for setLang"""
        self.lang=lang
        (titre_fr,titre_en)=current_title(self.dir)
        (annee,mois)=current_date(self.dir)
        if self.lang=="FR":
            self.slogan="Au service de l'UNITÉ des CHRÉTIENS et de la PAIX dans le MONDE."
            self.discover="Découvir la fraternité NetForGod"
            self.presname="presentation.html"
            self.diaponame="diaporama.html"
            self.resname="resume.html"
            self.videoname="video.html"
            self.resume="Résumé du film"
            self.titre=titre_fr
            self.nomMois=langues.mois_nom[self.mois]
            self.link="""Français<a href="presentation_EN.html"> / English</a>"""
        elif self.lang=="EN":
            self.slogan="Working for Christian unity and for peace in the world !"
            self.discover="Discover the NetForGod fraternity"
            self.presname="presentation_EN.html"
            self.diaponame="diaporama_EN.html"
            self.resname="resume_EN.html"
            self.videoname="video_EN.html"
            self.resume="Movie synopsis"
            self.titre=titre_en
            self.nomMois=langues.month_name[self.mois]
            self.link="""English <a href="presentation.html">/ Français</a>"""

    
    def do_html(self,lang="FR"):
        """docstring for do_html"""
        import os.path as op
        formvar={}
        formvar["link"]=self.link
        formvar["mois"]=self.nomMois
        formvar["annee"]=self.annee
        formvar["slogan"]=self.slogan
        formvar["discover"]=self.discover
        formvar["lang"]=self.lang
        formvar["flat_title"]=" - ".join(self.titre)
        formvar["file"]="test.flv"
        HTML=file(os.path.join(self.dir,self.videoname),"w")
        HTML.writelines(self.texte%formvar)
        HTML.close()

if __name__ == "main":
      print "cette bibliothèque doit être importée pour être utilisée"

