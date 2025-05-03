# Maintainer: Heddxh <g311571057 at gmail dot com>

_pkgname=karousel
pkgname=kwin-karousel
pkgver=0.13
pkgrel=1
pkgdesc='KWin tiling script with scrolling '
arch=('any')
url='https://github.com/peterfajdiga/karousel/'
license=('GPL-3.0-or-later')
depends=('qt6-declarative' 'knotifications')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/peterfajdiga/karousel/releases/download/v$pkgver/karousel_${pkgver//./_}.tar.gz")
sha1sums=('75efa53c3ad30c8fa27df8ca1592ea93d982b3a4')

package() {
    install -D -o root -m 755 -d "$pkgdir/usr/share/kwin/scripts/karousel"
    cp -r ${_pkgname}/* "$pkgdir/usr/share/kwin/scripts/karousel/"
}
