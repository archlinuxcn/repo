# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>
# Contributor: Hans-Nikolai Viessmann <hans AT viess.mn>
# Contributor: max_meyer
# Contributor: popsch
# Based on original tikzit-aur-package made by pippin

pkgname=tikzit
pkgver=2.1.5
pkgrel=2
pkgdesc="Allows the creation and modification of TeX diagrams written using the pgf/TikZ macro library"
arch=('i686' 'x86_64')
url="https://tikzit.github.io/"
license=('GPL2')
depends=('qt5-base' 'poppler-qt5' 'hicolor-icon-theme')
optdepends=('texlive-core: previews')
source=("$pkgname-$pkgver.tar.gz::https://github.com/tikzit/tikzit/archive/v$pkgver.tar.gz")
sha256sums=('f2c3ff7d8f7eb9fd4f5b29d8105e0d2930b1b736d2c06efddb6f20122a9a85ca')

build() {
  cd $pkgname-$pkgver
  qmake PREFIX=/usr \
        QMAKE_CFLAGS="${CFLAGS}" \
        QMAKE_CXXFLAGS="${CXXFLAGS}" -r
  make
}

package() {
  cd $pkgname-$pkgver
  make INSTALL_ROOT="$pkgdir" install
}
