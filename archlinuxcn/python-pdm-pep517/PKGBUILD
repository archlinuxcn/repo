# Maintainer: David Runge <dvzrv@archlinux.org>

# set to 0 to use vendored sources
_devendored=1
_name=pdm-pep517
pkgname=python-pdm-pep517
# WARNING: python-pdm may not be compatible with whatever pdm-pep517 can be upgraded to:
# https://github.com/pdm-project/pdm/issues/1165
pkgver=1.1.4
pkgrel=4
epoch=1
pkgdesc="A PEP 517 backend for PDM that supports PEP 621 metadata"
arch=(any)
url="https://github.com/pdm-project/pdm-pep517"
license=(MIT)
depends=(python)
if (( _devendored == 1 )); then
  # NOTE: devendored from sources
  depends+=(
    python-cerberus
    python-license-expression
    python-packaging
    python-tomli
    python-tomli-w
  )
fi
makedepends=(
  python-build
  python-installer
)
checkdepends=(
  git
  python-pytest
  python-setuptools
)
optdepends=(
  'python-setuptools: for setuptools support'
)
source=(
  https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz
  $pkgname-1.1.2-devendor.patch
)
sha512sums=('a9d56974cc451a7daf67a7bbcb1b03ded72c024f535dd87bacae5b29598101c44b404ef74a1389f0ed8158702d4bb6af32b4d4d763dcb91ef7793d0508b279a7'
            'a1342cf49f4da1e5e22f5ffe7b50f89e48b20de81058d4d560ab8ed978c67f4ec8b760bfb4fde273c6ab96a21c28936a55875449c377131505c938e7f6b23fca')
b2sums=('a1e43071e7b11bff4873be4233b9ff10c8ca2d0385fbd762f7c604b57f7bc850506d4d46fce61abf78c6412a6ef7a4ecd43c7844e8548863eedc1de4185cea3e'
        'e259c5dc7d2617370197c9ab9f2f55c2541e256af98fc219dca057cae687cea284ff53c94e80ed47b1c9a28dadf22d08c4c0ada35f0785167c140c949b81f5ee')

prepare() {
  if (( $_devendored == 1 )); then
    patch -Np1 -d $_name-$pkgver -i ../$pkgname-1.1.2-devendor.patch
    rm -frv $_name-$pkgver/pdm/pep517/_vendor
  fi
}

build() {
  cd $_name-$pkgver
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd $_name-$pkgver

  # set default git config for test
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
  pytest -vv
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -vDm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
  install -vDm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname/"
}
