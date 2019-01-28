# Maintainer: EHfive <eh5@sokka.cn>

pkgname=libldac
pkgver=2.0.2.2
pkgrel=1
pkgdesc="AOSP libldac dispatcher "
arch=("i686" "x86_64" "arm" "armv6h" "armv7h" "aarch64")
url="https://github.com/EHfive/ldacBT"
license=('Apache 2.0')
depends=()
makedepends=("cmake>=3.0" "make")
optdepends=()
provides=("ldacBT=2.0.2.2" "ldacBT_enc.so=2.0.2.2" "ldacBT_abr.so=2.0.2.2")
source=("https://github.com/EHfive/ldacBT/releases/download/v2.0.2.2/ldacBT-2.0.2.2.tar.gz")

sha256sums=('2baebf72de366178de67d014e52490577673858d030284243d61d0e507753d5e')


build() {
    cd "$srcdir/ldacBT"
    cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DINSTALL_LIBDIR=/usr/lib \
        -DLDAC_SOFT_FLOAT=OFF \
        .
    make
}

package() {
    cd "$srcdir/ldacBT"
    make DESTDIR="$pkgdir" install
}
