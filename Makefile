#######################################
# Utilisation
# Ce makefile decrit comment fabriquer les fichiers divx, flv et html
# 
# il doit être appelé avec la variable $(MAKEdir) qui contient le nom du dossier qui contient ce fichier (et les autres prgm)
# voir la doc plus bas (make help)
#
#######################################

#######################################
# partie adaptable à la configuration

# address of the prgm directory, which contains this Makefile and all the scripts
#MAKEdir = /home/netforgod/FOI_prgm

# three directories
# VIDEO : contains genuine content
# DIVX : fake directories linked to the real ones
# VOD : contains flv and other VOD material
# address of the VOD directory
#VIDEOdir = /home/netforgod/www/videos

# address of the VOD directory
#VODdir = /home/netforgod/www/VOD

# address of the DIVX directory
#DIVXdir = /home/netforgod/www/FOI

# commandes pour les codeurs

# addresse de FFMPEG
FFMPEG =  nice /home/netforgod/USR/bin/ffmpeg 
#-benchmark
#FFMPEG = echo

# la notice de copyright (apparait dans les meta informations)
COPYRIGHT = NetForGod
# le titre de la video (apparait dans les meta informations)
TITLE = video NFG
# la date
DATE = $(shell date +"%Y")

# commande pour fabriquer les divx .avi (il n'y a pas de compression simplement le muxage du son et de l'image)
#syntax depends on ffmpeg version
MUX2AVI = $(FFMPEG) -metadata title="$(TITLE)" -metadata copyright="$(COPYRIGHT) $(DATE)"
#MUX2AVI = $(FFMPEG) -title="$(TITLE)" -copyright "$(COPYRIGHT) $(DATE)"

# commande pour fabriquer les FLV
# mettre un réglage qui permet un débit son + image de l'ordre de 300-400 kbps
# le flux audio
AUDIOFLAG = -acodec libmp3lame -ab 32k -ar 22050

# le flux video standard VIDEOFLAG-43 est pour les 4:3 / VIDEOFLAG-169 est pour les 16:9
VIDEOFLAG-43 = -qscale 8 -s 320x240 -aspect 4:3 -b 256k -r 15
VIDEOFLAG-169 = -qscale 8 -s 370x210 -aspect 16:9 -b 256k -r 15

# le flux video amélioré - 500-700 kbps / PAS UTILISE
VIDEOFLAG2 = -qscale 8 -s 448x336 -aspect 4:3 

# les options de fichier
#syntax depends on ffmpeg version
FILEFLAG = -metadata copyright="$(COPYRIGHT) $(DATE)" -metadata title="$(TITLE)" -f flv -y
#FILEFLAG = -copyright "$(COPYRIGHT) $(DATE)" -title "$(TITLE)" -f flv -y

# this tells make that mp3 files should reside in a sons/ sub-dir
vpath %.mp3 sons

# this tells make that txt files should reside in a textes/ sub-dir
vpath %.txt textes

# fin de la configuration
#######################################

#######################################
# ramassage des fichiers
#######################################

# foiDIR : contains all the directory to be processed
foiDIR= $(wildcard */)

# FLVs contains all the */*.flv files to be built
FLVs = $(foreach dir,$(foiDIR),$(wildcard $(dir)*.flv))

# les var localXXX sont utilisée quand on rerentre dans MAKE dans les dir des videos.
# localMP3 : liste de tous les fichiers sons/*.mp3   utilisé pour construire les divx
localMP3 = $(wildcard sons/*.mp3)

# localDIVX built from localMP3
localDIVX = $(subst sons/,, $(patsubst %.mp3,%_divx.avi,$(localMP3)))

# localFLV built from localDIVX
localFLV = $(subst .avi,.flv,$(localDIVX))

# localAffiche is either empty is is the affiche.jpg file
localAffiche = $(wildcard affiche.jpg)

# localTi is the titles of the current video
localTi = $(wildcard textes/titre*.txt)

# localRes is the Abstracts of the current video
localRes = $(wildcard textes/resume*.txt)

# localIm is the list of images for diaporama
localIm = $(wildcard images/photo*.jpg) $(wildcard images/photo*.txt)

# parametres codés dans le fichier parametres.xml, et lu par le prgm xml_parse.py
#       python xml_parse.py parametres.xml cle val_par_defaut
# START   durée du générique à enlever pour les flv
START = $(shell $(MAKEdir)/xml_parse.py $(dir $@)parametres.xml start_at 0)

# ASPECT  4:3 ou 16:9
ASPECT = $(shell $(MAKEdir)/xml_parse.py $(dir $@)parametres.xml aspect 4:3)

#######################################
# liste des actions, l'action par défaut est la première - ici la doc -
#######################################

.PHONY: help
help:
	@echo "================ Documentation pour le prgm make ======================"
	@echo " Ce programme construit les différentes pages pour le site video "
	@echo ""
	@echo "à cause de la structure complexe, le make doit est appellé avec le directory en argument :"
	@echo "l'appel standard est :"
	@echo "make -C  $(VODdir)  MAKEdir=$$PWD -f $$PWD/Makefile action"
	@echo
	@echo "les actions standards suivantes existent:"
	@echo "make help : cette doc"
	@echo "make check : pour verifier"
	@echo "make all : pour tout faire"
        # $$PWD est pour que ca s'affiche correctement dans le shell

###################################################
# PHONY targets
# c'est ici que l'on défini les dépendances

#  pour tout faire
# .PHONY: all
# all:
	# $(MAKE) -C $(VIDEOdir) -f $(MAKEdir)/Makefile _all

.PHONY: all
all: link index 

# pour créer localement les pages .html ( appelé par 'all')
# crée les *.avi en dépendance
# les *.flv sont créés ensuite
.PHONY: index
index: 
	@for dir in $(foiDIR); \
	do \
		($(MAKE) -f $(MAKEdir)/Makefile -C $$dir lpages); \
		($(MAKE) -f $(MAKEdir)/Makefile -C $$dir lFLV); \
	done


# updates all the relations between the distrib directory : VODdir  and repository : CURDIR (list is in foiDIR)
.PHONY: link
link:
	@for dir in $(foiDIR); \
	do \
		mkdir -p $(VODdir)/$$dir; \
		ln -f -s $(CURDIR)/$$dir/affiche.jpg $(VODdir)/$$dir; \
	done
#ln -f -s $(CURDIR)/$$dir $(DIVXdir); \


###################################################
# transform rules
# c'est ici que tout le travail est fait
# $* est ce qui est "matché" par %, sans l'extension

# pour produire les divx en muxant video.avi et le son XX.mp3
%_divx.avi: %.mp3 video.avi
	$(MUX2AVI) -i sons/$*.mp3 -i video.avi -acodec copy -vcodec copy -y $@

# cette regle produit les .flv a partir des .avi
# 2 codages : standard : VIDEOFLAG : *.flv
#           : HQ : VIDEOFLAG2 *_700.flv   - pas utilisé pour l'instant -
%.flv: %.avi parametres.xml
	@if [ $(ASPECT) == "4:3" ]; then \
	  $(FFMPEG) -i $< -ss $(START) $(VIDEOFLAG-43)  $(AUDIOFLAG) $(FILEFLAG) $@; \
	fi
	@if [ $(ASPECT) == "16:9" ]; then \
	  $(FFMPEG) -i $< -ss $(START) $(VIDEOFLAG-169)  $(AUDIOFLAG) $(FILEFLAG) $@; \
	fi

#%divx_700.flv: %divx.flv
#	$(FFMPEG) -i $*divx.avi \
#	   -ss 	`python $(MAKEdir)/xml_parse.py $(dir $@)parametres.xml start_at 0` \
#	    $(VIDEOFLAG2)  $(AUDIOFLAG) $(FILEFLAG) $*divx_700.flv

# lpages : toutes les pages html locales
.PHONY: lpages
lpages:  index.html diaporama.html resume.html presentation.html

# construit la page html pour le download
index.html:  $(localDIVX) $(localAffiche) $(localTi)  parametres.xml .htaccess
	python $(MAKEdir)/do_tele.py .

# construit le diaporama
diaporama.html : $(localIm) $(localTi)
	python $(MAKEdir)/diaporama.py .

# construit la page de présentation de la video
presentation.html: $(localTi) resume.html diaporama.html
	python $(MAKEdir)/presentation.py .

# construit la page de resume
resume.html : $(localTi) $(localRes) 
	python $(MAKEdir)/resume.py .

# s'assure que la page a la protection par defaut
.htaccess :
	cp $(MAKEdir)/htaccess_def .htaccess
#et les bons parametres
parametres.xml :
	cp $(MAKEdir)/parametres.xml parametres.xml

# force le calcul des FLV locaux, permet de séparer cette regle de la précédente, et de produire la page de téléchargement avant de calculer le flv
# sinon, il suffirait de dire que index.html dépend de $(localFLV)
# voir index:
.PHONY: lFLV
lFLV: $(localFLV) parametres.xml

###################################################
# regles pour le debogage
# make check, permet de visualiser le contenu de toute les variables
.PHONY: check
check:
	$(MAKE) -C $(VIDEOdir) -f $(MAKEdir)/Makefile _check

.PHONY: _check
_check:
	@echo ======================================================================
	@echo Liste des Dossiers a explorer :
	@echo foiDIR : $(foiDIR) 
	@echo ======================================================================
	@echo FLVs : $(FLVs) 
	@echo ======================================================================
	@for dir in $(foiDIR); \
	do \
		$(MAKE) -w -f $(MAKEdir)/Makefile -C $$dir lcheck ; \
	done

#lckeck est appelé par check
lcheck:
	@echo Fichiers sons : \(localMP3\) $(localMP3)
	@echo
	@echo Divx requis \(localDIVX\) : $(localDIVX)
	@echo
	@echo FLV Requis \(localFLV\) : $(localFLV)
	@echo
	@echo images : \(localIl\) : $(localAffiche) $(localIm)
	@echo
	@echo textes \(localTi\) \(localRes\) : $(localTi) $(localRes)

