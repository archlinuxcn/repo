# Maintainer: Yiyao Yu <yuydevel at protonmail dot com>
# Contributor: Moritz Lipp <mlq@pwmt.org>

pkgname=bear
_pkgname=Bear
pkgver=3.0.10
pkgrel=1
pkgdesc="tool to generate compilation database for clang tooling"
arch=('i686' 'x86_64')
url="https://github.com/rizsotto/Bear"
license=('GPL3')
makedepends=('cmake' 'ninja' 'nlohmann-json')
depends=('grpc' 'fmt' 'spdlog')
conflicts=('bear' 'interception-tools')
provides=('bear')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/rizsotto/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('9d774b0b17edbded86b76681a3fc85517ef916a359b252acd97ef63aa7a1cbbf')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    cmake -DCMAKE_INSTALL_PREFIX=/usr \
          -DCMAKE_INSTALL_SYSCONFDIR=/etc \
          -DCMAKE_INSTALL_LIBEXECDIR="lib/${pkgname}" \
          -DENABLE_UNIT_TESTS=OFF \
          -DENABLE_FUNC_TESTS=OFF \
          .

    make all
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    DESTDIR="${pkgdir}" make install

    # Workaround for including compile dir in package
    rm -rf "${pkgdir}${srcdir}"
    find "${pkgdir}" -empty -type d -delete
}
