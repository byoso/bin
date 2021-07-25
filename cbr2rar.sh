#!/bin/bash

# ce petit script renomme simplement les extentions de fichier .rar et .zip en .cbr et .cbz et inversement.
echo "--------------------------------------------|"
echo `date +%H:%M:%S` "    *** cbr2rar ***     v1.0"
echo "--------------------------------------------|"
echo ""
echo "CONVERTISSEUR Archive / Bande Dessinée"
echo "Converter Archive / comics"
echo ""
echo "converti les .rar en .cbr et les .zip en .cbz ou l'inverse"
echo ""
echo "Dans le dossier :" `pwd`
echo ""
echo -e "Voullez-vous convertir TOUS les fichiers\na : Archrive vers BD\nb : BD vers Archive\nc : j'ai rien compris je sors"
read -p '' rep
echo ""
if [ $rep = "a" ]
then 
	find . -name "*.zip" -exec rename 's/\.zip$/\.cbz/i' {} \;
	find . -name "*.rar" -exec rename 's/\.rar$/\.cbr/i' {} \;
	echo "Archive --> BD OK";
	echo "";
	echo ls *.cbr;
	echo ls *.cbz
elif [ $rep = "b" ]
then
	find . -name "*.cbr" -exec rename 's/\.cbr$/\.rar/i' {} \;
	find . -name "*.cbz" -exec rename 's/\.cbz$/\.zip/i' {} \;
	echo "BD  --> Archive OK";
	echo "";
	echo ls *.rar;
	echo ls *.zip
else
	echo "OK, on touche à rien, au revoir."
fi

echo "--------------------------------------------"
echo "--------------------------------------------"


# for rename, you can use "-v" for verbose
