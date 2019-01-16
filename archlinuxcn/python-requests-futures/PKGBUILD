# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Alexander 'z33ky' Hirsch <1zeeky@gmail.com>

pkgname=python-requests-futures
pkgver=0.9.9
pkgrel=1
pkgdesc='Asynchronous Python HTTP for Humans.'
license=('Apache')
arch=('any')
url='https://github.com/ross/requests-futures'
depends=('python-requests')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/r/requests-futures/requests-futures-${pkgver}.tar.gz")
sha256sums=('200729e932ec1f6d6e58101a8d2b144d48c9695f0585bc1dcf37139190f699a1')

build() {
    cd requests-futures-$pkgver
    python setup.py build
}

check() {
    cd requests-futures-$pkgver
    python test_requests_futures.py
}

package() {
    cd requests-futures-$pkgver
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
