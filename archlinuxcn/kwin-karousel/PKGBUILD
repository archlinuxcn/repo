# Maintainer: Heddxh <g311571057 at gmail dot com>

_pkgname=karousel
pkgname=kwin-karousel
pkgver=0.15
pkgrel=1
pkgdesc='KWin tiling script with scrolling '
arch=('any')
url='https://github.com/peterfajdiga/karousel/'
license=('GPL-3.0-or-later')
depends=('qt6-declarative' 'knotifications')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/peterfajdiga/karousel/releases/download/v$pkgver/karousel_${pkgver//./_}.tar.gz")
sha1sums=('1ec96fb0f1d585aaf66abc58586add91582b3bc4')

package() {
    install -D -o root -m 755 -d "$pkgdir/usr/share/kwin/scripts/karousel"
    cp -r ${_pkgname}/* "$pkgdir/usr/share/kwin/scripts/karousel/"
}
