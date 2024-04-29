# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-strenum
_name=StrEnum
pkgver=0.4.15
pkgrel=3
pkgdesc="A Python Enum that inherits from str."
arch=('any')
url="https://github.com/irgeek/StrEnum"
license=('MIT')
depends=('python')
makedepends=(
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
)
#checkdepends=(
#  'python-pytest-black'
#  'python-pytest-cov'
#  'python-pytest-pylint'  ## Dropped to AUR
#)
source=("$_name-$pkgver.tar.gz::https://github.com/irgeek/StrEnum/archive/refs/tags/v$pkgver.tar.gz"
        'https://github.com/irgeek/StrEnum/pull/34.patch')
sha256sums=('ab442e918760a39a3b07e7923c128ff13a0bbebc6a173cda67237acb738d7e49'
            'f39d3b96dfc0447a3c54ec8083f90e3c40ce92196e232e694cec232bf8709fb0')

prepare() {
  cd "$_name-$pkgver"

  # Drop pytest-runner
  sed -i '/pytest-runner/d' setup.py

  # Replace SafeConfigParser and readfp
  patch -Np1 -i ../34.patch
}

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

#check() {
#  cd "$_name-$pkgver"
#  pytest
#}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
