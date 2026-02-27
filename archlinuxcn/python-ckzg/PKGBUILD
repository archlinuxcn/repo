# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=ckzg
pkgname=python-${_name}
pkgver=2.1.6
pkgrel=1
pkgdesc="A minimal implementation of the Polynomial Commitments API for EIP-4844 and EIP-7594, written in C."
arch=(x86_64)
url="https://github.com/ethereum/c-kzg-4844"
license=(MIT)
depends=(glibc python)
makedepends=(git python-build python-installer python-setuptools python-wheel)
source=(git+https://github.com/ethereum/c-kzg-4844.git#tag=v$pkgver
        git+https://github.com/supranational/blst.git)
sha512sums=('f04ca0fa3419961cd531f7867837f35030babe7f0cbd198ae6be3b0beff2de8d3f0719cc915cfc05cc869125d15266537b6a4f9d477f8ccccf7ad3ef0f01adff'
            'SKIP')

prepare() {
  cd c-kzg-4844
  git submodule init blst
  git config submodule.blst.url ../blst
  git -c protocol.file.allow=always submodule update blst

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
