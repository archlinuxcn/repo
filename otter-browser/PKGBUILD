# Maintainer: Steffen Weber <-boenki-gmx-de->

pkgname=otter-browser
pkgver=0.9.99
pkgrel=1
pkgdesc="Browser aiming to recreate classic Opera (12.x) UI using Qt5."
arch=('x86_64')
url="https://$pkgname.org"
license=('GPL3')
depends=('qt5-multimedia' 'qt5-webkit' 'qt5-svg' 'hicolor-icon-theme' 'hunspell')
makedepends=('cmake' 'qt5-tools')
source=($pkgname-$pkgver.tar.gz::https://github.com/OtterBrowser/$pkgname/archive/v$pkgver.tar.gz)
md5sums=('54ccf11ae062a8438a628f6593c7534c')

build() {
  cd $pkgname-$pkgver
  lrelease resources/translations/*.ts
  cmake -DCMAKE_INSTALL_PREFIX="/usr"
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
