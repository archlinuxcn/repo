# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=qv2ray-plugin-trojan
pkgver=2.0.0
pkgrel=3
pkgdesc="Qv2ray Plugin: Trojan"
arch=('x86_64')
url="https://github.com/Qv2ray/QvPlugin-Trojan"
license=('GPL3')
depends=('boost-libs' 'openssl' 'qt5-base' 'qv2ray')
makedepends=('boost' 'cmake' 'git' 'libffi' 'ninja' 'qt5-tools')
groups=('qv2ray-plugin')
source=("$pkgname-$pkgver::git+$url.git#tag=v$pkgver")
sha256sums=('SKIP')

prepare() {
    cd "$srcdir/$pkgname-$pkgver/"
    git submodule update --init
}

build() {
    cd "$srcdir/$pkgname-$pkgver/"
    mkdir -p build && cd build
    cmake .. \
        -DCMAKE_BUILD_TYPE=Release \
        -GNinja
    ninja
}

package() {
    cd "$srcdir/$pkgname-$pkgver/build/"
    install -Dm 644 libQvTrojanPlugin.so -t "$pkgdir/usr/share/qv2ray/plugins/"
}
