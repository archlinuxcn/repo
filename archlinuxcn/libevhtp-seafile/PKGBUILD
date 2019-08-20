# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

_pkgname=libevhtp
pkgname="${_pkgname}"-seafile
pkgver=1.2.0
pkgrel=4
epoch=2
pkgdesc="A more flexible replacement for libevent's httpd API. [Built for seafile]"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/libevhtp"
license=('BSD')
depends=('libevent>=2.0.0' 'oniguruma')
makedepends=('cmake')
provides=('libevhtp')
conflicts=('libevhtp')
source=("${_pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz"
        "fixed_test_code.patch")
sha256sums=('d8d98072693f5f68ccd74d327dedfa2f6add4446ac2799689c2f58dd480aa301'
            '0e30ff28d0bda592fd70f9e4bee54499473c9b7de6e017422c8c6420735eb992')

prepare(){
  cd "${srcdir}/${_pkgname}-${pkgver}"

  patch -p1 < "${srcdir}"/fixed_test_code.patch

}

build () {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    cmake -DCMAKE_INSTALL_PREFIX=/usr -DEVHTP_DISABLE_SSL=ON -DEVHTP_BUILD_SHARED=ON ./
    make
}

package () {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
    rm -fv ${pkgdir}/usr/include/onigposix.h

    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
