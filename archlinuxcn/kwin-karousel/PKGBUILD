# Maintainer: Heddxh <g311571057 at gmail dot com>

_pkgname=karousel
pkgname=kwin-karousel
pkgver=0.14
pkgrel=1
pkgdesc='KWin tiling script with scrolling '
arch=('any')
url='https://github.com/peterfajdiga/karousel/'
license=('GPL-3.0-or-later')
depends=('qt6-declarative' 'knotifications')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/peterfajdiga/karousel/releases/download/v$pkgver/karousel_${pkgver//./_}.tar.gz")
sha1sums=('c3c6d1d53f02240dff159b2845c02785399556ae')

package() {
    install -D -o root -m 755 -d "$pkgdir/usr/share/kwin/scripts/karousel"
    cp -r ${_pkgname}/* "$pkgdir/usr/share/kwin/scripts/karousel/"
}
