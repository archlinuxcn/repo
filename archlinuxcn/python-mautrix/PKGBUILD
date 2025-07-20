# Contributor: BluePeril <blueperil (at) blueperil _dot_ de>

pkgname=python-mautrix
pkgver=0.20.8
pkgrel=1
pkgdesc="A Python 3 asyncio Matrix framework."
url="https://github.com/mautrix/python/"
depends=('python' 'python-aiohttp' 'python-attrs' 'python-yarl')
makedepends=('python-setuptools' 'python-build' 'python-installer' 'python-wheel')
license=('MPL')
arch=('any')
source=("${pkgname}-${pkgver/_rc/-rc}.tar.gz"::"https://github.com/mautrix/python/archive/v${pkgver/_rc/-rc}.tar.gz")
sha256sums=('01011373288eb981caa98e211fe493982b8deed1f5c6763f9e24b882fcda7815')

build() {
    cd python-${pkgver/_rc/-rc}
    python -m build --wheel --no-isolation
}

package() {
    cd python-${pkgver/_rc/-rc}
    python -m installer --destdir="$pkgdir" dist/*.whl
}
