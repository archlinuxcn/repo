# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=ckzg
pkgname=python-${_name}
pkgver=2.1.2
pkgrel=1
pkgdesc="A minimal implementation of the Polynomial Commitments API for EIP-4844 and EIP-7594, written in C."
arch=(x86_64)
url="https://github.com/ethereum/c-kzg-4844"
license=(MIT)
depends=(glibc python)
makedepends=(git python-build python-installer python-setuptools python-wheel)
source=(git+https://github.com/ethereum/c-kzg-4844.git#tag=v$pkgver
        git+https://github.com/supranational/blst.git)
sha512sums=('bb530beefbb8d8585c68d16f431f617018ea22be4516b0c3840cb165e1bb8ad981c5723ee53636e341154e3646e1123f77d7575dc960bd9e638a4b985a0ec3c4'
            'SKIP')

prepare() {
  cd c-kzg-4844
  git config --global protocol.file.allow always
  git submodule init blst
  git config submodule.blst.url ../blst
  git submodule update blst

  # Conflict with $CFLAGS
  sed -i 's/-Werror//g' src/Makefile
}

build() {
  cd c-kzg-4844
  python -m build --wheel --no-isolation
}

package() {
  cd c-kzg-4844
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
}
