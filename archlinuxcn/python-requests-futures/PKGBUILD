# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Alexander 'z33ky' Hirsch <1zeeky@gmail.com>

pkgname=python-requests-futures
pkgver=1.0.0
pkgrel=1
pkgdesc='Asynchronous Python HTTP for Humans.'
license=('Apache')
arch=('any')
url='https://github.com/ross/requests-futures'
depends=('python-requests')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/r/requests-futures/requests-futures-${pkgver}.tar.gz")
sha256sums=('35547502bf1958044716a03a2f47092a89efe8f9789ab0c4c528d9c9c30bc148')

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
