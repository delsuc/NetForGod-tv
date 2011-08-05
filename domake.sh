#!/bin/sh
# utility to launch the main Makefile program alone
. configuration.sh
# $* is to get additional args from caller
make $* -C  $VIDEOdir  MAKEdir=$MAKEdir -f $MAKEdir/Makefile all
