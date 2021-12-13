# Maintainer: Yufan You <ouuansteve at gmail>

_pkgname=mathlibtools
pkgname=python-$_pkgname
pkgver=1.1.0
pkgrel=3
pkgdesc='This package contains leanproject, a supporting tool for Lean mathlib'
arch=('any')
url="https://github.com/leanprover-community/mathlib-tools"
license=('Apache')
depends=(
  'python-toml'
  'python-pygithub'
  'python-certifi'
  'python-gitpython'
  'python-requests'
  'python-click'
  'python-tqdm'
  'python-networkx'
  'python-pydot'
  'python-yaml'
  'python-atomicwrites'
)
makedepends=('python-setuptools')
optdepends=('lean-community')
source=("https://pypi.io/packages/source/${_pkgname:0:1}/${_pkgname}/$_pkgname-$pkgver.tar.gz")
sha256sums=('789f070f35424e89e4f2e2c007382250133cc48877627e37c5c463bcf4a1b58a')

build() {
  cd "$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
