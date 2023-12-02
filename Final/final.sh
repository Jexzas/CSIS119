#!/bin/bash
# This will only work on Windows machines

echo "This program, if executed, will delete all image files (webp, tiff, png, jpg, jpeg), recursing into all directories within. This script has to be placed within the directory you wish it to run within. Is that what you want? (y/n)"
read answer
echo $answer
if [ "$answer" = "y" ] || [ "$answer" = "Y" ];
then
    find . -type f -name '*.jpg' -delete
    find . -type f -name '*.jpeg' -delete
    find . -type f -name '*.tiff' -delete
    find . -type f -name '*.webp' -delete
    find . -type f -name '*.png' -delete
else
    exit
fi

