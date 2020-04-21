#!/bin/bash
export WINEPREFIX="$HOME/.cemu/wine"
export WINEDLLOVERRIDES="mscoree=;mshtml=;dbghelp.dll=n,b"

# Allows to play BotW with Polaris video cards
export R600_DEBUG="nohyperz"

if [ ! -d "$HOME"/.cemu ] ; then
  mkdir -p "$HOME"/.cemu/wine || exit 1
  ln -s /usr/share/cemu/Cemu.exe "$HOME"/.cemu/Cemu.exe || exit 1
  ln -s /usr/share/cemu/dbghelp.dll "$HOME"/.cemu/dbghelp.dll || exit 1
  ln -s /usr/share/cemu/keystone.dll "$HOME"/.cemu/keystone.dll || exit 1
  ln -s /usr/share/cemu/sharedFonts "$HOME"/.cemu/sharedFonts || exit 1
  cp -r /usr/share/cemu/gameProfiles "$HOME"/.cemu/ || exit 1
  cp -r /usr/share/cemu/mlc01 "$HOME"/.cemu/ || exit 1
  cp -r /usr/share/cemu/shaderCache "$HOME"/.cemu/ || exit 1
fi

if [ ! -L "$HOME"/.cemu/sharedFonts ] && [ ! -d "$HOME"/.cemu/sharedFonts ] ; then
  ln -s /usr/share/cemu/sharedFonts "$HOME"/.cemu/sharedFonts || exit 1
fi
if [ -L "$HOME"/.cemu/gameProfiles ] ; then
  rm "$HOME"/.cemu/gameProfiles
  cp -r /usr/share/cemu/gameProfiles "$HOME"/.cemu/ || exit 1
fi

if [ ! -f "$HOME"/.cemu/wine/drive_c/windows/syswow64/vcruntime140.dll ]; then
  if [ -n "`whereis zenity|grep bin`" ]; then
    zenity --info  --title 'Cemu' --text 'Installing wine dependencies.\n\nThe process may take a few minutes'
  fi
  winetricks -q vcrun2017
  winetricks settings win7
fi
cd ~/.cemu
wine Cemu.exe "$@"
