#!/bin/sh

# script to auto-create a novel for NaNoWriMo

tmp=/tmp/noveltmp
dest=$HOME/Desktop/novel.txt
touch $tmp
i=0
until [ $i -gt 49999 ]; do
alph=( a b c d e f g h i j k l m n o p q r s t u v w x y z)
RANGE=25
n1=$RANDOM
let "n1 %= $RANGE"
n2=$RANDOM
let "n2 %= $RANGE"
n3=$RANDOM
let "n3 %= $RANGE"
n4=$RANDOM
let "n4 %= $RANGE"
strng=${alph[$n1]}${alph[$n2]}${alph[$n3]}${alph[$n4]}
words=( `cat /usr/share/dict/words | grep $strng` )
if [ "$words" != "" ]; then
echo ${words} >> $tmp
fi
i=`cat $tmp |wc -l`
done

echo "the end." >> $tmp
tr '\n' ' ' < $tmp > $dest

exit 0
