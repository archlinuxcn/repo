# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=ckzg
pkgname=python-${_name}
pkgver=2.1.4
pkgrel=1
pkgdesc="A minimal implementation of the Polynomial Commitments API for EIP-4844 and EIP-7594, written in C."
arch=(x86_64)
url="https://github.com/ethereum/c-kzg-4844"
license=(MIT)
depends=(glibc python)
makedepends=(git python-build python-installer python-setuptools python-wheel)
source=(git+https://github.com/ethereum/c-kzg-4844.git#tag=v$pkgver
        git+https://github.com/supranational/blst.git)
sha512sums=('3eb41d7209b9aad9f5cf3e187099b902c7977ffcff437dbba01e3442747f5559cac7be4aeb70357f36fabdfe7c8f265cf7998a5654aeb4019af796a3675dd8ab'
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
