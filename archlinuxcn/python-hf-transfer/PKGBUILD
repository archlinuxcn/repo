# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=hf_transfer
pkgname=python-hf-transfer
pkgver=0.1.9
pkgrel=1
pkgdesc='Speed up file transfers with the Hugging Face Hub'
arch=('x86_64')
url='https://github.com/huggingface/hf_transfer'
license=('Apache-2.0')
depends=(
  gcc-libs
  glibc
  openssl
  python
)
makedepends=(
  python-build
  python-maturin
  python-installer
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/huggingface/hf_transfer/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('b6e107ab12bb389fef5c0701b96c839b6014b1e0250e78eebe8e1e02dc5aaeaa70a01d34678a222e0271cfc21ffd703143420877e53662f85ec2d2edfbf20885')

build() {
  cd "${_pkgname}-${pkgver}"
  # use system openssl
  OPENSSL_NO_VENDOR=1 \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
