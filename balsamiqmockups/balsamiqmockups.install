#!/bin/sh

desktop_update() {
  if [ -x usr/bin/update-mime-database ]; then
    update-mime-database usr/share/mime > /dev/null 2>&1
  fi

  if [ -x usr/bin/xdg-icon-resource ]; then
    xdg-icon-resource forceupdate --theme hicolor > /dev/null 2>&1
  fi

  if [ -x usr/bin/update-desktop-database ]; then
    usr/bin/update-desktop-database -q
  fi
}

# arg 1:  the new package version
post_install() {
  desktop_update
}

# arg 1:  the new package version
# arg 2:  the old package version
post_upgrade() {
  post_install "$1"
}

# arg 1:  the old package version
post_remove() {
  desktop_update
}

# vim:set ts=2 sw=2 ft=sh et:
