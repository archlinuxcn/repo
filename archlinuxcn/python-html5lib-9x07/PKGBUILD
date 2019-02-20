# Contributor: Erol V. Aktay <e.aktay@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>
# Maintainer: Philipp A. <flying-sheep@web.de>

_pkgnm=python-html5lib
pkgname=python-html5lib-9x07
pkgdesc="A Python HTML parser/tokenizer based on the WHATWG HTML5 spec (v0.9999999 as dep for bleach)"
pkgver=0.9999999
pkgrel=1
provides=("$_pkgnm=$pkgver")
conflicts=("$_pkgnm")
arch=('any')
url="https://github.com/html5lib"
license=('MIT')
depends=('python' 'python-six' 'python-webencodings')
makedepends=('python2' 'python' 'unzip' 'python-webencodings' 'python2-webencodings')
checkdepends=('python-six' 'python-pytest' 'python-lxml' 'python2-lxml' 'python-mock')
source=("$_pkgnm-$pkgver.tar.gz::https://github.com/html5lib/html5lib-python/archive/$pkgver.tar.gz"
    LICENSE)
md5sums=('2ca78b1ec5852779bc121a97da6e8d4d'
         '838c366f69b72c5df05c96dff79b35f2')

package() {
    cd "$srcdir/html5lib-python-$pkgver"

    python3 setup.py install --root="$pkgdir"
    install -Dm755 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

check() {
    cd "$srcdir/html5lib-python-$pkgver/html5lib/tests"

    #nosetests
}
