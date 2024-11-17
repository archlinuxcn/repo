# Maintainer: Haoyang Liu <tttturtleruss@gmail.com>
# Contributor: m8D2 <omui (at) proton mail (dot) com>
# Contributor: novenary <streetwalkermc@gmail.com>
# Contributor: Daniel M. Capella <polyzen@archlinux.org>

pkgname=python-soco
pkgver=0.30.6
pkgrel=1
pkgdesc="A Python library that allows you to control Sonos speakers programmatically"
arch=('any')
url="https://github.com/SoCo/SoCo"
license=('MIT')
depends=('python' 'python-requests' 'python-xmltodict' 'python-ifaddr' 'python-twisted' 'python-aiohttp' 'python-appdirs' 'python-lxml')
makedepends=('python-build' 'python-installer')
source=("SoCo-$pkgver.tar.gz::https://github.com/SoCo/SoCo/archive/v$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
  cd SoCo-$pkgver
  python3 -m build
}

package() {
  cd SoCo-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 -t "$pkgdir"/usr/share/licenses/$pkgname LICENSE.rst
}

# vim:set ts=2 sw=2 et:
