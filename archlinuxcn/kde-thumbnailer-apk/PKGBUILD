# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: Frikilinux <frikilinux at gmail.com>
# Contributor: Artem Sereda <overmind88@gmail.com>

pkgname=kde-thumbnailer-apk
pkgver=2.0
pkgrel=1
pkgdesc="Preview image generator plugin for Android Application Package files"
arch=('x86_64')
url="https://github.com/z3ntu/kde-thumbnailer-apk"
license=('GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL')
depends=('kio' 'libzip')
makedepends=('cmake' 'extra-cmake-modules')
source=("https://github.com/z3ntu/kde-thumbnailer-apk/archive/v$pkgver/$pkgname-v$pkgver.tar.gz")
sha512sums=('7ecda7a4b304ac022edde973c34232897aefd5726b5cb09fe1f1a867beb1f0826abfb086f1b472e38de8302125bccae266212bc59d0c135de67bb6e99c5f6144')

build() {
    cmake -B build -S "$pkgname-$pkgver" \
        -DCMAKE_BUILD_TYPE='None' \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
}
