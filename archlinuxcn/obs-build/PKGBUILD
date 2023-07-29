# Maintainer: Yurii Kolesykov <root@yurikoles.com>
# Contributor: Carson Black <uhhadd AT gmail DOT com>
# Contributor: Johannes Dewender arch at JonnyJD dot net
# Contributor: Eduardo Robles Elvira <edulix AT gmail DOT com>
# Contributor: Jon Nordby <jononor@gmail.com>

pkgname=obs-build
pkgver=20230105
pkgrel=1
license=(GPL)
pkgdesc='OBS build script, can be used with OBS or stand alone'
url=https://github.com/openSUSE/obs-build
arch=(any)
depends=(perl)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/openSUSE/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('ff519234c06dfe3711a1e1964c65b9948380382c29439df07e1e97962803beb7')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}
