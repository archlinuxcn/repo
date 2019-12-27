# Maintainer: Damjan Georgievski <gdamjan@gmail.com>

pkgname=nextcloud-app-totp
_releasename=twofactor_totp
pkgver=4.1.1
pkgrel=1
pkgdesc="Two factor TOTP provider for Nextcloud"
arch=('any')
url="https://github.com/nextcloud/twofactor_totp/"
license=('AGPL')
depends=('nextcloud>=17.0')
makedepends=()
options=('!strip')
source=("${_releasename}-${pkgver}.tar.gz"::"${url}/releases/download/v${pkgver}/${_releasename}.tar.gz")

package() {
    install -d --owner=root --group=root $pkgdir/usr/share/webapps/nextcloud/apps/
    cp -r --target-directory=$pkgdir/usr/share/webapps/nextcloud/apps/ $srcdir/$_releasename
}

sha256sums=('a46bb7de7f7ae73edc316e7b678ea78ccbad3a9e7df181893ddc69e384c6feb2')
