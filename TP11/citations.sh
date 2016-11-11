#! /bin/bash

#mkdir Citations
#cd Citations
#echo Répertoire de citations > readme

#echo Bonjour $USER
#echo répertoire Citation a été créé dans le répertoire $PWD

parcours(){
    for dir in $(ls)
    do
        if [ -d $dir ]
        then
            cd $dir
            parcours $1 $dir
            cd ..
        else
            txt=`grep -E [A-z]* $1 [A-z]*\. $dir`
            echo $txt >> ~/Documents/LS6/TP11/Citations/cite_$1.txt
        fi
    done
}

cite(){
    if [ ! -e Citations ]
    then mkdir Citations
    fi
    touch Citations/cite_$1.txt
    cd $2
    parcours $1 $2
}

if [ $# == 2 ]
then cite $1 $2
else echo Veuillez entrer un mot et une référence de répertoire
fi
