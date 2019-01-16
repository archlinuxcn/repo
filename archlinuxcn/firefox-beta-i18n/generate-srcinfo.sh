#!/bin/bash

set -e

if [[ 0 -ne $# ]]; then
  echo "Usage: $0" >&2
  echo "       $0 <-h|--help|help>" >&2

  case "$1" in
    -h|--help|help)
      exit 0
      ;;
    *)
      exit 1
      ;;
  esac
fi

if [[ ! -f 'PKGBUILD' ]]; then
  echo 'Cannot find PKGBUILD!' >&2
  exit 2
fi

# shellcheck disable=SC1091
source './PKGBUILD'

sed_args=()

# shellcheck disable=SC2154
for _locale in "${_locales[@]}"; do
  _as_lower="$(tr '[:upper:]' '[:lower:]' <<< "$_locale")"
  pkgname_pattern="^pkgname = $pkgbase-$_as_lower$"

  # Information parameters.
  infos_delim='\n\t'
  infos=("${infos_delim}pkgdesc = ${_languages["$_locale"]} language pack for Firefox Beta"
         "${infos_delim}provides = $pkgbase=$pkgver-$pkgrel"
         "${infos_delim}provides = firefox-i18n-$_as_lower=$pkgver"
         "${infos_delim}provides = firefox-developer-edition-i18n-$_as_lower=$pkgver"
         "${infos_delim}conflicts = firefox-i18n-$_as_lower"
         "${infos_delim}conflicts = firefox-developer-edition-i18n-$_as_lower")

  # shellcheck disable=SC2116
  sed_args+=(-e "s/$pkgname_pattern/\\0$(IFS=''; echo "${infos[*]}")/")
done

makepkg --printsrcinfo | sed "${sed_args[@]}" > '.SRCINFO'

# vim: set ts=2 sw=2 et syn=sh:
