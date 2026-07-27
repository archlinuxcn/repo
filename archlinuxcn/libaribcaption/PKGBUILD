# Maintainer: Daniel Bermond <dbermond@archlinux.org>

pkgname=libaribcaption
pkgver=1.1.2
pkgrel=1
pkgdesc='Caption decoder/renderer library for handling ARIB STD-B24 based TV broadcast captions'
arch=('x86_64')
url='https://github.com/xqq/libaribcaption/'
license=('MIT')
depends=(
    'glibc'
    'fontconfig'
    'freetype2'
    'libgcc'
    'libstdc++')
makedepends=(
    'cmake')
source=("https://github.com/xqq/libaribcaption/archive/v${pkgver}/${pkgname}-${pkgver}.tar.gz")
sha256sums=('649b50bde99272b97c66af2a8400163e2f84eae072d252daa26baaaf0866a1c2')

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
