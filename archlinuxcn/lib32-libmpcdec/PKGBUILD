# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_basename=libmpcdec
pkgname=lib32-libmpcdec
pkgver=0.1+r475
pkgrel=3
epoch=1
_rel=475
pkgdesc="Musepack decoding library (32 bit)"
arch=(x86_64)
url="http://musepack.net/"
license=(custom)
depends=(lib32-glibc libmpcdec)
makedepends=(lib32-libreplaygain lib32-libcue)
source=("http://files.musepack.net/source/musepack_src_r${_rel}.tar.gz"
        01_am-maintainer-mode.patch
        02_link-libm.patch
        03_mpcchap.patch
        04_link-order.patch
        05_visibility.patch
        1001_missing_extern_kw.patch
        add_subdir-objects.patch)
sha256sums=('a4b1742f997f83e1056142d556a8c20845ba764b70365ff9ccf2e3f81c427b2b'
            '76b5b7295f5e0be5de7edeb2ef481fe912cef349be5bd26f8b0870572a1ed5ee'
            'cf7ded3474ecefbe877a672539996b99dd6d62be546b74b70c4d56a7b943952d'
            'c6ef8e91b8e4450854d14e47fb4b4bde643b3f22a0d30cd0fae79d1897feb9f7'
            'b184df85c164cb6f37e077b5511bee994e767f25f641d5a44ad3877db0e7eba1'
            'db78faeb4944ab443c89a1da058693e419a8eef1ca4859550afcc6232ec407fb'
            'b736438a93fa5cc10bde753e82a0ce432db5c8c9a4a0689baa738d421166bff4'
            '88e2d7df269c8f19daccb98bd9d1a2bdc9002c7ea03ca093e2dc68b0fb04e636')

prepare() {
    cd musepack_src_r${_rel}

    patch -Np1 -i ../01_am-maintainer-mode.patch
    patch -Np1 -i ../02_link-libm.patch
    patch -Np1 -i ../03_mpcchap.patch
    patch -Np1 -i ../04_link-order.patch
    patch -Np1 -i ../05_visibility.patch
    patch -Np1 -i ../1001_missing_extern_kw.patch
    patch -Np1 -i ../add_subdir-objects.patch

   mv configure.in configure.ac

    autoreconf -fi
}

build() {
    cd musepack_src_r${_rel}

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --enable-mpcchap

    make
}

package() {
    cd musepack_src_r${_rel}

    make -C libmpcdec DESTDIR="${pkgdir}" install

    install -Dm644 libmpcdec/COPYING "${pkgdir}/usr/share/licenses/lib32-libmpcdec/COPYING"
}
