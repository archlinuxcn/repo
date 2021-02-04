# Maintainer: mutantmonkey <aur@mutantmonkey.mx>
# Contributor: Kyle Sferrazza <kyle.sferrazza@gmail.com>
# Contributor: Dimitrios Vogiatzis <me@dimtree.net>

pkgname=python-plexapi
_name="PlexAPI"
source=("$pkgname-$pkgver.tar.gz::https://github.com/pkkid/python-plexapi/archive/$pkgver.tar.gz")
pkgver=4.3.0
pkgrel=2
pkgdesc="Python bindings for the Plex API."
arch=('any')
url="https://github.com/pkkid/python-plexapi"
license=('BSD')
depends=('python-requests'
         'python-tqdm'
         'python-websocket-client')
makedepends=()
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('40ba5cf064e40ee56116774e1ff19f17fbf88b69b8a0387396d5be5c40d5edf2')

package() {
    cd "$_name-$pkgver"
    python ./setup.py install --root="$pkgdir/" --prefix=/usr --optimize=1
}
