# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Clayton Craft <clayton@craftyguy.net>
_name=py_spy
pkgname=py-spy
pkgver=0.3.11
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('891ab9f2b89e011ada12ad40e13503ef3bdaafb72f92a34d7ccd41a6275122f427dabdc6017baeecdb37fa33561843b827c756ae9518becb4fbe34a17af153c2')

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
