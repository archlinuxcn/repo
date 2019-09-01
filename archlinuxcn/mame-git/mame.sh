#!/bin/sh
mame=/usr/lib/mame/mame

mame_first_run() {
  echo "Creating an ini file for MAME at $HOME/.mame/mame.ini"
  echo "Modify this file for permanent changes to your MAME"
  echo "options and paths before running MAME again."

  cd -- ~/.mame || exit

  if [ -e mame.ini ]; then
    mv mame.ini mameini.bak || exit
    echo "Your old ini file has been renamed to mameini.bak"
  fi

  # Note: the single quotes here are not a mistake; MAME will save these
  # strings verbatim into its configuration file, and expand the variables when
  # it is run in future.
  "$mame" \
    -artpath '$HOME/.mame/artwork;/usr/lib/mame/artwork' \
    -bgfx_path '$HOME/.mame/bgfx;/usr/lib/mame/bgfx' \
    -ctrlrpath '$HOME/.mame/ctrlr;/usr/lib/mame/ctrlr' \
    -hashpath '$HOME/.mame/hash;/usr/lib/mame/hash' \
    -languagepath '$HOME/.mame/language;/usr/lib/mame/language' \
    -pluginspath '/usr/lib/mame/plugins' \
    -inipath '$HOME/.mame/ini' \
    -rompath '$HOME/.mame/roms' \
    -samplepath '$HOME/.mame/samples' \
    -cfg_directory '$HOME/.mame/cfg' \
    -comment_directory '$HOME/.mame/comments' \
    -diff_directory '$HOME/.mame/diff' \
    -input_directory '$HOME/.mame/inp' \
    -nvram_directory '$HOME/.mame/nvram' \
    -snapshot_directory '$HOME/.mame/snap' \
    -state_directory '$HOME/.mame/sta' \
    -video opengl \
    -createconfig
}

if [ "$1" = "--newini" ]; then
  mame_first_run
  exit
elif ! [ -e ~/.mame ]; then
  echo "Running MAME for the first time..."

  mkdir -- ~/.mame
  (
    cd -- ~/.mame || exit
    mkdir artwork bgfx cfg comments ctrlr diff hash ini inp language nvram samples snap sta roms

    mame_first_run
  ) || exit
fi

exec "$mame" "$@"
