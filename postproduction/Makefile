# Ce fichier contient toutes les commandes pour réaliser le pipeline de production video
#
# faire
# make help
# pour avoir les informations utilisateur
# 
# documentation technique
# utilise et nécessite gnu make (doc complete  : http://www.gnu.org/software/make/manual/html_node/index.html )
#
# make est utilisé à la racine du projet pour tout tester
# make est ensuite appelé dans les sous-directory FOI* de manière récursive pour faire les fichiers

#######################################
# partie adaptable à la configuration

# address of the directory, which contains this Makefile and other scripts
MAKEdir = /home/netforgod/netforgod-tv/postproduction

# compte sur le serveur - doit être configuré en ssh
# SSH-USER = user@nom.de.la.machine
SSH-USER = netforgod@chemin.bayard-service.com

# directories sur le serveur
# VIDEO-DIR : là où vont les videos
VIDEO-DIR = /home/netforgod/www/videos
# BCK-DIR là où les fichiers côté post-prod sont stockés
BCK-DIR = /home/netforgod/post_prod_log

# commandes pour les codeurs
FFMPEG = nice ~/bin/ffmpeg -benchmark 
TOXVID = ~/bin/toxvid # pour les SD DivX compatible en 576p
TOHD = ~/bin/toHD     # pour les HD en 720p
WAV2AC3 = -ar 48000 -ab 224k 
AC32MP3 = -acodec mp3 -ar 44100 -ab 128k 
MUX2AVI = $(FFMPEG)

# nom des projets

# noms des dossiers
wavDIR = sons
ac3DIR = sons
mp3DIR = sons
divxDIR = .
textDIR = textes

# fin de la configuration
#######################################
# V4 était sur saul4 - crashé - V5 est la nouvelle version
VERSION = V5
DATE = 26-Jan-2015
AUTHOR = Marc-André
#######################################
# ramassage des fichiers
#######################################

# FOI*   this dir is used by the top most make
#foiDIR= $(wildcard FOI*)
foiDIR= $(wildcard */)
# FOI*/*.mp4
VIDMP4= $(wildcard $(addsuffix *.mp4,$(foiDIR)))
# FOI*/*.mpg
VIDMPG= $(wildcard $(addsuffix *.mpg,$(foiDIR)))
# FOI*/*.avi
VIDAVI= $(patsubst %.mpg,%.avi,$(VIDMPG)) $(patsubst %.mp4,%.avi,$(VIDMP4))
# FOI*/*_divx.avi
DIVX= $(patsubst %.avi,%_divx.avi,$(VIDAVI))
# FOI*/sons/*.wav
SONSWAV= $(wildcard $(addsuffix sons/*.wav,$(foiDIR)))
# FOI*/sons/*.ac3 to do
SONSAC3TODO=$(patsubst %.wav,%.ac3,$(SONSWAV))
# FOI*/sons/*.ac3 done
SONSAC3DONE= $(wildcard $(addsuffix sons/*.ac3,$(foiDIR)))
# FOI*/sons/*.ac3 all of them
SONSAC3= $(sort $(SONSAC3DONE) $(SONSAC3TODO))
# FOI*/sons/*.mp3 to do
SONSMP3= $(patsubst %.ac3,%.mp3,$(SONSAC3))

# sons/*.mp3   utilisé par localdivx
localMP3 = $(wildcard sons/*.mp3)
localDIVX = $(subst sons/,, $(patsubst %.mp3,%_divx.avi,$(localMP3)))

#vpath %.wav sons
vpath %.mp3 sons
#vpath %.ac3 sons

#
SHELL = /bin/bash
#variables calculées
#Ce sont des definitions, les appel sont faits au moment de l'usage (variable "recursively expanded")
#parse du fichier de parametre
ASPECT =  $(shell ~/bin/xml_parse.py $(dir $@)/parametres.xml aspect 4:3)
#determine le nbre de processor en comptant dans /proc/cpuinfo
NCPU = $(shell awk  "/processor/ {i++} END {print i}" /proc/cpuinfo )

#######################################
# liste des actions, l'action par défaut est la première - ic la doc -
#######################################

.PHONY: default
default: hello 
	@echo "================ programme Export-Make ======================================"
	@echo " Ce programme prend en charge les fichiers deposes dans le dossier export"
	@echo " le principe est que les fichiers video (.mp) et sons (.wav ou .ac3) sont déposé dans un dossier"
	@echo " le nom du dossier DOIT être : FOI_YY_MM ou YY est l'année, et MM est le mois"
	@echo " et ensuite tout est pris en charge"
	@echo ""
	@echo "il n'y a rien d'autre à faire, mais quelques commandes sont disponibles:"
	@echo ""
	@echo "make all       - appelé automatiquement toute les 2 heures"
	@echo "    fabrique les divx les ac3 et mp3 manquant et les transfert sur le serveur "
	@echo "    si on est pressé..."
	@echo ""
	@echo "make help"
	@echo "    une documentation plus détaillée"

.PHONY: help
help: hello
	@echo "================ Documentation pour le prgm Export-Make ======================"
	@echo " Ce programme prend en charge les fichiers deposes dans le dossier export"
	@echo ""
	@echo "Liste des commandes utilisables avec ce programme :"
	@echo ""
	@echo "make all       - appelé automatiquement toute les 2 heures"
	@echo "    fabrique les divx les ac3 et mp3 manquant et les transfert sur le serveur "
	@echo ""
	@echo "-----------------------------------------------------------------------"
	@echo " on peut aussi faire manuellement les sous-commandes suivantes: (toutes faites automatiquement par 'make all')"
	@echo ""
	@echo "make divx"
	@echo "   crée les fichiers XX_divx.avi complets avec le son l'image dans chaque langue."
	@echo "   XX : code de la langue"
	@echo ""
	@echo "make image"
	@echo "   crée le fichier .avi codé pour l'image (sans son) à partir du fichier codé en MP2 .mpg"
	@echo ""
	@echo "make ac3"
	@echo "   crée les fichiers .ac3 à partir des fichiers .wav présents dans le dossier $(wavDIR)."
	@echo "   les met dans le dossier $(ac3DIR)"
	@echo ""
	@echo "make transfert"
	@echo "    copie tous les nouveaux fichiers sur le serveur internet  - utilise la commande rsync"
	@echo ""
	@echo "Remarque 1 : toutes les créations sont 'incrémentales'."
	@echo "   C'est à dire que seuls les nouveaux fichiers sont pris en compte, les fichiers déjà là ne sont pas recalculé"
	@echo "   de mÃªme, seuls les fichiers nouvellement créés sont copiés sur le serveur."
	@echo "   ainsi on peut rajouter un fichier wav (ou ac3) et faire make divx pour faire un nouveau divx"
	@echo ""
	@echo "Remarque 2 : 'make all' est fait automatiquement toutes les heures paires (à 2h00 - 4h00 - 6h00 etc...)"
	@echo ""
	@echo "Remarque 3 : si l'on veut s'assurer de ce qui serait fait, sans le faire réellement, il faut rajouter -n"
	@echo "   par exemple :"
	@echo "make -n all     fera la liste de tout ce qui est à faire."
	@echo "make -n divx    fera la liste des divx à faire"
	@echo "======================================================================="

# pour le  deboguage, il y  a aussi make check

###################################################
# PHONY targets
# c'est ici que l'on défini les dépendances

#  pour tout faire
.PHONY: all
all: hello clean-ln image ac3 mp3
# transfert

# dit bonjour poliment
.PHONY: hello
hello: 
	@echo -----------------------------------------------------
	@echo Export-Make par $(AUTHOR), version $(VERSION) du $(DATE)
	@echo -----------------------------------------------------

# enleve tout les liens casses
.PHONY: clean-ln
clean-ln:
	-find -L . -lname "*" -print -delete

# compresse le .mpg en.avi - sans les sons
.PHONY: image
image: $(VIDAVI)

# compresse tout les ac3 en mp3
.PHONY: mp3
mp3: $(SONSMP3)

# compresse tout les wav en ac3
.PHONY: ac3
ac3: $(SONSAC3)


#  pour transferer tous les fichiers sur le serveur
#  #  inclus tous les sous-dossier,:
#     le video.avi (divx sans le son) affiche.jpg (l'affiche de la video)
#     #     et les .mp3 et .txt, dans les fichiers sons et textes
#     exclus tout les reste
#     #  le fichier syncing signale qu'un transfert est deja en route
# pour que rsync fonctionne, il faut avoir fait un certificat ssh-keygen et opsé la clép publique sur SSH-USER
.PHONY: transfert
transfert: 
	rsync  -a --copy-links \
	--include '*/' --include 'video.avi' --include '*.jpg' --include '*.mp3' --include '*.txt' --include 'public' --include '*.xml' --exclude '*' \
	. $(SSH-USER):$(VIDEO-DIR)
	rsync -a auto.sh Makefile make.log $(SSH-USER):$(BCK-DIR)

# pour créer localement les divx (pas apellé par 'all')
.PHONY: divx
divx: image mp3
	@for dir in $(foiDIR); \
	do \
		(cd $$dir; $(MAKE) --no-print-directory -f $(MAKEdir)/Makefile localdivx); \
	done

# dans chaque directory, fabrique les divx de chaque langues (pas apellé par 'all', seulement par divx)
.PHONY: localdivx
localdivx: $(localDIVX)


###################################################
# transform rules
# c'est ici que tout le travail est fait
# $* est ce qui est "matché" par %, $(*D) est seulement le directory
%.ac3: %.wav
	echo $@
	-$(FFMPEG) -i $*.wav $(WAV2AC3)  -y $*.ac3

%.mp3: %.ac3
	-$(FFMPEG) -i $*.ac3 $(AC32MP3)  -y $*.mp3

# .HD est une pseud extension, pour un fichier qui est en fait un *.mp4
%.HD %.avi: %.mp4
	@echo conversion de $<
	$(TOXVID) -a $(ASPECT) $< $*.avi
	$(TOHD) -a $(ASPECT) $< $*.HD
	cd $(dir $@); ln -s  $(notdir $*.HD)  video.HD; ln -s  $(notdir $*.avi)  video.avi


%_divx.avi: %.mp3
	-$(MUX2AVI) -i sons/$*.mp3 -i video.avi -acodec copy -vcodec copy -y $*_divx.avi
# regles pour passer en minuscule les fichiers d'entrée
%.wav: %.WAV
	mv $*.WAV $*.wav
%.ac3: %.AC3
	mv %.AC3 %.ac3
%.mpg: %.MPG
	mv %.MPG %.mpg
%.mp4: %.MP4
	mv %.MP4 %.mp4

# regle pour le debogage
check:
	@echo foiDIR $(foiDIR) 
	@echo VIDMPG $(VIDMPG)
	@echo VIDAVI $(VIDAVI)
	@echo DIVX $(DIVX)
	@echo SONSWAV $(SONSWAV)
	@echo SONSAC3TODO $(SONSAC3TODO)
	@echo SONSAC3DONE $(SONSAC3DONE)
	@echo SONSAC3 $(SONSAC3)
	@echo SONSMP3 $(SONSMP3)
        @echo NCPU $(NCPU)
	@for dir in $(foiDIR); \
	do \
		(cd $$dir; $(MAKE) -n -w -f $(MAKEdir)/Makefile lcheck); \
	done
lcheck:
	@echo localDIVX $(localDIVX)
	@echo localMP3 $(localMP3)


