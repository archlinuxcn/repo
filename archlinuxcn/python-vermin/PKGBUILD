# Maintainer: mark.blakeney at bullet-systems dot net
_pkgname="vermin"
pkgname="python-$_pkgname"
pkgver=1.8.0
pkgrel=1
pkgdesc="Concurrently detect the minimum Python versions needed to run code"
url="https://github.com/netromdk/$_pkgname"
license=(MIT)
arch=(any)
depends=("python>=3.0")
makedepends=(python-setuptools python-build python-installer python-wheel)
_pkgtag="$_pkgname-$pkgver"
_pkgtar="$_pkgtag.tar.gz"
source=("$_pkgtar::$url/archive/v$pkgver.tar.gz")
noextract=("$_pkgtar")
md5sums=('113043fea13ac31e7cb5aa19d338ca70')

prepare() {
  mkdir -p "$_pkgtag"
  tar xf "$_pkgtar" -C "$_pkgtag" --strip-components 1
}

build() {
  cd "$_pkgtag"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_pkgtag"
  python -m installer --destdir="$pkgdir" dist/*.whl
}

# vim:set ts=2 sw=2 et:
