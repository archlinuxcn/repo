#!/bin/sh

# Prompts for confirmation, returns 1 if Yes
#
# Usage: getConfirmation "Question message"
# You can get anwser value on retcode
# if [[ $? == "1"]]; then
#   echo "You choose yes"
# fi
function getConfirmation {
  value=0
  while true; do
    read -p "${1} [Y/n]" yn

    case $yn in
      [Yy]* ) return 0 ;;
      [Nn]* ) return 1 ;;
      * ) return 0 ;;
    esac

  done
}

echo "This script will cleanup all workfiles"
getConfirmation "Do you want to proccess"
if [[ $1 == "0" ]]; then
  echo "Aborting"
  exit 1
fi

rm -r src/
rm -r pkg/
rm v*.zip
rm v*.zip.part
rm *tar.gz
rm *tar.xz

exit 0
