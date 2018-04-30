#!/bin/bash

mkdir ./icons

for i in 16x16 32x32 64x64 128x128 256x256 512x512 1024x1024; do
  (cd ./icons && curl -O "https://raw.githubusercontent.com/extr0py/oni/master/build/icons/$i.png")
done

tar -cvzf icons.tar.gz ./icons/*.png
