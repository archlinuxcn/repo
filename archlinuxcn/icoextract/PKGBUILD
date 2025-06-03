# Maintainer: Nocifer <apmichalopoulos at gmail dot com>

pkgname=icoextract
pkgver=0.2.0
pkgrel=1
pkgdesc='Icon extractor for Windows PE files (.exe/.dll) with optional thumbnailer functionality'
arch=('any')
url='https://github.com/jlu5/icoextract'
license=('MIT')
depends=('python-pefile')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
optdepends=('python-pillow: required for the optional thumbnailer')
provides=('exe-thumbnailer')
conflicts=('exe-thumbnailer')
source=("https://github.com/jlu5/${pkgname}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('1bbb9fcbd1e5cf584f2d41df83ceb901a9594110487a670d453dabcf453cfacc')

build() {
    cd ${pkgname}-${pkgver}

    python -m build --wheel --no-isolation
}

package() {
    cd ${pkgname}-${pkgver}

    python -m installer --destdir="${pkgdir}" dist/*.whl

    install -Dm644 exe-thumbnailer.thumbnailer "${pkgdir}"/usr/share/thumbnailers/exe-thumbnailer.thumbnailer
}
