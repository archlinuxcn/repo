# Maintainer: Yiyao Yu <yuydevel at protonmail dot com>
# Contributor: Moritz Lipp <mlq@pwmt.org>

pkgname=bear
_pkgname=Bear
pkgver=3.0.0
pkgrel=1
pkgdesc="tool to generate compilation database for clang tooling"
arch=('i686' 'x86_64')
url="https://github.com/rizsotto/Bear"
license=('GPL3')
makedepends=('cmake' 'ninja')
depends=('python' 'grpc' 'fmt' 'spdlog' 'nlohmann-json')
# Needed for cmake to build correctly
options=('!buildflags')
conflicts=('bear')
provides=('bear')
source=($_pkgname-$pkgver.tar.gz::https://github.com/rizsotto/$_pkgname/archive/$pkgver.tar.gz)
sha256sums=('7b68aad69e887d945ad20f8e9f3a8c33cf2d59cc80da7e52d931d8c685fe2f79')

build() {
    cd "$srcdir/$_pkgname-$pkgver"
    cmake -DCMAKE_INSTALL_PREFIX=/usr \
          -DENABLE_UNIT_TESTS=OFF \
          -DENABLE_FUNC_TESTS=OFF \
          .
    make all
}

package() {
    cd "$srcdir/$_pkgname-$pkgver"
    DESTDIR="$pkgdir" make install

    # No idea why this is generated in the pkgbuild since it behaves normally
    # outside of PKGBUILD. Dirty hack until I have time to fix this and
    # the !buildflags issue
    rm -r "$pkgdir/${srcdir:1}"
    find "$pkgdir" -empty -type d -delete
}
