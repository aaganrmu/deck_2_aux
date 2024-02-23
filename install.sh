#!/bin/sh

DEVICE="/media/elmarw/CIRCUITPY/"

echo "installing"
cd source
echo "transfering boot.py"
$(cp boot.py $DEVICE)
echo "transfering code.py"
$(cp code.py $DEVICE)
echo "creating folders"
$(mkdir -p $DEVICE/lib)
cd lib
localfiles=$(ls)
for file in $localfiles; do
    echo "transfering lib/$file"
    $(cp $file $DEVICE/lib/)
done
