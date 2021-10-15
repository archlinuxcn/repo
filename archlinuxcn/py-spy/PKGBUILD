# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Clayton Craft <clayton@craftyguy.net>
_name=py_spy
pkgname=py-spy
pkgver=0.3.10
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('c3ddeffe645b6f04ed9384bcb349d215db21c9011842b3a1f09ec727e8f0724d0e270a2a31a7a3f94a3f4d91bef90a498a248e70472fdf72e148835c89417bc0')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  cargo build --release
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  install -Dm755 "target/release/py-spy" "${pkgdir}/usr/bin/py-spy"
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -Dm644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}
