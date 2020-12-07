# Maintainer: Yufan You <ouuansteve at gmail>

_pkgname=mathlibtools
pkgname=python-$_pkgname
pkgver=1.0.0
pkgrel=2
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
)
makedepends=('python-setuptools')
optdepends=('lean-community')
source=("https://pypi.io/packages/source/m/$_pkgname/$_pkgname-$pkgver.tar.gz")
sha256sums=(da41c65e206f55b1faea303581fc11215e52d6e6990b827336b2e1eb82aad96c)

build() {
  cd "$_pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$_pkgname-$pkgver"
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
}
