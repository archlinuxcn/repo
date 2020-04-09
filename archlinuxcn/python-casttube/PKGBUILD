# Maintainer: Sibren Vasse <arch@sibrenvasse.nl>

_name=casttube
pkgname="python-$_name"
pkgver=0.2.1
pkgrel=1
pkgdesc='YouTube chromecast api'
url='http://github.com/ur1katz/casttube'
depends=('python' 'python-requests')
makedepends=('python-setuptools')
license=('MIT')
arch=('any')
source=("https://github.com/ur1katz/casttube/archive/${pkgver}.tar.gz")
sha256sums=('351819818a10a107641675cab71c4154afb490762410b3138c18ef410cbf5c33')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
