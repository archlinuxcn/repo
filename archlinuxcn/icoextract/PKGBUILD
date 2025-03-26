# Maintainer: Nocifer <apmichalopoulos at gmail dot com>

pkgname=icoextract
pkgver=0.1.6
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
sha256sums=('761bcbe00c80939fbc3ac42ee6892d558b2a7a920c997197e80b935eef1eb1ec')

build() {
    cd ${pkgname}-${pkgver}

    python -m build --wheel --no-isolation
}

package() {
    cd ${pkgname}-${pkgver}

    python -m installer --destdir="${pkgdir}" dist/*.whl

    install -Dm644 exe-thumbnailer.thumbnailer "${pkgdir}"/usr/share/thumbnailers/exe-thumbnailer.thumbnailer
}
