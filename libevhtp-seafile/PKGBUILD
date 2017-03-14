# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

_pkgname=libevhtp
pkgname="${_pkgname}"-seafile
pkgver=1.2.9
pkgrel=1
epoch=1
pkgdesc="A more flexible replacement for libevent's httpd API. [Built for seafile]"
arch=('i686' 'x86_64' 'armv5te' 'armv6h' 'armv7h')
url="https://github.com/ellzey/libevhtp"
license=('BSD')
depends=('libevent>=2.0.0' 'oniguruma')
makedepends=('cmake')
provides=('libevhtp')
conflicts=('libevhtp')
source=("${_pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('6a45125dab5211be5e0b6098b6d100f4aebe84dc6b80a9ce7211885fb3c4a97c')

build () {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    cmake -DCMAKE_INSTALL_PREFIX=/usr -DHAS_SYS_ONIG:FILEPATH="" -DEVHTP_DISABLE_SSL=ON -DEVHTP_BUILD_SHARED=ON ./
    make
}

package () {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    make DESTDIR="${pkgdir}" install
    rm -fv ${pkgdir}/usr/include/onigposix.h

    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
