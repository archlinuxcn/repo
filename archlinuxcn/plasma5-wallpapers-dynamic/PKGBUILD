# Maintainer: Vlad Zahorodnii <vladzzag@gmail.com>
pkgname=plasma5-wallpapers-dynamic
pkgver=4.4.1
pkgrel=1
pkgdesc="Dynamic wallpaper plugin for KDE Plasma"
arch=(x86_64)
url="https://github.com/zzag/plasma5-wallpapers-dynamic"
license=('GPL')
depends=(libavif libexif plasma-framework5 qt5-base qt5-declarative qt5-location)
makedepends=(cmake extra-cmake-modules)
optdepends=('geoclue: automatic location detection support')
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/zzag/$pkgname/archive/$pkgver.tar.gz")
sha256sums=('99953135a7a984d405980fad00ab98409a15bab8ba09452ca6885023c9a2023c')

build() {
    cmake -B build -S $pkgname-$pkgver
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
