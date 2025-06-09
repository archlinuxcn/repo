# Maintainer:  Chris Severance aur.severach aATt spamgourmet dott com
# Contributor: Steven Honeyman <stevenhoneyman at gmail com>
# Contributor: Maxim Fomin <maxim at fomin one>

# Add yourself to the disk group to edit disks

set -u
pkgname='wxhexeditor'
pkgver=0.24
pkgrel=5
pkgdesc='A free hex editor / disk editor for Linux, Windows and MacOSX'
arch=('i686' 'x86_64')
url='http://www.wxhexeditor.org'
license=('GPL-2.0-only')
depends=('glibc' 'gcc-libs' 'wxwidgets-common' 'wxwidgets-gtk3')
makedepends=('python')
optdepends=('gksu: For root access support'
            'polkit: For root access support')
_srcdir="wxHexEditor-${pkgver}"
source=("${_srcdir}.tgz::https://github.com/EUA/wxHexEditor/archive/v${pkgver}.tar.gz"
        "01-add-pkexec-support.patch"
        "02-remove-strange-output.patch")
md5sums=('1b77bddc026e22797fd0e7a82e52cd28'
         'e62ae9e6b0aac2afdcc41b51cab39272'
         '9f8f2ea86c7cc1d4706ac8c4862cfb51')
sha256sums=('6ad993ba13a0076b31fb95daa7a812eae3b613d86f5e6709021e4d3398afcf00'
            'fbb88c153e0bcba91a18bd6c646e262793a0b91c9e0ff6c40c4341247a47f620'
            'ac9878adb6a25eca07b6ee8fcad07d4d655af23f6dcc49c418628184ab210f17')

prepare() {
  set -u
  cd "${_srcdir}"
  patch -Np1 -i "${srcdir}/01-add-pkexec-support.patch"
  patch -Np1 -i "${srcdir}/02-remove-strange-output.patch"
  sed -e '/WX_CLEAR_ARRAY/ s:)$:);:g' -i $(grep --include='*.cpp' -lre 'WX_CLEAR_ARRAY' .)
  set +u
}

build() {
  set -u
  cd "${_srcdir}"
  test -x '/usr/bin/wx-config' || echo "${}"
  export CFLAGS="${CFLAGS} -std=gnu17"
  make -s WXCONFIG='/usr/bin/wx-config'
  set +u
}

package() {
  set -u
  cd "${_srcdir}"
  make -j1 -s install DESTDIR="${pkgdir}" PREFIX='/usr'
  set +u
}
set +u
