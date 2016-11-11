#! /bin/bash

if [[ $# == 1 && -d $1 ]]
then
    stat=`stat -c "%a" $1`
    if [ "$stat" -lt 700 ]
    then chmod u+x+r $1
    fi
    ls $1
    chmod "$stat" $1
else echo Entrer le nom d\'un répertoire valide.
fi
