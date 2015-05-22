# Maintainer: googol <googol@posteo.de>
# Former maintainer: Oliver Mangold <o.mangold at gmail dot com>
pkgname=python-alembic
pkgver=0.7.6
pkgrel=1
pkgdesc="Lightweight dababase migration tool for usage with SQLAlchemy"
arch=('any')
license=('MIT')
url=('https://bitbucket.org/zzzeek/alembic')
makedepends=('python-distribute')
source=(https://pypi.python.org/packages/source/a/alembic/alembic-${pkgver}.tar.gz)
        #https://pypi.python.org/packages/source/a/alembic/alembic-${pkgver}.tar.gz.asc)

sha256sums=('864fa461265d6c97bcefee603e9ef0b6385bda9063d41b3db3e010abbba5ef61')
            #'c1391272683e3ff178b4a87930a2e18fe348b3bb72703f75e5e9510e13042c48')
depends=('python' 'python-mako' 'python-sqlalchemy')
provides=("${pkgname}")

build() {
  cd "${srcdir}/alembic-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/alembic-${pkgver}"
  python setup.py install --root "${pkgdir}"
  install -m 755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m 644 "${srcdir}/alembic-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
