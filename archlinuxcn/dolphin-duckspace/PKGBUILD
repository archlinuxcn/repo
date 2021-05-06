# Maintainer: DuckSoft <realducksoft at gmail dot com>
# Maintainer: Antonio Rojas <arojas@archlinux,org>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Pierre Schmitz <pierre@archlinux.de>

pkgname=dolphin-duckspace
_pkgname=dolphin
pkgver=21.04.0
pkgrel=1
pkgdesc="KDE File Manager (with DuckSoft's Space Patch)"
arch=(x86_64)
url="https://kde.org/applications/system/dolphin/"
license=(LGPL)
provides=(dolphin)
conflicts=(dolphin)
depends=(baloo-widgets knewstuff kio-extras kcmutils kparts kinit kactivities kuserfeedback)
makedepends=(extra-cmake-modules kdoctools packagekit-qt5)
optdepends=('kde-cli-tools: for editing file type options' 'ffmpegthumbs: video thumbnails' 'kdegraphics-thumbnailers: PDF and PS thumbnails'
            'konsole: terminal panel' 'purpose: share context menu' 'packagekit-qt5: service menu installer')
source=("https://download.kde.org/stable/release-service/$pkgver/src/$_pkgname-$pkgver.tar.xz"
        "ducksoft-want-my-space-back.patch")
sha256sums=('4988e59d4e3edfd58c2d0857745398fc1840c87ec03ea13b0d73254874cfbdbe'
            '21a50881ce6dce2a831d8fc0e2d1339a158aaabc65986bbe3c9e990a4a71fcbe')

prepare() {
    cd "$srcdir"/$_pkgname-$pkgver
    patch -p1 < ../ducksoft-want-my-space-back.patch
}
              
build() {
  cmake -B build -S $_pkgname-$pkgver \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
