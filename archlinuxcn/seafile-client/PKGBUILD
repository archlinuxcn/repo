# Maintainer: Joffrey <j-off@live.fr>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: localizator <localizator@ukr.net>
# Contributor: Edvinas Valatka <edacval@gmail.com>

pkgname=seafile-client
pkgver=8.0.3
pkgrel=1
pkgdesc='GUI client for synchronizing your local files with seafile server'
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/$pkgname"
license=('Apache')
depends=(
    "seafile>=$pkgver"
    'qt5-base'
    'qt5-webengine'
    'qt5-tools'
)
optdepends=('gtk-update-icon-cache')
makedepends=("cmake")
conflicts=('seafile-client-qt5')
provides=('seafile-client-qt5')
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('37241cddcfd0bbf46c41f346458fd93a27bec9879d3fd461145b24e8aa2405fb')

prepare() {
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
