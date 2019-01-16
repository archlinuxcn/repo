# Maintainer: Aetf <aetf at unlimitedcodeworks dot xyz>
# Contributor: j605
# Contributor: Thomas Weißschuh <thomas t-8ch de>

pkgbase=python-pipsi
pkgname=(python-pipsi python2-pipsi)
_name=pipsi
pkgver=0.9
pkgrel=3
pkgdesc='Wraps pip and virtualenv to install scripts'
arch=('any')
url='https://github.com/mitsuhiko/pipsi/'
license=('BSD')
makedepends=(python2-setuptools python-setuptools)
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")

sha256sums=('688b688cc8a7a76612c0d4d1839aaef98ece8382d4382b9d8b6f0caa65f0ed34')

# this multipackage trick was copied from community/python-perf
prepare() {
    cp -a ${_name}-${pkgver}{,-py2}
    sed 's|pipsi=|pipsi2=|' -i ${_name}-${pkgver}-py2/setup.py
}

build() {
    (cd "${srcdir}/${_name}-${pkgver}"
        python setup.py build
    )

    (cd "${srcdir}/${_name}-${pkgver}-py2"
        python2 setup.py build
    )
}

package_python-pipsi() {
    depends=(python-virtualenv python-click)
    provides=(pipsi=${pkgver})
    conflicts=(pipsi=${pkgver})

    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py install --root="${pkgdir}/" --optimize=1 --skip-build
    install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/python-pipsi/LICENSE"
}

package_python2-pipsi() {
    depends=(python2-virtualenv python2-click)
    provides=(pipsi2=${pkgver})
    conflicts=(pipsi2=${pkgver})

    cd "${srcdir}/${_name}-${pkgver}-py2"
    python2 setup.py install --root="${pkgdir}/" --optimize=1 --skip-build
    install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/python2-pipsi/LICENSE"
}
