# Maintainer: Miguel de Val-Borro <miguel.deval at gmail dot com>
# Maintainer: Universebenzene <universebenzene at sina dot com>

pkgname=('python-astropy-helpers')
pkgver=4.0.1
pkgrel=8
pkgdesc="Utilities used for building the Astropy python library for astronomy"
arch=('any')
url="https://astropy-helpers.readthedocs.io/"
license=('BSD-3-Clause')
makedepends=('python-setuptools'
             'python-wheel'
             'python-build'
             'python-installer')
source=("https://files.pythonhosted.org/packages/source/a/astropy-helpers/astropy-helpers-${pkgver}.tar.gz"
        'fix-importlib.patch')
md5sums=('e626e395b4eac6784acb45c5f56e6706'
         'b289870dcc9fe1c7744868b454d3cad4')

get_pyver() {
    python -c "import sys; print('$1'.join(map(str, sys.version_info[:2])))"
}

build() {
    cd ${srcdir}/astropy-helpers-${pkgver}

    python -m build --wheel --no-isolation
}

prepare() {
    cd ${srcdir}/astropy-helpers-${pkgver}

    sed -e "/astropy_helpers/s:astropy_helpers:/usr/lib/python$(get_pyver .)/site-packages/astropy_helpers:" \
        -i "astropy_helpers/commands/build_sphinx.py"
    patch -Np1 -i "${srcdir}/fix-importlib.patch"
}

package() {
    optdepends=("python-astropy-helpers-doc=${pkgver}: Documentation for Astropy helpers")
    cd ${srcdir}/astropy-helpers-${pkgver}
    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" licenses/*
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
