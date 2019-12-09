# Maintainer: Clayton Craft <clayton at craftyguy dot net>
pkgname=py-spy
pkgver=0.3.1
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("$pkgname-$pkgver.tar.gz::https://github.com/benfred/py-spy/archive/v$pkgver.tar.gz")
sha512sums=('79c6eb70e7b003183587debd69f6399b5e2dda598e8e1c235905d3843637427dd8b145de13228bf67cadc89a5bc249ff7184e464ccd88ad4c5b0be4fec687115')

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
