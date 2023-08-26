# Maintainer: Daniel Bermond <dbermond@archlinux.org>

# NOTE:
# 10-bit depth is not supported currently
# https://github.com/pkuvcl/davs2/blob/1.7/build/linux/configure#L470

pkgname=davs2
pkgver=1.7
pkgrel=1
arch=('x86_64')
pkgdesc='Open-Source decoder of AVS2-P2/IEEE1857.4 video coding standard'
url='https://github.com/pkuvcl/davs2/'
license=('GPL')
depends=('glibc')
makedepends=('nasm')
provides=('libdavs2')
conflicts=('libdavs2')
replaces=('libdavs2')
options=('!lto')
source=("https://github.com/pkuvcl/davs2/archive/${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('b697d0b376a1c7f7eda3a4cc6d29707c8154c4774358303653f0a9727f923cc8')

build() {
    cd "${pkgname}-${pkgver}/build/linux"
    ./configure \
        --prefix='/usr' \
        --enable-shared \
        --disable-static \
        --bit-depth='8' \
        --chroma-format='all' \
        --enable-pic
    make
}

package() {
    make -C "${pkgname}-${pkgver}/build/linux" DESTDIR="$pkgdir" install-cli install-lib-shared
}
