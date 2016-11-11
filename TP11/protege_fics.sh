#! /bin/bash

protege(){
    for dir in $(ls)
    do
        if [ -d $dir ]
        then
            cd $dir
            protege $dir
            cd ..
        else
            chmod 444 $dir
        fi
    done
}

if [ $# == 1 ]
then
    cd $1
    protege 
else echo Entrer un nom de répertoire valide.
fi
