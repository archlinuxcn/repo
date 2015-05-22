# Maintainer: wenLiangcan <boxeed at gmail dot com>

pkgname=('pyfm' 'python2-pyfm')
pkgver=0.2.4
pkgrel=1
pkgdesc="A Tiny and Smart Terminal Player of douban.fm."
url="https://github.com/skyline75489/pyfm"
depends=('mpg123')
optdepends=('libnotify: for system notification')
license=('MIT')
arch=('any')
source=("https://pypi.python.org/packages/source/p/pyfm/pyfm-${pkgver}.tar.gz")
sha512sums=('34600528dfe79d28bb0879890b9bd3a26d69afb99deb88bd5a97ba66c8939cbff06028a6d59f88357807400fbe33a6ffe18b149244985e633f5a4067c4ddb91c')

prepare() {
    cp -a "${srcdir}/pyfm-${pkgver}"{,-python2}
}

package_pyfm() {
    depends+=('python-requests' 'python-urwid')
    makedepends=('python-setuptools')
    cd "pyfm-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1
}

package_python2-pyfm() {
    depends+=('python2-requests' 'python2-urwid')
    makedepends=('python2-setuptools')
    cd "pyfm-${pkgver}-python2"
    python2 setup.py install --root="${pkgdir}" --optimize=1
    mv "${pkgdir}/usr/bin/pyfm"{,2}
}
