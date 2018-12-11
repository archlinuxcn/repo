# Maintainer: Damjan Georgievski <gdamjan@gmail.com>

pkgname=nextcloud-app-totp
_releasename=twofactor_totp
pkgver=2.0.1
pkgrel=1
pkgdesc="Two factor TOTP provider for nextcloud"
arch=('any')
url="https://github.com/nextcloud/twofactor_totp/"
license=('AGPL')
depends=('nextcloud>=15.0')
makedepends=()
options=('!strip')
source=("${_releasename}-${pkgver}.tar.gz"::"${url}/releases/download/v${pkgver}/${_releasename}.tar.gz"
        'php-7.3.patch')

build() {
    cd "$srcdir/${_releasename}"
    patch -p1 -i "$srcdir/php-7.3.patch"
}

package() {
    install -d --owner=root --group=root $pkgdir/usr/share/webapps/nextcloud/apps/
    cp -r --target-directory=$pkgdir/usr/share/webapps/nextcloud/apps/ $srcdir/$_releasename
}

sha256sums=('a882baae7ffe7e3613f4f292ea694fff676a3f9d5508794a76da42225edeba44'
            '69e1a5a5e6c02690e4317ca8a28a51bbf59cb62eb42e78a9c0d2ea940079ba50')
