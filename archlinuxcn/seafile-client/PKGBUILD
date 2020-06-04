# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=7.0.8
pkgrel=1
pkgdesc='GUI client for synchronizing your local files with seafile server'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('Apache')
depends=(
    'seafile'
    'qt5-base'
    'qt5-webengine'
    'qt5-webkit'
    'qt5-tools'
    'gtk-update-icon-cache'
)
makedepends=("cmake")
conflicts=('seafile-client-qt5')
provides=('seafile-client-qt5')
source=(
    "$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
    'fix_QT5_v5.15_QPainterPath.diff'
)
sha256sums=(
    '9c737acc7d6e92e36625156346b866c2e90fa5900828fc77a28ed4f622629bae'
    '300d77db22b8f0845faa4442afc557d46c21b758b7b3be75381e5a2dd58fef07'
)
prepare() {
    cd "$srcdir/$pkgname-$pkgver"
    patch -p1 -i "$srcdir/fix_QT5_v5.15_QPainterPath.diff"

    cd "$srcdir"
    rm -rf build
    mkdir -p build
}

build() {
    cd "$srcdir/build"
    cmake \
        -DBUILD_TESTING=ON \
        -DBUILD_SHIBBOLETH_SUPPORT=ON \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX='/usr' \
        "$srcdir/$pkgname-$pkgver"
    make
}

check() {
    cd "$srcdir/build"
    make test
}

package() {
    cd "$srcdir/build"
    make DESTDIR="$pkgdir" install
}
