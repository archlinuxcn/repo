# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from https://aur.archlinux.org/packages/nextcloud-app-ocsms/
# Original contributors:
# Contributor: Polichronucci <nick at discloud dot eu>

pkgname=nextcloud-app-ocsms
pkgver=2.1.0
pkgrel=1
epoch=1
pkgdesc="Push your Android SMS to your Nextcloud instance."
arch=('any')
url="https://apps.nextcloud.com/apps/ocsms"
license=('AGPL')
depends=('nextcloud')
options=('!strip')
source=("https://github.com/nextcloud/ocsms/releases/download/$pkgver/ocsms-$pkgver.tar.gz")
sha512sums=('f267aea793828b5fa52f4794883f6643b6dd01ff2a6a59f98689f38973b52d51752ff4bd281a7389a01d716b884412a0dd5fcf2007c83d195802b39aba344d8c')

package() {
  install -d "${pkgdir}/usr/share/webapps/nextcloud/apps"
  cp -a "${srcdir}/ocsms" "${pkgdir}/usr/share/webapps/nextcloud/apps/ocsms"
}
