# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Klaus Alexander Seiﬆrup <klaus@seistrup.dk>

pkgname='python-jh2'
_srcname='h2'
pkgver=5.0.11
pkgrel=1
pkgdesc='HTTP/2 State-Machine based protocol implementation'
arch=('aarch64' 'x86_64')
url='https://github.com/jawah/h2'
license=('MIT')  # SPDX-License-Identifier: MIT
depends=(
  'libgcc'
  'glibc'
  'python'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-maturin'
  'python-setuptools'
  'python-wheel'
)
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('9fe909fa5a6b3aafeac08949cc03de3a2059de8b21a98eb7c3c7e17b2e65ba0d')

_srcdir="$_srcname-$pkgver"

build() {
  cd "$_srcdir"

  python -m build --wheel --no-isolation
}

package() {
  cd "$_srcdir"

  python -m installer --destdir="$pkgdir" dist/*.whl

  install -vDm0644 -t "$pkgdir/usr/share/doc/$pkgname/" \
    {CHANGELOG,README}.rst

  install -vDm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" \
    LICENSE
}
