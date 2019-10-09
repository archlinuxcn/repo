# Maintainer: Clayton Craft <clayton at craftyguy dot net>
pkgname=py-spy
pkgver=0.2.2
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("$pkgname-$pkgver.tar.gz::https://github.com/benfred/py-spy/archive/v$pkgver.tar.gz")
sha512sums=('6a38804e6a683410137bbfb8f485e5826bf80f1f5a4bff4e84c9dd6d2a3a548d8339ad59ab4409f91c0b028bd36a9b3967c8bb11bda1787741882455d0504723')

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
