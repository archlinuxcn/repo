# Maintainer: Jiachen Yang <farseerfc@gmail.com>
# Maintainer: Ariel AxionL <axiionl@aosc.io>

pkgname=netease-musicbox
_gitname=musicbox
_pyname=NetEase-MusicBox
pkgver=0.3.1
pkgrel=2
pkgdesc="A sexy command line interface musicbox for NetEase based on Python"
arch=(any)
url="https://github.com/darknessomi/musicbox"
depends=('mpg123' 'python-pycryptodomex' 'python-requests' 'python-future' 
         'python-fuzzywuzzy' 'python-requests-cache' 'python-importlib-metadata')
makedepends=('python-setuptools' 'python-poetry')
optdepends=('aria2: music caching'
            'libnotify: notifications'
            'qt5-base: lyrics support'
            'python-qtpy: lyrics support'
            'python-pyqt5: lyrics support'
            'python-dbus: lyrics support'
            'python-levenshtein: fuzzy search support')
provides=('musicbox')
conflicts=('netease-musicbox-git')
license=('MIT')

source=("musicbox-$pkgver.tar.gz::https://github.com/darknessomi/musicbox/archive/${pkgver}.tar.gz"
        "LICENSE::https://raw.githubusercontent.com/darknessomi/musicbox/master/LICENSE")

sha256sums=('b7f984b0462b553ebc8fccb414783b07936efa49fdd1822d2c79a4c8aa624f4e'
            '40aaf7aea7939284b07c487929472fa9cc5a842ff5f0c1e474ac93e6de7aa64e')

build() {
    cd "${srcdir}/musicbox-${pkgver}"
    poetry build -f sdist
    tar xvf "./dist/${_pyname}-${pkgver}.tar.gz"
}

package() {
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    cd "${srcdir}/musicbox-${pkgver}"/${_pyname}-${pkgver}
    python setup.py install --root="${pkgdir}/" --optimize=1
}
# vim:set ts=4 sw=4 et:
