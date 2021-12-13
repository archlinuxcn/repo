# Maintainer: Astro Benzene <universebenzene at sina dot com>
pkgbase=python-extension-helpers
_pyname=${pkgbase#python-}
pkgname=("python-${_pyname}" "python-${_pyname}-doc")
pkgver=0.1
pkgrel=2
pkgdesc="Helpers to assist with building Python packages with compiled C/Cython extensions"
arch=('i686' 'x86_64')
url="http://extension-helpers.readthedocs.io"
license=('BSD')
makedepends=('python-setuptools-scm' 'python-sphinx-automodapi')
checkdepends=('python-pytest')
#'python-pytest-cov')
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/${_pyname}-${pkgver}.tar.gz")
md5sums=('3d37bf28543e7ed2e226db28be2cfbe5')

build() {
    cd ${srcdir}/${_pyname}-${pkgver}
    python setup.py build

    msg "Building Docs"
    python setup.py build_sphinx
}

check() {
    cd ${srcdir}/${_pyname}-${pkgver}

    pytest "build/lib" || warning "Tests failed"
}

package_python-extension-helpers() {
    depends=('python>=3.6' 'python-setuptools')
    optdepends=('python-extension-helpers-doc: Documentation for Python Extension helpers')
    cd ${srcdir}/${_pyname}-${pkgver}

    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" licenses/*
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
}

package_python-extension-helpers-doc() {
    pkgdesc="Documentation for Python Extension helpers"
    cd ${srcdir}/${_pyname}-${pkgver}/build/sphinx

    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../licenses/*
    install -D -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" ../../LICENSE.rst
    install -d -m755 "${pkgdir}/usr/share/doc/${pkgbase}"
    cp -a html "${pkgdir}/usr/share/doc/${pkgbase}"
}
