# utility to launch the main Makefile program alone
. configuration.sh
make $1 -C  $VIDEOdir  MAKEdir=$MAKEdir -f $MAKEdir/Makefile all
