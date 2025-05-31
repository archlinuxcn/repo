# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=vyper
pkgver=0.4.2
pkgrel=1
pkgdesc="Pythonic Smart Contract Language for the EVM"
arch=(any)
url="https://github.com/vyperlang/$pkgname"
license=(Apache-2.0)
depends=(python python-cbor2 python-asttokens python-pycryptodome python-lark-parser python-packaging python-importlib-metadata)
makedepends=(git python-build python-installer python-setuptools python-wheel python-pytest-runner python-setuptools-scm python-sphinx python-sphinx-copybutton)
source=(git+https://github.com/vyperlang/vyper.git#tag=v$pkgver)
sha512sums=('f2d5d85994410341b0934f5b33716239a51facd182d618304f4b67b6adf5eb769b34887993a71266b27b6e8c7498ccb7c161de4a2e0587280e7bb3ebb6ab33cc')

prepare() {
  cd $pkgname
  sed -i 's/setuptools_scm>=7.1.0,<8.0.0/setuptools_scm/' setup.py
}

build() {
  cd $pkgname
  python -m build --wheel --no-isolation
  make -C docs man
}

package() {
  cd $pkgname
  python -m installer --destdir="$pkgdir" dist/*.whl
  rm -f "$pkgdir/usr/vyper_git_commithash.txt"
  install -Dm644 docs/_build/man/vyper.1 -t "$pkgdir/usr/share/man/man1"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
