#!/usr/bin/python
# -*- coding: utf-8 -*-
# Ce script fait une stat des telechargements

import re
import datetime
import gzip
import glob
import os
import os.path as op
from bottle import view
import langues
import codec
from subprocess import Popen, PIPE
from collections import defaultdict
import itertools

try:
    base = os.environ['WEBROOT']
    baseurl = os.environ['WEBSITE']
except:
    raise Exception('do_stat.py cannot work - probably due to a lack of configuration, try doing    . configuration.sh    first')
directories = glob.glob(op.join(base,"videos/FOI_*"))
#base = "/home/netforgod/www/"
#directories = glob.glob(base + '/videos/FOI_*')

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

@view('tmpl/stat_mois.tpl')  # utilise le template de bottle
def stat_month_html(dic):
    return dic
@view('tmpl/stat_glob.tpl')  # utilise le template de bottle
def stat_glob_html(dic):
    return dic


def add_dic(a,b):
    "additione les valeurs de b dans a et retourne a"
    for (k,v) in b.items():
        a[k] = a.get(k, 0) + b[k]
    return a
def test():
    "tests add_dic"
    a={"aa":1, "bb":10}
    b={"aa":1, "cc":100}
    print add_dic(a,b)
def ip_name(ip):
    "return the host name of a given IP"
    output = Popen(["host", ip], stdout=PIPE).communicate()[0]
    try:
        name = output.split()[-1]
    except:
        name = ip
    if name.find('NXDOMAIN')>=0:    # means not found
        name = ip
    return name
def constant_factory(value):
    "used by defaultdict"
    return itertools.repeat(value).next
def stat():
    """build the stats month per month and global"""
    baseurl = os.environ['WEBSITE']
    TTotal = 0
    stat_tfilm = {}
    stat_film = {}
    stat_d = {}
    stat_ip = {}
    stat_lang = {}
    for dir in directories:
        (mon_tototal, mon_total, mon_d, mon_ip, mon_lang) = stat_month(dir)
        TTotal = TTotal + mon_total
        stat_tfilm[op.basename(dir)] = mon_tototal
        stat_film[op.basename(dir)] = mon_total
        stat_d = add_dic(stat_d,mon_d)
        stat_ip = add_dic(stat_ip,mon_ip)
        stat_lang = add_dic(stat_lang,mon_lang)
    ipnm = defaultdict(constant_factory('untested'))
    for ip in sorted(stat_ip.keys(), key = lambda s:stat_ip[s], reverse=True):
        if stat_ip[ip]<20: break     # truncate to 20, 
        ipnm[ip] = ip_name(ip)
    ll = langues.languages
    F = open( op.join(base,'stat_nfg.html'), 'w')
    html = stat_glob_html(locals())    # makes html from local variables and template
    F.write( html )                     # and write it
    F.close()

def stat_month(dir):
    """reads dl.log in dir, and creates a log file"""
    baseurl = os.environ['WEBSITE']
    file = op.join(dir,'dl.log')
#    print file
    basename = op.basename(dir)
    stat_t = {}  # one entry per language, list of IPs
    stat_d = {}  # one entry per day, list of IPs
    tot_d = {}       # one entry per day, just count
    tot_ip = {}      # one entry per IP, just count
    tot_lang = {}    # one entry per lang, just count
    pattern = re.compile('c=(.+)"')
    pdate = re.compile('(\d\d)\/(\w\w\w)\/(\d\d\d\d)')
    if op.exists(file):
        for l in open(file,'r'):
            if l.find("END ") > -1:
                field = l.split()
                ip = field[0]       # find IP
                dl_date = field[3][1:]  # find and parse date
                mdate = pdate.match(dl_date)
                (dl_day, dl_month, dl_year) = mdate.groups()
                i_month = month.index(dl_month)+1
                dmy = "%s-%02d-%s"%(dl_year, i_month, dl_day)
                m = pattern.search(field[9])    # find and parse film
                if m:
                    (date, video, lang) = codec.decodage(m.group(1))
                    if lang != field[6][:-1]:
                        #raise "Internal error !"
                        continue
                else:
                    lang = field[6][:-1]
                stat_t.setdefault(lang, []).append(ip)  # append IP to stat_t[lang]
                stat_d.setdefault(dmy, []).append(ip)
                tot_d[dmy] = tot_d.get(dmy, 0) +1
                tot_ip[ip] = tot_ip.get(ip, 0) +1
                tot_lang[lang] = tot_lang.get(lang, 0) +1
    Tototal = sum(tot_d.values())    # total total of all download
    Total = 0
    stat_n = {}
    for i in stat_t:
        n = len(set(stat_t[i]))     # removes multiple download with same ip and same language
        Total += n
        stat_n[i] = n
    F = open( op.join(dir,"stat.html"), 'wb' )
    ll = langues.languages
    html = stat_month_html(locals())    # makes html from local variables and template
    F.write( html )                     # and write it
    F.close()
    return (Tototal, Total, tot_d, tot_ip, tot_lang)    # returns totals for this film

if __name__ == '__main__':
#    os.system("cd ..; ./rsync.sh")
    stat()

