# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
# Contributor: Sibren Vasse <arch@sibrenvasse.nl>
pkgname=python-casttube
_name=${pkgname#python-}
pkgver=0.2.1
pkgrel=4
pkgdesc="YouTube Chromecast API"
arch=('any')
url="http://github.com/ur1katz/casttube"
license=('MIT')
depends=('python-requests')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('54d2af8c7949aa9c5db87fb11ef0a478a5d3e7ac6d2d2ac8dd1711e3a516fc82')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/LICENSE" "$pkgdir/usr/share/licenses/$pkgname"
}
