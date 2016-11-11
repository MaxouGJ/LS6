#! /bin/bash
c=0
for dir in $(ls)
do
    if [ -d $dir ]
    then
        echo "$dir"
        let "c+=1"
    fi
done
echo $c
