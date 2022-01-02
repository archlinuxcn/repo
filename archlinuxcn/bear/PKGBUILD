# Maintainer: Yiyao Yu <yuydevel at protonmail dot com>
# Contributor: Moritz Lipp <mlq@pwmt.org>

pkgname=bear
_pkgname=Bear
pkgver=3.0.18
pkgrel=1
pkgdesc="tool to generate compilation database for clang tooling"
arch=('i686' 'x86_64' 'aarch64')
url="https://github.com/rizsotto/Bear"
license=('GPL3')
makedepends=('cmake')
depends=('grpc' 'fmt' 'spdlog' 'nlohmann-json')
conflicts=('bear')
provides=('bear')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/rizsotto/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('ae94047c79b4f48462b66981f66a67b6a833d75d4c40e7afead491b1865f1142')

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
}
