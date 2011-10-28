# to keep a set of compressed log files
# typically called regularly

NLOG=20

rm -f make.log.$NLOG.gz

for (( i = $(($NLOG)); i >1; i-- )); do
   mv make.log.$(($i-1)).gz make.log.$i.gz
done

gzip -c make.log > make.log.1.gz

rm make.log
