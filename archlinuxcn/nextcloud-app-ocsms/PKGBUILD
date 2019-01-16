# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from https://aur.archlinux.org/packages/nextcloud-app-ocsms/
# Original contributors:
# Contributor: Polichronucci <nick at discloud dot eu>

pkgname=nextcloud-app-ocsms
pkgver=2.1.1
pkgrel=1
epoch=1
pkgdesc="Push your Android SMS to your Nextcloud instance."
arch=('any')
url="https://apps.nextcloud.com/apps/ocsms"
license=('AGPL')
depends=('nextcloud')
options=('!strip')
source=("https://github.com/nextcloud/ocsms/releases/download/$pkgver/ocsms-$pkgver.tar.gz")
sha512sums=('8dfd7046275e6fe30d1cd4ebdcde89f9cd294b2c33df1400de6e188148039c270e4ea45d0328d2ce204880797bba5140a86653986e47226b81951fd42fcc4aa7')

package() {
  install -d "${pkgdir}/usr/share/webapps/nextcloud/apps"
  cp -a "${srcdir}/ocsms" "${pkgdir}/usr/share/webapps/nextcloud/apps/ocsms"
}
