# Maintainer: Clayton Craft <clayton@craftyguy.net>
pkgname=py-spy
pkgver=0.3.4
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("$pkgname-$pkgver.tar.gz::https://github.com/benfred/py-spy/archive/v$pkgver.tar.gz")
sha512sums=('471547eadeaf6fef5d2a6a36db0b6e01a70ce2eb82ac3e82b0f6242162916172ddc9865daced7de20104d693e24b23cd8b3f545d9977eba09bbe68f715e9622c')

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
