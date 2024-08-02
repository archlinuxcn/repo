# Maintainer: Heddxh <g311571057 at gmail dot com>

_pkgname=karousel
pkgname=kwin-karousel
pkgver=0.9.4
pkgrel=1
pkgdesc='KWin tiling script with scrolling '
arch=('any')
url='https://github.com/peterfajdiga/karousel/'
license=('GPL-3.0-or-later')
depends=('kwin')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/peterfajdiga/karousel/releases/download/v$pkgver/karousel_${pkgver//./_}.tar.gz")
sha1sums=('75a481cc8072310a9374632383035d15e2542d47')

package() {
    install -D -o root -m 755 -d "$pkgdir/usr/share/kwin/scripts/karousel"
    cp -r package/* "$pkgdir/usr/share/kwin/scripts/karousel/"
}
