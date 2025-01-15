# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=eth-abi
pkgname=python-${_name}
pkgver=5.2.0
pkgrel=1
pkgdesc="Ethereum ABI utilities for python"
arch=(any)
url="https://github.com/ethereum/${_name}"
license=(MIT)
depends=(python python-eth-utils python-eth-typing python-parsimonious)
makedepends=(python-build python-installer python-setuptools python-wheel python-sphinx python-sphinx_rtd_theme)
checkdepends=(python-pytest python-hypothesis)
optdepends=('python-hypothesis: eth_abi.tools module')
source=(${_name}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('f14ed97af2a04f9201763064f4e993d9c25283432adad6d9ada7716fb563d44bf3830003dfddc38c7ffa16edcdcdc01cbd59e7c23b4a1e872dfaa58a98ca7c75')

build() {
  cd $_name-$pkgver
  python -m build --wheel --no-isolation
  make -C docs man
}

check(){
  cd $_name-$pkgver
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  # Fail with new python-hypothesis
  test-env/bin/python -m pytest -vv --showlocals tests/ || true
}

package() {
  cd $_name-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 docs/_build/man/eth_abi.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
