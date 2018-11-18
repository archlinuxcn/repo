# Maintainer: Clayton Craft <clayton at craftyguy dot net>
pkgname=py-spy
pkgver=0.1.8
pkgrel=3
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/benfred/py-spy/archive/v$pkgver.tar.gz")
sha512sums=('68831d1c066887f3473e9eef1a773c0f9e1eb9252f929b0884b1d04faede90a72d7e3eb949d14e2e75c12e2645bf6b57ea5f94d5514491f46594231ad68ad1d1')

build() {
        cd "${srcdir}/${pkgname}-${pkgver}"
        cargo build --release
}

package() {
        cd "${srcdir}/${pkgname}-${pkgver}"
        install -Dm755 "target/release/py-spy" "${pkgdir}/usr/bin/py-spy"
        install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
        install -Dm644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}
