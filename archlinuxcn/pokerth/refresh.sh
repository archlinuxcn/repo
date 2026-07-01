#!/usr/bin/bash

# Commands to make a new release
# Edit PKGBUILD to bump release

echo -ne "\tHave you bumped pkgrel in PKGBUILD? (Y/N) "
read YN
if [ "$YN" == "Y" ]
then
  makepkg --printsrcinfo > .SRCINFO
  git add PKGBUILD .SRCINFO
  if [ -n "$1" ]
  then
    echo -ne "\t\tcommitting..."
    git commit -m "$1"
    git push
    echo " done!"
  else
    echo -e "\tNo commit message provided"
  fi
else
  echo -e "\tDon't forget to add a commit message to this script!"
fi