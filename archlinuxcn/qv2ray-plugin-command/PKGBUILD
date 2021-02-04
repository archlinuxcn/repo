# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=qv2ray-plugin-command
pkgver=2.0.0
pkgrel=2
pkgdesc="Qv2ray Plugin: Command"
arch=('x86_64')
url="https://github.com/Qv2ray/QvPlugin-Command"
license=('GPL3')
depends=('qt5-base' 'qv2ray')
makedepends=('cmake' 'git' 'ninja')
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
    install -Dm 755 libQvCommandPlugin.so -t "$pkgdir/usr/share/qv2ray/plugins/"
}
