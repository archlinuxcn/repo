# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Clayton Craft <clayton@craftyguy.net>
pkgname=py-spy
pkgver=0.3.13
pkgrel=2
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("https://github.com/benfred/py-spy/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('83d4f76672002edf8189ed2917046cfea035c9e6a24b4e25eb04614340c361b459e44ec2edd658969a629743953791f880ce3728e93e732793e6815932d38838')

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
