#!/bin/sh
# utility to launch the main Makefile program alone
. configuration.sh
# $* is to get additional args from caller
if [ $DEBUG_MODE ]; then
    make $* -C  $VIDEOdir  MAKEdir=$MAKEdir -f $MAKEdir/Makefile all
else
    make $* -C  $VIDEOdir  MAKEdir=$MAKEdir -f $MAKEdir/Makefile all
fi
