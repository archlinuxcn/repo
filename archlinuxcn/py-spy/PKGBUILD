# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Clayton Craft <clayton@craftyguy.net>
pkgname=py-spy
pkgver=0.3.14
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("https://github.com/benfred/py-spy/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('f079b002248a033eac3b93723fd267e6cbdb415ac3172ace0d14eb9cd87a1e4adf471eeec641f9644abe8a4fab43b48db7440b4b1242ea18e02bcc574104d303')

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
