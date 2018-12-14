# Maintainer: Clayton Craft <clayton at craftyguy dot net>
pkgname=py-spy
pkgver=0.1.10
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo')
source=("$pkgname-$pkgver.tar.gz::https://github.com/benfred/py-spy/archive/v$pkgver.tar.gz")
sha512sums=('527aa93d88db3b6544b4a2fed7930198c2aa16e2aa4f4579478fdb36d367adc9ce82ca66ce31de5ddb9ce847ce22faf4ed0b8795d8ff518ac1aaa61c2382a008')

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
