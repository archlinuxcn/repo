# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from https://aur.archlinux.org/packages/nextcloud-app-ocsms/
# Original contributors:
# Contributor: Polichronucci <nick at discloud dot eu>

pkgname=nextcloud-app-ocsms
pkgver=2.0.2
pkgrel=2
epoch=1
pkgdesc="Push your Android SMS to your Nextcloud instance."
arch=('any')
url="https://apps.nextcloud.com/apps/ocsms"
license=('AGPL')
depends=('nextcloud')
options=('!strip')
source=("https://github.com/nextcloud/ocsms/releases/download/$pkgver/ocsms-$pkgver.tar.gz")
sha512sums=('a11e355c0034ad5241ee6095d7ec2952a32a636db4220c87c817c50dd0e92dddc44ead14f4395bef1d0efaf629263e7278cbe92bfcdac4aaf4afafcf67fa0b16')

package() {
  install -d "${pkgdir}/usr/share/webapps/nextcloud/apps"
  cp -a "${srcdir}/ocsms" "${pkgdir}/usr/share/webapps/nextcloud/apps/ocsms"
}
