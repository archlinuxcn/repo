# Maintainer: Benjamin A. Shelton <zancarius@gmail.com>
# Source: https://github.com/zancarius/archlinux-pkgbuilds
pkgname=python2-raven
pkgver=5.5.0
pkgrel=1
pkgdesc="Python client for Sentry."
arch=(any)
url="http://pypi.python.org/pypi/raven"
license=(BSD)
depends=(python2 python2-service-identity)
makedepends=(python2-setuptools)
source=("https://pypi.python.org/packages/source/r/raven/raven-${pkgver}.tar.gz")
md5sums=(7e7961562bce6cb6fcf54c3427cf043e)

package () {

    cd "${srcdir}/raven-${pkgver}"
    /usr/bin/python2 setup.py install --root="${pkgdir}/" --optimize=1
    install -Dm0664 "${srcdir}/raven-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

    # Move python2-raven's binary (/usr/bin/raven) to /usr/bin/raven2.
    mv "${pkgdir}/usr/bin/raven" "${pkgdir}/usr/bin/raven2"

}