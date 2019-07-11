# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=taglib-extras
pkgver=1.0.1
pkgrel=7
pkgdesc="Additional taglib plugins"
arch=('x86_64' 'aarch64')
url="https://developer.kde.org/~wheeler/taglib.html"
license=('LGPL')
depends=('taglib')
makedepends=('cmake')
source=("https://download.kde.org/stable/$pkgname/$pkgver/src/$pkgname-$pkgver.tar.gz" taglib-1.10.patch)
sha256sums=('fe546b4b315f3227c975fed8ea9dfc0e54fc6997fdbba2a9da7beba479229632'
            '31673efa5f655b26e5f28277bfb97b3d85d7c9f9e650a229227afe09ae2f9749')

prepare() {
  [[ -d build ]] || mkdir -p build

# Fix taglib 1.10 detection
  cd $pkgname-$pkgver
  patch -p1 -i "$srcdir"/taglib-1.10.patch
}

build() {
  cd build
  cmake ../$pkgname-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
}
