# Maintainer: Yufan You <ouuansteve at gmail>

_pkgname=mathlibtools
pkgname=python-$_pkgname
pkgver=1.3.2
pkgrel=1
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
sha256sums=('9a49f4cb7355fda72792a5738bcc5df927b1e102efc719adfbe16db199a0ac6b')

build() {
  cd "$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
