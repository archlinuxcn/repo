# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

_pkgname=libevhtp
pkgname="${_pkgname}"-seafile
pkgver=1.2.0
pkgrel=1
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
        "fix_test_code.diff::${url}/commit/18c649203f009ef1d77d6f8301eba09af3777adf.diff")
sha256sums=('d8d98072693f5f68ccd74d327dedfa2f6add4446ac2799689c2f58dd480aa301'
            'e541796e94dcc71c9167bc64aa2e76d13ef327605e40240e8abd736385bfccb8')

prepare(){
  cd "${srcdir}/${_pkgname}-${pkgver}"

  patch -p1 < "${srcdir}"/fix_test_code.diff

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
