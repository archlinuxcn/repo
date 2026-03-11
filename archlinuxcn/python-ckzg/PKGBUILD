# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=ckzg
pkgname=python-${_name}
pkgver=2.1.7
pkgrel=1
pkgdesc="A minimal implementation of the Polynomial Commitments API for EIP-4844 and EIP-7594, written in C."
arch=(x86_64)
url="https://github.com/ethereum/c-kzg-4844"
license=(MIT)
depends=(glibc python)
makedepends=(git python-build python-installer python-setuptools python-wheel)
source=(git+https://github.com/ethereum/c-kzg-4844.git#tag=v$pkgver
        git+https://github.com/supranational/blst.git)
sha512sums=('cc5b3e84f52dc5be98f41d18f7d2487d1e2ebd1b24415bb6282b41978818f01e13dfb87ff220d0a2ba2594e8122f1e9648f54f8fa32a987aa3ac53bb6aaba2dd'
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
