# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=7.0.9
pkgrel=1
pkgdesc='GUI client for synchronizing your local files with seafile server'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('Apache')
depends=(
    'seafile'
    'qt5-base'
    'qt5-webengine'
    'qt5-tools'
)
optdepends=('gtk-update-icon-cache')
makedepends=("cmake")
conflicts=('seafile-client-qt5')
provides=('seafile-client-qt5')
source=(
    "$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz"
    'fix_QT5_v5.15_QPainterPath.diff'
)
sha256sums=(
    '200b258339cafcaf809f85d88cc53ff15b265673d74f3777c86809e26bf49738'
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
