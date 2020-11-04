# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: josephgbr <rafael.f.f1 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>

_basename=faac
pkgname=lib32-faac
pkgver=1.30
pkgrel=2
pkgdesc="Freeware Advanced Audio Coder"
arch=(x86_64)
url="https://www.audiocoding.com/"
license=('GPL2' 'custom')
depends=(lib32-glibc faac)
source=(${_basename}-${pkgver}.tar.gz::"https://github.com/knik0/${_basename}/archive/${pkgver/./_}.tar.gz")
sha512sums=('8582cd580dba2a347d15dc4fab42020d7120d0552c54ab74cfaf59ba1b270abb94c67e39d42459a14cbc6e98f3fd00cbda589e1b4f0c7278e41bdef6ae7b6554')

prepare() {
    mv -v "${_basename}-${pkgver/./_}" "${_basename}-${pkgver}"

    cd "${_basename}-${pkgver}"

    autoreconf -vfi
}

build() {
    cd "${_basename}-${pkgver}"

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32

    make
}

package() {
    cd "${_basename}-${pkgver}"

    make DESTDIR="$pkgdir" install

    rm -rf "$pkgdir"/usr/{bin,include,share}

    install -Dm644 "${srcdir}"/${_basename}-${pkgver}/COPYING \
     "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
