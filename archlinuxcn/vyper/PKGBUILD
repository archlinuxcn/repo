# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

pkgname=vyper
pkgver=0.4.1
pkgrel=1
pkgdesc="Pythonic Smart Contract Language for the EVM"
arch=(any)
url="https://github.com/vyperlang/$pkgname"
license=(Apache-2.0)
depends=(python python-cbor2 python-asttokens python-pycryptodome python-lark-parser python-packaging python-importlib-metadata)
makedepends=(git python-build python-installer python-setuptools python-wheel python-pytest-runner python-setuptools-scm python-sphinx python-sphinx-copybutton)
source=(git+https://github.com/vyperlang/vyper.git#tag=v$pkgver)
sha512sums=('1a1576453e8af67e4f860e1c3c4a4fc89fd9bb0243843b258bcb43b802fa6f028471486ca0b74de32444b2f0d3728ff0cc6b23b8e91fd66c6a5abc44d996289c')

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
