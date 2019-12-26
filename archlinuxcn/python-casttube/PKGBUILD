# Maintainer: Sibren Vasse <arch@sibrenvasse.nl>

_name='casttube'
pkgname="python-$_name"
pkgver='0.2.0'
pkgrel=2
pkgdesc="YouTube chromecast api"
url="http://github.com/ur1katz/casttube"
depends=('python' 'python-requests')
makedepends=('python-setuptools')
license=('MIT')
arch=('any')
source=("https://github.com/ur1katz/casttube/archive/${pkgver}.tar.gz")
sha256sums=('5dffe63803914ccd0f311940dc49865c4cd0bd4461f901c27a0ef22b3338cd14')

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
