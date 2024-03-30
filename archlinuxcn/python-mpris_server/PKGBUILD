# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-mpris_server
_name=${pkgname#python-}
pkgver=0.4.2
pkgrel=3
epoch=1
pkgdesc="Integrate MPRIS Media Player support into your app"
arch=('any')
url="https://github.com/alexdelorenzo/mpris_server"
license=('AGPL-3.0-or-later')
depends=('python-gobject' 'python-pydbus' 'python-unidecode' 'python-emoji')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('a779ccf347ce32d46678abce5ee5f8d05bbdc47f203e06329de5db512ebbf1f1')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
