# utility to rate all python code
# obsolete - use QC.py rather
for i in *.py; do
  echo $i
  pylint -f text $i > TMPFILE
  grep  '^E[0..9]' TMPFILE
  grep  '^W[0..9]' TMPFILE
  grep  '^R[0..9]' TMPFILE
  echo "=============" $i "==========="
  grep  '^Your code has been rated'  TMPFILE
  echo "============================"
done
rm TMPFILE
