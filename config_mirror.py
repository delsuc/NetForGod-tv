#!/usr/bin/env python
# encoding: utf-8
"""
config_mirror.py

this script is to be called after any modification of the configuration.sh file.
it creates configuration.php from configuration.sh 

Created by Marc-André on 2011-10-29.
Copyright (c) 2011 Communauté du Chemin-Neuf. All rights reserved.
"""
from __future__ import with_statement
import sys
import re
with open("www/prgm/configuration.php",'w') as F:
    F.write("<?php\n# This file was automaticaly created from configuration.sh using config_mirror.py - do not edit\n")
    with  open("configuration.sh") as config:
        for l in config:
            l = l[:-1]
            m = re.match('export (\w+)=[\"\']?([^\"\']*)[\"\']?',l)
            if m:
                var = m.group(1)
                val = m.group(2)
                try:
                    v = float(val)
                except:
                    val = "'{}'".format(val)    # if not numeral, put into single quotes
                F.write( "${0} = {1};\n".format(var,val))
            else:
                F.write(l+"\n")
    F.write("?>\n")
