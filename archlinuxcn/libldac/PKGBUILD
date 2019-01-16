# Maintainer: EHfive <eh5@sokka.cn>

pkgname=libldac
pkgver=2.0.2
pkgrel=2
pkgdesc="AOSP libldac dispatcher "
arch=("i686" "x86_64" "arm" "armv6h" "armv7h" "aarch64")
url="https://github.com/EHfive/ldacBT"
license=('Apache 2.0')
depends=()
makedepends=("cmake>=3.0" "make")
optdepends=()
provides=("ldacBT=2.0.2" "ldacBT_enc.so=2.0.2" "ldacBT_abr.so=2.0.2")
source=("https://github.com/EHfive/ldacBT/releases/download/1.1-ldac.2.0.2/ldacBT.tar.gz")

sha256sums=('3fc4269f0cab8ef11e119502c3441042889970d019420de47588ad8777524ab3')


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
