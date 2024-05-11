# Maintainer: Evgenii Alekseev

pkgname=kiview
_pkgname=Kiview
pkgver=1.1
pkgrel=1
pkgdesc="Quick files preview for dolphin"
arch=('x86_64')
url="https://github.com/Nyre221/Kiview"
license=('GPL-3.0-only')
depends=('kcoreaddons' 'ki18n' 'kirigami' 'qt6-multimedia' 'qt6-webengine')
makedepends=('cmake' 'extra-cmake-modules')
source=("https://github.com/Nyre221/Kiview/archive/refs/tags/v${pkgver}.tar.gz")

build () {
    cmake -B build -S "$_pkgname-$pkgver"
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}

sha256sums=('e068dd8a7fe18222ad70b677414f9a6ab0fe5f338eb2dbcd6119e68675071e8a')
