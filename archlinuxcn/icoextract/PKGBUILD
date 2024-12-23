# Maintainer: Nocifer <apmichalopoulos at gmail dot com>

pkgname=icoextract
pkgver=0.1.5
pkgrel=2
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
sha256sums=('9eddf003b2188a1c81805836fd7bd9b157c6ed16d0db1b51121f2bb8bee1963a')

build() {
    cd ${pkgname}-${pkgver}

    python -m build --wheel --no-isolation
}

package() {
    cd ${pkgname}-${pkgver}

    python -m installer --destdir="${pkgdir}" dist/*.whl

    install -Dm644 exe-thumbnailer.thumbnailer "${pkgdir}"/usr/share/thumbnailers/exe-thumbnailer.thumbnailer

    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
}
