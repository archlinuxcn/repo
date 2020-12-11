# Maintainer: Miguel de Val-Borro <miguel.deval at gmail dot com>
# Contributor: Universebenzene <universebenzene at sina dot com>
pkgname=('python-astropy-helpers')
pkgver=4.0.1
pkgrel=4
pkgdesc="Utilities used for building the Astropy python library for astronomy"
arch=('any')
url="https://astropy-helpers.readthedocs.io/"
license=('BSD')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/a/astropy-helpers/astropy-helpers-${pkgver}.tar.gz"
        'use_system_astropy_helpers.patch')
md5sums=('e626e395b4eac6784acb45c5f56e6706'
         'cc001e2567642396d2eebabc2c323c26')

prepare() {
    cd ${srcdir}/astropy-helpers-${pkgver}

    patch -Np1 -i "${srcdir}/use_system_astropy_helpers.patch"
}

package() {
    optdepends=("python-astropy-helpers-doc=${pkgver}: Documentation for Astropy helpers")
    cd ${srcdir}/astropy-helpers-${pkgver}
    install -D -m644 LICENSE.rst -t "${pkgdir}/usr/share/licenses/${pkgname}"
    install -m644 -t "${pkgdir}/usr/share/licenses/${pkgname}" licenses/*
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
    python setup.py install --prefix=/usr --root=${pkgdir} --optimize=1
}
