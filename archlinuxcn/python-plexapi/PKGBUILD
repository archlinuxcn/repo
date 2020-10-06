# Maintainer: mutantmonkey <aur@mutantmonkey.mx>
# Contributor: Kyle Sferrazza <kyle.sferrazza@gmail.com>
# Contributor: Dimitrios Vogiatzis <me@dimtree.net>

pkgname=python-plexapi
_name="PlexAPI"
source=("$pkgname-$pkgver.tar.gz::https://github.com/pkkid/python-plexapi/archive/$pkgver.tar.gz")
pkgver=4.1.2
pkgrel=1
pkgdesc="Python bindings for the Plex API."
arch=('any')
url="https://github.com/pkkid/python-plexapi"
license=('BSD')
depends=('python-requests'
         'python-tqdm'
         'python-websocket-client')
makedepends=()
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('5de36cc26a1e919dbc7ecc3e62733e1332a6257646cbaca73846238b297d387d')

package() {
    cd "$_name-$pkgver"
    python ./setup.py install --root="$pkgdir/" --prefix=/usr --optimize=1
}
