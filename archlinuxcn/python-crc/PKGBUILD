# Maintainer: Popolon <popolon @ popolon. org>
# made with pip2pkgbuild

pkgname='python-crc'
_module='crc'
pkgver='7.1.0'
pkgrel=1
pkgdesc="Library and CLI to calculate and verify all kinds of CRC checksums"
url="https://github.com/Nicoretti/crc"
depends=('python' 'python-poetry')
makedepends=('python-build' 'python-installer' 'python-wheel')
license=('custom:BSD License')
arch=('any')
source=("https://github.com/Nicoretti/crc/releases/download/${pkgver}/${_module}-${pkgver}.tar.gz")
sha256sums=('99dd540909a37ae4f62c65441df8ecb4e7f9af014fecaf4f331052a41d66c07d')

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    depends+=()
    cd "${srcdir}/${_module}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
