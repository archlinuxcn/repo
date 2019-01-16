# Maintainer: kfgz <kfgz at interia dot pl>
# Contributor: Lukas Fleischer <archlinux at cryptocrack dot de>

pkgname=codecs64
pkgver=20071007
pkgrel=1
pkgdesc="Non-linux native codec pack."
arch=('x86_64')
url="http://www.mplayerhq.hu/design7/dload.html"
license=('other')
depends=('gcc-libs')
conflicts=('codecs-extra' 'codecs')
replaces=('codecs-extra' 'codecs')
options=('!strip')
source=(http://www.mplayerhq.hu/MPlayer/releases/codecs/essential-amd64-${pkgver}.tar.bz2)
md5sums=('8e1ceeec51469f5baac65e56fac709e8')

package() {
  install -d "${pkgdir}"/usr/lib/codecs
  install -m644 "${srcdir}"/essential-amd64-${pkgver}/* "${pkgdir}"/usr/lib/codecs
}
