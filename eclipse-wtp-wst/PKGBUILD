# Maintainer: Hugo Osvaldo Barrera <hugo@barrera.io>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-wtp-wst
pkgver=3.6.0
_pkgbuild=20140602160322
pkgrel=1
pkgdesc="Web Developer Tools for the Eclipse platform - part of webtools, includes enough to do web development (e.g. HTML, CSS, Javascript, and XML)"
url="http://www.eclipse.org/webtools/"
arch=('any')
license=('EPL')
depends=('eclipse-emf' 'eclipse-gef')
makedepends=('unzip')
conflicts=('eclipse-wtp')
provides=('eclipse-wtp')
#changelog=$pkgname.changelog
source=("http://www.eclipse.org/downloads/download.php?r=1&file=/webtools/downloads/drops/R${pkgver}/R-$pkgver-${_pkgbuild}/wtp4x-sdk-R-$pkgver-${_pkgbuild}.zip")
sha256sums=('1cfd0c6370d624401fcbdaa99ce16e9148479b2ba35c8ceacff1aa7f209dedca')

package() {

  _dest=${pkgdir}/usr/share/eclipse/dropins/${pkgname/eclipse-}/eclipse

  cd ${srcdir}/eclipse

  # Features
  find features -type f | while read _feature ; do
    if [[ ${_feature} =~ (.*\.jar$) ]] ; then
      install -dm755 ${_dest}/${_feature%*.jar}
      cd ${_dest}/${_feature/.jar}
      jar xf ${srcdir}/${_feature} || return 1
    else
      install -Dm644 ${_feature} ${_dest}/${_feature}
    fi
  done

  # Plugins
  find plugins -type f | while read _plugin ; do
    install -Dm644 ${_plugin} ${_dest}/${_plugin}
  done
}
