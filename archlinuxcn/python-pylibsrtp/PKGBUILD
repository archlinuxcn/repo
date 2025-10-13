# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibsrtp
pkgname=python-pylibsrtp
pkgver=1.0.0
pkgrel=1
pkgdesc='Python bindings for libsrtp'
arch=('x86_64')
url='https://github.com/aiortc/pylibsrtp'
license=('BSD-3-Clause')
depends=(
  glibc
  libsrtp
  python-cffi
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/aiortc/pylibsrtp/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('5d02a456fef6a6b091ec722f93f02721fe0385629391ab9b520a31aad754cb8ac94e2d0a7619cd43ddc18bf1e3c10fa567c879525bc1c142dc5e22a8e32e259c')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
