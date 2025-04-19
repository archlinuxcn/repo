#!/bin/bash
# Maintainer: capezotte
# Contributor: Seto (huresche at GitHub)
# Contributor: Koichi Murase (akinomyoga at GitHub)

_ble_base_package_type=AUR

function ble/base/package:AUR/version_check {
  LC_ALL=C pacman -Qi blesh-git | sed -n 's/^Version[[:space:]]*:[[:space:]]*//p'
}

function ble/base/package:AUR/update {
  local PKGNAME='blesh-git'
  local PRE_VERSION POST_VERSION
  ble/util/assign PRE_VERSION ble/base/package:AUR/version_check
  # Try to use an AUR helper
  local helper_exit
  (
    # Check for common AUR helpers
    available=(); default_helper='';
    for helper in yay paru pacaur pikaur pakku aura yaourt aurman trizen; do
      ble/bin#has "$helper" || continue
      ble/array#push available "$helper"
      [[ ! $default_helper && $_ble_base_repository == */"$helper"* ]] && default_helper=$helper
    done

    if ((${#available[@]})); then
      ble/array#push available built-in

      if [[ $default_helper ]]; then
        # Bring the default to the beginning of the list
        ble/array#remove available "$default_helper"
        ble/array#unshift available "$default_helper"
      fi

      local PS3="Which AUR helper to use? [${default_helper:+d: $default_helper (default), }x: cancel]? "
      NEEDS_ROOT=''; OPERATION='S';
      select helper in "${available[@]}"; do
        # Check if default was set
        [[ ${helper:=$REPLY} = [dD] || $REPLY = default ]] && helper=$default_helper
        # Special case: Aura
        [[ $helper = aura ]] && { NEEDS_ROOT=1; OPERATION='Ax'; }
        case $helper in
        (aura|yay|paru|pacaur|pikaur|pakku|yaourt|aurman|trizen)
          ble/util/print "Selected helper: $helper"
          exec ${NEEDS_ROOT:+sudo} "$helper" "-$OPERATION" "$PKGNAME"
          break ;;
        (built-in)
          ble/util/print 'Using built-in AUR helper.'
          exit 3 ;;
        ([xX]|exit|[cC]|cancel)
          ble/util/print >&2 'Canceled by the user.'
          exit 1 ;;
        esac
      done
      # Did not exec into a helper
      ble/util/print >&2 'AUR helper failed.'
      exit 1
    else
      ble/util/print >&2 'AUR helper not found, using built-in.'
      exit 3
    fi
  )
  helper_exit=$?

  # Hope this exit code isn't used by "No" in some AUR helper
  local makepkg_exit
  if ((helper_exit == 3)); then
    # Try to build from scratch
    (
      LOCALR=~/.cache/blesh/package
      ble/util/print "Trying set up a build environment at $LOCALR"
      AURREPO="https://aur.archlinux.org/${PKGNAME}.git"

      set -ex
      [[ -w ${LOCALR%/*} ]]
      mkdir -p "$LOCALR" && builtin cd "$LOCALR"
      git clone "$AURREPO" || [[ $(builtin cd "$PKGNAME" && git remote get-url origin) == "$AURREPO" ]]
      builtin cd "$PKGNAME"
      # Discard changes made by makepkg
      git reset --hard HEAD
      git pull
      exec makepkg -fsi
    )
    makepkg_exit=$?
  else
    makepkg_exit=$helper_exit
  fi

  ble/util/assign POST_VERSION ble/base/package:AUR/version_check

  # TODO: make AUR helpers not build already up-to-date packages:
  # (could be used to check for makepkg (1) exit code 13)
  # [ "$makepkg_exit" -eq 13 ] && return 6
  if ((makepkg_exit == 0)); then
    [[ $PRE_VERSION == "$POST_VERSION" ]] && return 6
    return 0
  fi
  # Just return 1 if we reached this point
  return 1
}
