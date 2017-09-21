# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: SaultDon <sault.don gmail>
# Contributor: Gunther Schulz < mail at guntherschulz.de >
# Contributor: Kévin Guilloy <kevin at guilloy dot ath dot cx>

pkgname=qwtpolar-qt4
_pkgname=qwtpolar
pkgver=1.1.1
pkgrel=1
pkgdesc='Qwt library that contains classes for displaying values on a polar coordinate system - Qt4 version'
arch=('i686' 'x86_64')
url='http://qwtpolar.sourceforge.net/'
license=('custom')
depends=('gcc-libs' 'glibc' 'qt4' 'qwt-qt4')
source=("https://sourceforge.net/projects/qwtpolar/files/$_pkgname/$pkgver/$_pkgname-$pkgver.tar.bz2")
sha1sums=('38edf5220c971eef0e88fcc6db7c718e6198ccac')

prepare() {
  cd $_pkgname-$pkgver

  sed -e '/^\s*QWT_POLAR_INSTALL_PREFIX/ s|=.*|= /usr|' \
      -e '/^QWT_POLAR_INSTALL_DOCS/ s|^|#|' \
      -e '/^QWT_POLAR_INSTALL_HEADERS/ s|include|&/qwt-qt4|' \
      -e '/^QWT_POLAR_INSTALL_PLUGINS/ s|plugins/designer|lib/qt4/&|' \
      -e '/^QWT_POLAR_INSTALL_FEATURES/ s|features|share/qt4/mkspecs/&|' \
      -e '/QwtPolarExamples/ s/^/#/' \
      -i qwtpolarconfig.pri

  sed -i '/^\s*\(LIBRARY_NAME\|LIB_NAME\)/ s/$/-qt4/' qwtpolarfunctions.pri
}

build() {
  cd $_pkgname-$pkgver

  qmake-qt4 qwtpolar.pro

  make
}

package() {
  cd $_pkgname-$pkgver

  make INSTALL_ROOT="$pkgdir" install

  install -Dm644 COPYING -t "$pkgdir/usr/share/licenses/$pkgname/"
}
