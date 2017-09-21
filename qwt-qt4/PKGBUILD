# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Ronald van Haren <ronald.archlinux.org>

pkgname=qwt-qt4
_pkgname=qwt
pkgver=6.1.3
pkgrel=1
pkgdesc='Qt Widgets for Technical Applications - Qt4 version'
arch=('i686' 'x86_64')
url='http://qwt.sourceforge.net/'
depends=('gcc-libs' 'glibc' 'qt4')
license=('custom')
source=("https://downloads.sourceforge.net/$_pkgname/$_pkgname-$pkgver.tar.bz2")
sha1sums=('90ec21bc42f7fae270482e1a0df3bc79cb10e5c7')

prepare() {
  cd $_pkgname-$pkgver

  sed -e '/^\s*QWT_INSTALL_PREFIX/ s|=.*|= /usr|' \
      -e '/^QWT_INSTALL_DOCS/ s|^|#|' \
      -e '/^QWT_INSTALL_HEADERS/ s|include|&/qwt-qt4|' \
      -e '/^QWT_INSTALL_PLUGINS/ s|plugins/designer|lib/qt4/&|' \
      -e '/^QWT_INSTALL_FEATURES/ s|features|share/qt4/mkspecs/&|' \
      -i qwtconfig.pri

  sed -i '/^\s*\(LIBRARY_NAME\|LIB_NAME\)/ s/$/-qt4/' qwtfunctions.pri
}

build() {
  cd $_pkgname-$pkgver

  qmake-qt4 qwt.pro

  make
}

package() {
  cd $_pkgname-$pkgver

  make INSTALL_ROOT="$pkgdir" install

  install -Dm644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname/"
}
