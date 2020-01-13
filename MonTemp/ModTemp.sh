#!/bin/bash


#This script runs program LecturaModuloTemp.py

if [ -e $1 ] #$1 is the configuration file
then
    filename=$(grep Port: $1)
    filename=${filename#Port:}
    if test -e $filename #Ask if filename directory exist
    then
        Per=$(stat -c "%a" $filename)
        PythonFile=$(readlink -f ~/.myPrograms/TempModule)
        PythonFile=${PythonFile%ModTemp.sh}
        PythonFile=$PythonFile"LecturaModuloTemp.py"
        if [ $Per -ne '777' ] #Ask for the permissions of filename
        then
            sudo chmod 777 $filename #Change permissions of filename
            Status=$?
            if [ $Status -eq 0 ]
            then
                
                #echo $PythonFile
                $CONDA_PYTHON_EXE $PythonFile $1 #Executes LecturaModuloTemp.py
                #python3.7 $PythonFile $1
            else
                echo 'You do not have the permissions required to habilitate ' $1
            fi
        else
             $CONDA_PYTHON_EXE $PythonFile $1
             #python3.7 $PythonFile $1
        fi
    else 
        echo $filename 'does not exist. Please, check the connection of module Lakeshore.'

    fi
else
    echo $1 'does not exist. Please, check the configuration file.'
fi

