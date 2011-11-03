#!/usr/bin/env python
# encoding: utf-8
"""
codec.py

duplicate the codec.php code

Created by Marc-André on 2011-02-13.
Copyright (c) 2011 IGBMC. All rights reserved.
"""

import langues
import radix
import time, math
import binascii

prim1 = 9007; # 8191;   # pour separer video; > 5000; premier c'est mieux, 
prim2 = 97; # pour separer ilang
prim3 = 17;
crclen = 5; # nbre de digit gardés pour le crc
ordrelangues = langues.ordrelangues + " MUL"
debug = 0;     # mettre à 0 pour production 

#date_default_timezone_set("Europe/Paris")

def codage(date_sec, video, lang):
    """
    # return une chaine qui "crypte" (très faiblement) les champs
    # i) date_sec est transformée en jours depuis le 1 1 2009
    # ii) lang est transformée dans l'index dans la table globale
    # iii) date lang et video sont mélangés avec des nmbre premiers prim1 et prim2
    # iv) le nombre est codé en base 35
    # v) les derniers chiffres du crc codé en base 33 sont rajoutés à la fin
    """
    count = 0
    ilang = ordrelangues.split(' ').index(lang)+1     #trouve index de langue
    date = int(math.floor(int(date_sec)/3600)) - 39*24*365       # change la date en heures depuis le ~ 1 1 2009
    descrip = (date*prim1 + video)*prim2 + ilang            # je préfère que la langue soit facile à piratée
    crc = binascii.crc32(str(descrip))
    crcst = radix.str(crc, 35)       # rajoute un crc
    descrip = descrip * prim3       # puis multiplie par prim3
    crcst = crcst[-crclen:]     # garde les 5
    value = radix.str(descrip,33)     # en base 33
    if (debug == 1):
        print "ilang :", ilang
        print "video :", video
        print "date :", date
        print "descrip :", descrip
        print "crc : ", crc
        print "value : ",value
        print "return : ",value+crcst
    return value+crcst
        
def decodage(val1):
    """ inverse codage"""
    crc = val1[-crclen:]
    v = val1[0:-crclen]
    val = int(v,33);  # en base 33
    val = (val / prim3)
    check = binascii.crc32(str(val))
    check = radix.str(check, 35)
    #trouve index de langue
    #    $descrip = ($date*$prim1 + $video)*$prim2 + $ilang;   
    dd = (val/prim2)
    il = int(val - dd*prim2)
    lang = ordrelangues.split(' ')[il-1]
    video = (dd % prim1)
    date = (dd / prim1) + 39*24*365
    if (debug == 1):
        print "crc : ", crc, check
        print "value : ", val
        print "video : ", video
        print "lang : ", il, lang
        print "date : ", date
    if crc !=  check[-crclen:]:
        print "caramba"
        date=0
        video=0
        lang=0
    return (date, video, lang)

def test_code(jours,  video, lang):
    date = time.time() + 3600*24* jours   #date de validite  time() donne le nbre de secondes depuis le 1 1 1970, à aujourd'hui
#    date = 1300224603
    print  "date :", jours, date
    print "video : ", video
    print "lang : ",lang
    print "========codage"
    code = codage(date,  video, lang)
    print code
    print "========decodage"
    t = decodage(code)
    if (debug == 1 ):
        d = t[0]
        v = t[1]
        l = t[2]
        print "decoded film : FOI_%s_%04d"%(l,v);
        print "decoded validite : %06d  : "%(d*3600)
        print time.ctime(d*3600);
if __name__ == '__main__':
    debug = 1
    jours = 30
    video = 712    #date du film  YY-MM  ==>  max = 2000 si 2020
    lang = "MUL"
    test_code(jours,  video, lang)

