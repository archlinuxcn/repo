# Maintainer: Hyacinthe Cartiaux <hyacinthe.cartiaux@free.fr>

pkgname=prettyping-hg
pkgver=20131019
pkgrel=1
pkgdesc="prettyping.sh: a better UI for watching ping responses"
arch=('any')
url="http://my.opera.com/CrazyTerabyte/blog/2013/10/18/prettyping-sh-a-better-ui-for-watching-ping-responses"
license=('MIT')
depends=('iputils' 'bash' 'awk')
replaces=prettyping-mercurial
conflicts=prettyping-mercurial
source=()
md5sums=()

_mercurial=https://bitbucket.org/denilsonsa/small_scripts/raw/tip/prettyping.sh

package() {
  mkdir -p ${pkgdir}/usr/bin
  curl $_mercurial -o ${pkgdir}/usr/bin/prettyping.sh
  chmod 755 ${pkgdir}/usr/bin/prettyping.sh
}

