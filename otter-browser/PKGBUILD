# Maintainer: Steffen Weber <-boenki-gmx-de->

pkgname=otter-browser
pkgver=0.9.92
pkgrel=2
pkgdesc="Browser aiming to recreate classic Opera (12.x) UI using Qt5."
arch=('i686' 'x86_64')
url="https://$pkgname.org"
license=('GPL3')
depends=('qt5-multimedia' 'qt5-webkit' 'qt5-svg' 'hicolor-icon-theme' 'hunspell')
makedepends=('cmake' 'qt5-tools')
conflicts=('otter-browser-git')
source=($pkgname-$pkgver.tar.gz::https://github.com/OtterBrowser/$pkgname/archive/v$pkgver.tar.gz
$pkgname-check-if-frame-is-valid.patch::https://github.com/OtterBrowser/otter-browser/commit/6ea39464fe6c073e63642aa05afd4ed0bcfbc1a5.patch)
md5sums=('5c7087c6c17873846091a152b9df061d'
         'c48891aa5f6ad9123d7756164259f2b8')

prepare() {
 cd $pkgname-$pkgver
 patch -p1 -i ${srcdir}/$pkgname-check-if-frame-is-valid.patch
}

build() {
  cd $pkgname-$pkgver
  lrelease resources/translations/*.ts
  cmake -DCMAKE_INSTALL_PREFIX="/usr"
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR=$pkgdir install
}
