# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=libaribcaption
pkgver=1.1.1
pkgrel=1
pkgdesc='Caption decoder/renderer library for handling ARIB STD-B24 based TV broadcast captions'
arch=('x86_64')
url='https://github.com/xqq/libaribcaption/'
license=('MIT')
depends=('fontconfig' 'freetype2')
makedepends=('cmake')
source=("https://github.com/xqq/libaribcaption/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('278d03a0a662d00a46178afc64f32535ede2d78c603842b6fd1c55fa9cd44683')

build() {
    cmake -B build -S "${pkgname}-${pkgver}" \
        -G 'Unix Makefiles' \
        -DCMAKE_BUILD_TYPE:STRING='None' \
        -DCMAKE_INSTALL_PREFIX:PATH='/usr' \
        -DARIBCC_SHARED_LIBRARY:BOOL='ON' \
        -Wno-dev
    cmake --build build
}

package() {
    DESTDIR="$pkgdir" cmake --install build
    install -D -m644 "${pkgname}-${pkgver}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
