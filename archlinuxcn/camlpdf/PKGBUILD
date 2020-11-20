# Maintainer: Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: oliver < a t >  first . in-berlin . de

set -u
pkgname='camlpdf'
#_pkgver='2.1.1'
#_pkgver='2.2'
#_pkgver='2.2precrypt'
#_pkgver='2.2-patchlevel1'
#_pkgver='2.3'
_pkgver='2.3.1'
pkgver="${_pkgver//atchlevel/}"
pkgver="${pkgver//-/.}"
pkgrel='1'
pkgdesc='Coherent Graphics OCaml library for reading, writing and modifying PDF files'
arch=('i686' 'x86_64')
url="https://github.com/johnwhitington/camlpdf"
license=('LGPL')
depends=('glibc')
makedepends=('ocaml-findlib')
options=('!makeflags' 'staticlibs')
_srcdir="camlpdf-${_pkgver}"
source=("${_srcdir}.tar.gz::https://github.com/johnwhitington/camlpdf/archive/v${_pkgver}.tar.gz")
md5sums=('84baae9a24d7ceac55c59907720f14e1')
sha256sums=('40b68d660247164a8ac0093c20f6c521cc95ed310f6b9a3bca3792a4db29dfd0')

_setvars() {
  OCAMLFIND_DESTDIR="${pkgdir}/$(ocamlfind printconf destdir)"
  OCAMLFIND_LDCONF="${pkgdir}/$(ocamlfind printconf ldconf)"
}

build() {
  set -u
  cd "${_srcdir}"

  local OCAMLFIND_DESTDIR OCAMLFIND_LDCONF; _setvars
  make -s OCAMLFIND_DESTDIR="${OCAMLFIND_DESTDIR}"
  set +u
}

package() {
  set -u
  cd "${_srcdir}"

  local OCAMLFIND_DESTDIR OCAMLFIND_LDCONF; _setvars
  install -d "${OCAMLFIND_DESTDIR}"
  make -s install -d OCAMLFIND_DESTDIR="${OCAMLFIND_DESTDIR}" OCAMLFIND_LDCONF="${OCAMLFIND_LDCONF}"
  set +u
}
set +u
