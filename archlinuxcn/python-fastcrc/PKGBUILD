# Maintainer: kpn <kuzkin at gmail dot com>
# Maintainer: Bet4 <0xbet4@gmail.com>

_pkgname=fastcrc
pkgname=python-$_pkgname
pkgver=0.5.0
pkgrel=1
pkgdesc="A hyper-fast Python module for computing CRC(8, 16, 32, 64) checksum"
arch=(x86_64)
url="https://github.com/overcat/fastcrc"
license=(MIT)
depends=(python)
makedepends=(
  maturin
  python-installer
  rust
)
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('e02cdf379d7371f0bd9d7cac957c67f0696e62292d73eebe02ff6393eef05b50')

build() {
  cd $_pkgname-$pkgver
  maturin build --release --strip
}

package() {
  cd $_pkgname-$pkgver
  python -m installer --destdir="$pkgdir" target/wheels/*.whl
}
