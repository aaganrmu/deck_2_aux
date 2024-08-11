#!/bin/sh

DEVICE="/media/elmarw/CIRCUITPY/"

echo "installing"
cd source
localfiles=$(ls)
for file in $localfiles; do
    echo "transfering $file"
    $(cp -r $file $DEVICE/)
done