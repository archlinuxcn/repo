# Maintainer: kpn <kuzkin at gmail dot com>
# Maintainer: Bet4 <0xbet4@gmail.com>

_pkgname=fastcrc
pkgname=python-$_pkgname
pkgver=0.3.6
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
sha256sums=('58eb2409d37f47edd962d1a8df55fd018dd553e0830e7c016b92f4ecafb825fe')

build() {
  cd $_pkgname-$pkgver
  maturin build --release --strip
}

package() {
  cd $_pkgname-$pkgver
  python -m installer --destdir="$pkgdir" target/wheels/*.whl
}
