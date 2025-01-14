# Maintainer: Xeonacid <h.dwwwwww@gmail.com>

_name=ckzg
pkgname=python-${_name}
pkgver=2.0.1
pkgrel=1
pkgdesc="A minimal implementation of the Polynomial Commitments API for EIP-4844 and EIP-7594, written in C."
arch=(x86_64)
url="https://github.com/ethereum/c-kzg-4844"
license=(MIT)
depends=(glibc python)
makedepends=(git python-build python-installer python-setuptools python-wheel)
source=(git+https://github.com/ethereum/c-kzg-4844.git#tag=v$pkgver
        git+https://github.com/supranational/blst.git)
sha512sums=('8267263ef93cee47669651cdb499028ed8f58e3174ae197f02e7e1f05680ce927cc5c8d3629143c7ef9ba562baa3e3ef719242113b00f4b349121bbcd7045f2e'
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
