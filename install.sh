#!/bin/sh

DEVICE="/media/elmarw/CIRCUITPY/"

echo "installing"
cd source
localfiles=$(ls)
for file in $localfiles; do
    echo "transfering $file"
    $(cp -r $file $DEVICE/)
done

# echo "installing libs"
# $(mkdir -p $DEVICE/lib)
# cd lib
# localfiles=$(ls)
# for file in $localfiles; do
#     echo "transfering lib/$file"
#     $(cp -r $file $DEVICE/lib/)
# done
# cd ..