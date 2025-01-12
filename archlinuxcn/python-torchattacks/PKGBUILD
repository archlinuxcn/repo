# Maintainer: Xeonacid <h.dwwwwww@gmail.com>
# Contributor: Wu Zhenyu <wuzhenyu@ustc.edu>

_name=adversarial-attacks-pytorch
_pkgname=torchattacks
pkgname=python-$_pkgname
pkgver=3.5.1
pkgrel=2
pkgdesc="PyTorch implementation of adversarial attacks"
arch=(any)
url=https://github.com/Harry24k/adversarial-attacks-pytorch
depends=(python python-pytorch python-torchvision python-scipy python-tqdm python-requests python-numpy python-setuptools python-pillow python-jinja)
makedepends=(python-build python-installer python-wheel python-sphinx)
license=(MIT)
source=($pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz)
sha256sums=('95cfce9631048d6b781bb273e129af706e22262cdf071bbd6d52256d62f96191')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation

  cd docs
  make man
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"

  MANPAGE="docs/_build/man/torchattacks.1"
  gzip -n "$MANPAGE"
  install -Dm644 "$MANPAGE.gz" "$pkgdir/usr/share/man/man1/torchattacks.1.gz"
}
