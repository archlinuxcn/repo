#!/bin/bash
nano PKGBUILD
updpkgsums
makepkg --printsrcinfo > .SRCINFO
makepkg
namcap *.pkg.*
paru -U *.pkg.*
rm -rf trilium-* pkg/ src/
git add .
git commit
git push
