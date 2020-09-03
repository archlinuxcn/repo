# Maintainer: EHfive <eh5@sokka.cn>

pkgname=libldac
pkgver=2.0.2.3
pkgrel=3
pkgdesc="LDAC encoder and LDAC Adaptive Bit Rate(ABR) libraries"
arch=("i686" "x86_64" "arm" "armv6h" "armv7h" "aarch64")
url="https://github.com/EHfive/ldacBT"
license=('Apache 2.0')
depends=()
makedepends=("cmake>=3.0")
optdepends=()
provides=("ldacBT=$pkgver" "libldacBT_enc.so" "libldacBT_abr.so")
source=("https://github.com/EHfive/ldacBT/releases/download/v$pkgver/ldacBT-$pkgver.tar.gz")

sha256sums=('4bd8eece78bb5c1361fab95743e7100506e2408a25c4a592a0f8d349746dc5b4')


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
    install -Dm 644 LICENSE -t "$pkgdir"/usr/share/licenses/ldacBT
    install -Dm 644 libldac/LICENSE libldac/NOTICE -t "$pkgdir"/usr/share/licenses/ldacBT/libldac
}
