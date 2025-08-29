# Maintainer: nicknb <nicknb at posteo dot com>
# Contributor: Haoyang Liu <tttturtleruss@gmail.com>
# Contributor: m8D2 <omui (at) proton mail (dot) com>
# Contributor: novenary <streetwalkermc@gmail.com>
# Contributor: Daniel M. Capella <polyzen@archlinux.org>

pkgname=python-soco
pkgver=0.30.11
pkgrel=2
pkgdesc="A Python library that allows you to control Sonos speakers programmatically"
arch=('any')
url="https://github.com/SoCo/SoCo"
license=('MIT')
provides=("$pkgname")
conflicts=("$pkgname")
depends=('python' 'python-requests' 'python-xmltodict' 'python-ifaddr' 'python-twisted' 'python-aiohttp' 'python-appdirs' 'python-lxml')
makedepends=('python-build' 'python-installer')
source=("SoCo-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('f06fdae32d6e3a74977f80a1924e661d67e0505d9616cb30a775e128ca42f3dd')

build() {
    cd SoCo-$pkgver
    python3 -m build --wheel --no-isolation
}

package() {
    cd SoCo-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 -t "$pkgdir"/usr/share/licenses/$pkgname LICENSE.rst
}
