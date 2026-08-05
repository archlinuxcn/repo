#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *
import os

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('edk2-ovmf')

  for f in g.files:
    if f != 'PKGBUILD':
      os.remove(f)

  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64) # Avoid conflicting with the official package in the x86 repo'
    if line.startswith('pkgrel='):
      print(f"_upstream_{line}")
    print(line)
  with open('PKGBUILD', 'a') as f:
    f.write(r"""
makedepends=()
source=()
noextract=()
for _name in "${pkgname[@]}"; do
  source+=(https://mirrors.kernel.org/archlinux/extra/os/x86_64/${_name}-${pkgver}-${_upstream_pkgrel}-any.pkg.tar.zst)
  noexxtract+=(${_name}-${pkgver}-${_upstream_pkgrel}-any.pkg.tar.zst)
  eval "package_$_name() {
    _package $_name
  }"
done

prepare() {
  :
}

build() {
  :
}

_package() {
  _name="$1"
  rm -rf unpack-$_name
  mkdir unpack-$_name
  cd unpack-$_name

  bsdtar xf ../${_name}-${pkgver}-${_upstream_pkgrel}-any.pkg.tar.zst

  rm .BUILDINFO .MTREE

  if [[ -f .INSTALL ]]; then
    mv .INSTALL "${startdir}/$_name.install"
    install=$_name.install
  fi
  arch=(aarch64)

  replaces=()
  conflicts=()
  provides=()
  while read line; do
    if ! [[ $line =~ ^([a-z].*)\ =\ (.*) ]]; then
      continue
    fi
    _key="${BASH_REMATCH[1]}"
    _value="${BASH_REMATCH[2]}"
    case $_key in
      pkgdesc)
        pkgdesc="$_value"
        ;;
      url)
        url="$_value"
        ;;
      replaces)
        replaces+=("$_value")
        ;;
      conflict)
        conflicts+=("$_value")
        ;;
      provides)
        provides+=("$_value")
        ;;
      pkgname|pkgbase|xdata|pkgver|builddate|packager|size|arch|license|makedepend)
        ;;
      *)
        echo "Unhandled PKGINFO: $_key = $_value"
        ;;
    esac
  done < .PKGINFO
  rm .PKGINFO
  mv * "${pkgdir}"
}
""")
  run_protected(["updpkgsums"])
