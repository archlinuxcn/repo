# Maintainer: lilydjwg <lilydjwg@gmail.com>
# Contributor: Clayton Craft <clayton@craftyguy.net>
_name=py_spy
pkgname=py-spy
pkgver=0.3.12
pkgrel=1
pkgdesc="Sampling profiler for Python programs"
arch=('x86_64')
license=('GPL3')
url="https://github.com/benfred/py-spy"
makedepends=('rust' 'cargo' 'libunwind')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha512sums=('4583de4ccfbb2db1a74a00c98ed90b2d1a5b57700ee00937bb18d3da8e9101b49480e558248acfcb03892158c74d4f6a1f965289070f6a4a8ad8ceda09e304cb')

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
