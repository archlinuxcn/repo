# Maintainer: mutantmonkey <aur@mutantmonkey.mx>
# Contributor: Kyle Sferrazza <kyle.sferrazza@gmail.com>
# Contributor: Dimitrios Vogiatzis <me@dimtree.net>

pkgname=python-plexapi
_name="PlexAPI"
source=("$pkgname-$pkgver.tar.gz::https://github.com/pkkid/python-plexapi/archive/$pkgver.tar.gz")
pkgver=4.2.0
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
sha256sums=('1e9b5467e8550a3cdd43db16fa4b501c103673fcc70a0543505bdc58b0909b99')

package() {
    cd "$_name-$pkgver"
    python ./setup.py install --root="$pkgdir/" --prefix=/usr --optimize=1
}
