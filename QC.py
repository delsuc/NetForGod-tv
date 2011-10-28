# encoding: utf-8
"""
This programm run pylint on all python files managed by mercurial in a directory.


Created by Marc-André Delsuc on 2011-10-26.
Copyright (c) 2011 IGBMC. All rights reserved.
"""

from subprocess import Popen, PIPE

CMD = "pylint"
ARGS = []   # ["--rcfile=rcpylint"]

def msg(st, sep='='):
    print sep*(len(st)+4)
    print '|',st,'|'
    print sep*(len(st)+4)

def tracked_files(excluded=('none',)):
    """return list of hg tracked files in folder as a tuple : (all,modified) 
    excluded is a list of patterns (unix style) which are excluded
    """
    import fnmatch
    hgall = Popen(["hg", "stat", "-A"], stdout=PIPE).communicate()[0]
    lines = [l for l in hgall.split("\n")]
    hg = []
    modif = []
    for line in lines:
        sp = line.split()
        cont = False
        if len (sp) < 1:      # exit on conditions
            continue
        if sp[0] not in ('C', 'M'):
            continue
        fname = sp[1]
        for pat in excluded:
            if fnmatch.fnmatch(fname, pat): # find pattern
                print "excluding", fname
                cont = True
        if cont:
            continue
        hg.append(fname)
        if sp[0] in ('M'):
            modif.append(sp[1])
    return (hg, modif)
class WritableObject(object):
    "dummy output stream for pylint"
    def __init__(self):
        self.content = []
    def write(self, string):
        "dummy write"
        self.content.append(string)
    def read(self):
        "dummy read"
        return self.content
    
def run_pylint(fich):
    "run pylint on the given file and return synthetic results (note, error, reorder, warning)"
    import re
    from pylint import lint
    from pylint.reporters.text import TextReporter
#    pyl = lint.Run(args)
    pylint_output = WritableObject()
    lint.Run([fich]+ARGS, reporter=TextReporter(pylint_output), exit=False)
    ignored_error = ('Exter', 'E1103')  # 5 first char of ignored errors
    ignored_warn = ('none',)            # 5 first char of ignored warnings
    errors = 0
    warn = 0
    reorder = 0
    note = 0
    for l in pylint_output.read():
        if l.startswith('E0001'):
            errors = 10000  # indicates crash
            break
        elif l.startswith('E'):
            if l[0:5] not in ignored_error:
                errors += 1
        elif l.startswith('W'):
            if l[0:5] not in ignored_warn:
                warn += 1
        elif l.startswith('R') and l.split()[0] != 'Raw':
            reorder += 1
        elif l.startswith('Your code has been rated'):
            m = re.match('Your code has been rated at (-?\d+.\d.)/10', l)
            note = float(m.group(1))
    if errors == 10000:    # means crash
        note = -100
    return (note, errors, warn, reorder )

def process(files):
    "apply pylint to files"
    # msg("Checking files")
    stats = {}
    for f in files:
        if f.endswith('.py'):
            res = run_pylint(f)
            stats[f] = res
        else:
            print "excluding", f
    return stats
def report(stats, modif):
    "print a tabular report"
    title = "  Note/10   File                      Error Warning"
    nchar = len(title)
    print "\n", "-"*nchar
    print title
    print "-"*nchar
    top = 1
    mean = 0.0
    for k in reversed(sorted(stats.keys(), key = lambda x: stats[x][0])):
        note = stats[k][0]
        err = stats[k][1]
        warn = stats[k][2]
        if k in modif:
            head = 'M'
        else:
            head = ' '
        if err != 10000:    # means crash
            mean += note
        if top == 1:
            if note < 5.0:
                print "-"*nchar
                top = 0
        elif top == 0:
            if note < 0.01:
                print "*"*nchar
                top = -1
        if err == 10000:
            print "{} ******  {:25s} HAS SYNTAX ERRORS".format(head, k)
        elif err > 0:
            print "{} {:5.2f}  {:30s} {:3d}   {:3d} ".format(head, note, k, err, warn)
        else:
            print "{}{:6.2f}  {:30s}       {:3d}".format(head, note, k, warn)
    print "-"*nchar
    print "Mean note value is : {:5.2f}".format(mean/len(stats))
    print "-"*nchar

def message():
    "print pylint command"
    print "    to run pylint, type :"
    print CMD, 
    for a in ARGS[:-1]:
        print a,
    print "filename.py"
    print "    to check only errors, type :"
    print CMD, "-E",
    for a in ARGS[:-1]:
        print a,
    print "filename.py"
    
def main(folder='.', excluded=('.hgignore',)):
    "does the work id 'dir'  excluded is a list of excluded files"
    import os
    os.chdir(folder)
    #collect
    (hg, modif) = tracked_files(excluded=excluded)
    if modif:
        msg("Warning, the following files are modified but not commited", sep="*")
        for i in modif:
            print i
    stats = process(hg)
    report(stats, modif)
    message()
if __name__ == '__main__':
    main()

